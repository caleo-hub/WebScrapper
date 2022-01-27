from element import BasePageElement
from selenium.webdriver.support.ui import WebDriverWait
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
        
        return "Science" in self.driver.title

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

    def get_papers_titles(self):
        search_result_list= PageElementObject(self.driver).getElement(SearchResultPageLocators.SEARCH_RESULTS_LIST)
        papers_titles = search_result_list.find_elements(By.TAG_NAME,'h2')
        self.papers_titles_text = []
        for element in papers_titles:
            self.papers_titles_text.append(element.text)
        return self.papers_titles_text
    
    def get_papers_link(self):
        search_result_list= PageElementObject(self.driver).getElement(SearchResultPageLocators.SEARCH_RESULTS_LIST)
        papers_titles = search_result_list.find_elements(By.TAG_NAME,'h2')
        self.papers_link_text = []
        for i,element in enumerate(papers_titles) :
            title = self.papers_titles_text[i]
            self.papers_link_text.append(element.find_element(By.LINK_TEXT, title))
        return self.papers_link_text 



