import unittest
from unittest.main import main
from selenium import webdriver
from selenium.webdriver.common.by import By
import page
from papersData import papersData
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



class ScienceDirectSearch(unittest.TestCase):
    

    def setUp(self) -> None:
        ser = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=ser)
        self.driver.get('https://www.sciencedirect.com')
    
    # def test_search_in_page(self):
    #     #Load the main page.
    #     main_page = page.MainPage(self.driver)
    #     assert main_page.is_title_matches()

    #     #Sets the text of search textbox
    #     main_page.search_text_element = "qa/qc software"
    #     main_page.click_go_button()

        


    def test_get_SearchResults(self):

        main_page = page.MainPage(self.driver)
        main_page.search_text_element = "qa/qc software"
        main_page.click_go_button()
        
        #Verifies that the results page is not empty
        search_results_page = page.SearchResultsPage(self.driver)
        assert search_results_page.is_results_found()

        papersData_ScienceDirect = papersData()
        papersData_ScienceDirect.titles = search_results_page.get_articles_titles()
        assert papersData_ScienceDirect.saveCSV()





    def tearDown(self) -> None:
        self.driver.close()

if __name__ == "__main__":
    unittest.main()