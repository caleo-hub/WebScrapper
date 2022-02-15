from settings import *

class ScienceDirectSearch(unittest.TestCase):
    
    def setUp(self) -> None:
        ser = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=ser)
        self.driver.get('https://www.sciencedirect.com')
        self.driver.maximize_window()


    
    def test_get_SearchResults(self):
        main_page = page.MainPage(self.driver)
        main_page.search_text_element = "(software OR algorithm) development (control OR analysis) (computer OR engineering)"
        main_page.click_go_button()
        
        #Verifies that the results page is not empty
        search_results_page = page.SearchResultsPage(self.driver)
        assert search_results_page.is_results_found()

        papersData_ScienceDirect = papersData()
        search_results_page.page_options()
        pagesNumber = search_results_page.find_pages_numbers()

        for i in range(1,pagesNumber):
            search_results_page.find_result_list()
            pageResult = {'Title':search_results_page.get_papers_titles(),
                   'Link':search_results_page.get_papers_link(),
                   'ISSN':search_results_page.get_ISSN()
                }
            papersData_ScienceDirect.appendData(pageResult)
            print('Page:',i)
            search_results_page.click_next_page()


        assert papersData_ScienceDirect.saveCSV()


    def tearDown(self) -> None:
        self.driver.close()


class SucupiraSearch(unittest.TestCase):
    
    def setUp(self) -> None:
        self.papersData = papersData()
        self.papersData.openCSV()
        
    def test_getRank(self):
        detector = qualisDetector()
        ISSNList = self.papersData.ISSN
        detector.getJSON_list(ISSNList)
        mainRanks, _ = detector.getRank_list()
        self.papersData.mainRank = mainRanks
        assert self.papersData.saveCSV()

    def tearDown(self) -> None:
        pass

if __name__ == "__main__":
    unittest.main()