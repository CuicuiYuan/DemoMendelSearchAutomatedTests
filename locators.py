from selenium.webdriver.common.by import By

class MainPageLocators(object):
    # """A class for main page locators. All main page locators should come here"""

    RESULTS = (By.XPATH, "//body[1]/div[9]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/ul[1]/li")
    MAIN_RESULTS = (By.XPATH, "//ul/li/span[@class='name']//mark")
    FIRST_RESULT = (By.XPATH, "//body[1]/div[9]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[1]")
    NO_RESULTS_FOUND = (By.XPATH, "//body[1]/div[9]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[1]/span[1]")