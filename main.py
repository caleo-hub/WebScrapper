from settings import *


class ScienceDirectSearch():
    
    def setUp(self) -> None:
        ser = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=ser)
        self.driver.get('https://www.sciencedirect.com')
        self.papersData_ScienceDirect = papersData()
    
    def getSearchResults(self):

        try:
            if os.stat('search_text.txt').st_size > 0:
                with open('search_text.txt') as f:
                    search_text = f.readline()
            else:
                raise NameError('Empty search_text.txt')
        except OSError:
            print ('search_text.txt not found')
        

        main_page = page.MainPage(self.driver)
        main_page.search_text_element = search_text
        main_page.click_go_button()
        
        #Verifies that the results page is not empty
        search_results_page = page.SearchResultsPage(self.driver)
        search_results_page.page_options()
        pagesNumber = search_results_page.find_pages_numbers()

        print('Results is found:',search_results_page.is_results_found()) 

        for i in range(pagesNumber):
            print('Page:',i+1)
            search_results_page.find_result_list()
            pageResult = {'Title':search_results_page.get_papers_titles(),
                   'Link':search_results_page.get_papers_link(),
                   'ISSN':search_results_page.get_ISSN()
                }
            self.papersData_ScienceDirect.appendData(pageResult)
            search_results_page.click_next_page()

        print('CSV Saved:',self.papersData_ScienceDirect.saveCSV()) 

    def getRank(self):
        detector = qualisDetector()
        ISSNList = self.papersData_ScienceDirect.ISSN
        asyncio.run(detector.getJSON_list(ISSNList))
        mainRanks, _ = detector.getRank_list()
        self.papersData_ScienceDirect.mainRank = mainRanks
        print('CSV Saved:',self.papersData_ScienceDirect.saveCSV()) 


    def tearDown(self) -> None:
        self.driver.close()
    
def main():
    SC_Search = ScienceDirectSearch()
    SC_Search.setUp()
    SC_Search.getSearchResults()
    SC_Search.getRank()
    SC_Search.tearDown()
    print('Search Finished')



if __name__ == "__main__":
    main()