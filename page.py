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

    def get_articles_titles(self):
        search_result_list= PageElementObject(self.driver).getElement(SearchResultPageLocators.SEARCH_RESULTS_LIST)
        print(search_result_list)
        papers_titles = search_result_list.find_elements(By.TAG_NAME,'h2')
        papers_titles_text = []
        for element in papers_titles:
            papers_titles_text.append(element.text)
        return papers_titles_text
