import unittest
from unittest.main import main
from selenium import webdriver
import page

class ScienceDirectSearch(unittest.TestCase):
    

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.sciencedirect.com')
    
    def test_search_in_page(self):

        #Load the main page.
        main_page = page.MainPage(self.driver)
        assert main_page.is_title_matches()

        #Sets the text of search textbox
        main_page.search_text_element = "qa/qc software"
        main_page.click_go_button()

        search_results_page = page.SearchResultsPage(self.driver)
        #Verifies that the results page is not empty

        assert search_results_page.is_results_found()


    def tearDown(self) -> None:
        self.driver.close()

if __name__ == "__main__":
    unittest.main()