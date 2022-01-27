from selenium.webdriver.common.by import By

class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""

    SEARCH_BAR = (By.ID,'qs-searchbox-input')
    GO_BUTTON = (By.XPATH, '//*[@id="aa-srp-search-submit-button"]/button')
    
    # GO_BUTTON = (By.XPATH, '/html/body/div[1]/div/div/div[2]/div[1]/div/div/div/div/div/form/div/div[1]/div/div[6]/div[2]/button')

class SearchResultPageLocators(object):

    SEARCH_RESULTS_LIST = (By.ID,'srp-results-list')
