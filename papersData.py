from operator import index
import pandas as pd

class papersData(object):

    def __init__(self) -> None:
        self.papersDataFrame = pd.DataFrame(columns=['Title'])
    
    
    @property
    def titles(self):
        return self.papersDataFrame['Title']
    
    @titles.setter
    def titles(self, titlesList):
        self.papersDataFrame['Title'] = titlesList

    def saveCSV(self):
        self.papersDataFrame.to_csv('\data')

