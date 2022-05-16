from element import BasePageElement
from locators import MainPageLocators

class SearchTextElement(BasePageElement):
    # """This class gets the search text from the specified locator"""

    #The locator for search box where search string is entered
    locator = 'search-input'


class BasePage(object):
    # """Base class to initialize the base page that will be called from all
    # pages"""

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    # """Home page action methods come here. I.e. Mendel"""

    #Declares a variable that will contain the retrieved text
    search_text_element = SearchTextElement()

    def is_title_matches(self):
        # """Verifies that the hardcoded text "Mendel" appears in page title"""

        return "Mendel" in self.driver.title

    def result_count(self):
        # """Triggers the search"""

        return len(self.driver.find_elements(*MainPageLocators.RESULTS))

    def results(self):
        return self.driver.find_elements(*MainPageLocators.RESULTS)

    def resultText(self, elem):
        return elem.get_attribute("innerHTML")

    def main_results(self):
        return self.driver.find_elements(*MainPageLocators.MAIN_RESULTS)

    def main_resultText(self, elem):
        return elem.text

    def click_the_first_result(self):
        self.driver.find_element(*MainPageLocators.FIRST_RESULT).click()

    def no_results_found_text(self):
        return self.driver.find_element(*MainPageLocators.NO_RESULTS_FOUND).text
