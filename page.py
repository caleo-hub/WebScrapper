from element import BasePageElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium import webdriver


from locators import *

class SearchTextElement(BasePageElement):
    locator = MainPageLocators.SEARCH_BAR



class BasePage(object):
    def __init__(self, driver) -> None:
        self.driver = driver

class MainPage(BasePage):

    #Declares a variable that will contain the retrieved text
    search_text_element = SearchTextElement()

    def is_title_matches(self):
        
        return "Sucupira" in self.driver.title

    def click_go_button(self):
        """Triggers the search"""
        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        element.click()


class PageElementObject(BasePage):

    def getElement(self,locator) -> None:
         WebDriverWait(self.driver,100).until(
             lambda driver:driver.find_element(*locator))
         pageElement = self.driver.find_element(*locator)
         return pageElement


class SearchResultsPage(BasePage):
    """Search results page action methods come here"""

    def is_results_found(self):
        # Probably should search for this text in the specific page
        # element, but as for now it works fine
        return "No results found." not in self.driver.page_source

    def find_result_list(self):
        self._searchResultList= PageElementObject(self.driver).getElement(SearchResultPageLocators.SEARCH_RESULTS_LIST)
        self._searchResultWrapper = self._searchResultList.find_element(By.TAG_NAME,'ol')
        self._allList_items = self._searchResultWrapper.find_elements(By.TAG_NAME,'li')

    def get_papers_titles(self):

        self.papers_titles_text = []
        for item in self._allList_items:
            className = item.get_attribute('class')
            PAPER_ITEM_CLASS=  'ResultItem col-xs-24 push-m'

            if className == PAPER_ITEM_CLASS:
                papers_title = item.find_element(By.TAG_NAME,'h2')
                self.papers_titles_text.append(papers_title.text)

        return self.papers_titles_text
    
    def get_papers_link(self):

        self.papers_doi = []
        for paper in self._allList_items:
            doi = paper.get_attribute('data-doi')
            if doi != None:
                self.papers_doi.append(DOI_Locators.DOI_Link +  doi)
        return self.papers_doi

    def get_ISSN(self):
        self.papers_ISSN = []
        for item in self._allList_items:
            className = item.get_attribute('class')
            PAPER_ITEM_CLASS=  'ResultItem col-xs-24 push-m'

            if className == PAPER_ITEM_CLASS:
                link_tag = item.find_element(By.CLASS_NAME,'subtype-srctitle-link')
                papers_periodicURL = link_tag.get_attribute('href')
                lastURL_Item = papers_periodicURL.split('/')[-1]
                ISNN = lastURL_Item[0:4]+'-'+ lastURL_Item[4:8]
                self.papers_ISSN.append(ISNN)

        return self.papers_ISSN

    def find_pages_numbers(self):
        pagination= PageElementObject(self.driver).getElement(SearchResultPageLocators.PAGINATION)
        PaginationLists = pagination.find_elements(By.TAG_NAME,'li')
        for element in PaginationLists:
            if element.get_attribute('class') == '':
                return int(element.text.split()[-1])

    def click_next_page(self):
        pagination = self.driver.find_element(*SearchResultPageLocators.PAGINATION)
        next_button = pagination.find_element(By.LINK_TEXT,'next').get_attribute('href')
        self.driver.get(next_button)

    def page_options(self):
        paginationOptions= PageElementObject(self.driver).getElement(SearchResultPageLocators.PAGINATION_OPTIONS)
        paginationOptions.find_element(By.LINK_TEXT,'100').click()

        



class SucupiraSearchPage(BasePage):
    def is_title_matches(self):
        return "Sucupira" in self.driver.title

 



