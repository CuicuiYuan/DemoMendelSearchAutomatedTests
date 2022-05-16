import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service # this is for mac, no need for windows
import page
import HtmlTestRunner
import time

PATH = "/Users/cuicuiyuan/Documents/DemoMendelSearchAutomatedTests/chromedriver"
baseURL = "https://mendel.webflow.io/"
options = webdriver.ChromeOptions()

class MendelAiSearch(unittest.TestCase):
    # """A sample test class to show how page object works"""
    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(PATH), options = options) # initialize chrome driver
        self.driver.get(baseURL)
        self.driver.implicitly_wait(5) #  wait for 10 sec.
        self.driver.maximize_window() #  maximize the browser window

    # @unittest.skip("This test is skipped")
    def test_01_search_in_mendelai_returns_suggestion(self):
        # """Tests mendel.webflow.io search feature. Searches for the word "Mendel" then
        # verified that some results show up.  Note that it does not look for
        # any particular text in search results page. This test verifies that
        # the results were not empty."""


        #Load the main page. In this case the home page of Mendel.webflow.io.
        main_page = page.MainPage(self.driver)
        #Checks if the word "Mendel" is in title
        self.assertTrue(main_page.is_title_matches(), "Mendel.webflow.io title doesn't match.")
        #Sets the text of search textbox to "test"
        main_page.search_text_element = "covid"

        auto_count = main_page.result_count()
        #Verifies that the auto suggested result(s) would  display
        self.assertIsNotNone(auto_count, "There is no auto suggestions.")

    # @unittest.skip("This test is skipped")
    def test_02_search_in_mendelai_match_the_suggestions(self):
        # """Tests mendel.webflow.io search feature. Searches for the word "test" then
        # verified that some results show up.  Note any auto result suggestionss should contain "test". This test verifies that
        # the results include the keyword "test" """

        #Load the main page. In this case the home page of Mendel.webflow.io.
        main_page = page.MainPage(self.driver)

        #Sets the text of search textbox to "test"
        keyword = main_page.search_text_element = "covid"

        time.sleep(2)

        results = main_page.main_results()

        #Declar an array that holds all the result text
        all_results = []

        for ele in results:
            # print("Suggestions are:", main_page.main_resultText(ele))
            all_results.append(main_page.main_resultText(ele))
        
        #Verifies that the entered keyword is in the auto suggessted results
        self.assertIn(keyword, all_results, "The keyword is not in the auto suggested result(s)")

    def test_03_search_in_mendelai_mismatch_result_with_no_result_found(self):
        # """Tests mendel.webflow.io search feature. Searches for the word "bsssss" then
        # verified that some results show up.  Note any auto result suggestion dropdown should say no result found. This test verifies that
        # the results not found is displayed """

        #Load the main page. In this case the home page of Mendel.webflow.io.
        main_page = page.MainPage(self.driver)

        #Sets the text of search textbox to "test"
        keyword = main_page.search_text_element = "bsssss"

        time.sleep(2)

        results = main_page.no_results_found_text()
        
        #Verifies that the entered keyword is in the auto suggessted results
        self.assertNotIn(keyword, results, "The the keyword is in the result suggestions text")
        self.assertEqual("No results found", results, "The no result found should show up when there is not any matching result suggestions" )

    @classmethod 
    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(testRunner = HtmlTestRunner.HTMLTestRunner(output="/Users/cuicuiyuan/Documents/DemoMendelSearchAutomatedTests/Reports"))