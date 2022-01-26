import os
import pandas as pd
from urllib3 import Retry

class papersData(object):

    def __init__(self) -> None:
        dirName = 'data'
        try:
            os.makedirs('data')
            print("Directory " , dirName ,  " Created ")
        except FileExistsError:
            print("Saving in " , dirName ) 

        self.papersDataFrame = pd.DataFrame(columns=['Title'])
    
    
    @property
    def titles(self):
        return self.papersDataFrame['Title']
    
    @titles.setter
    def titles(self, titlesList):
        self.papersDataFrame['Title'] = titlesList
    
    def saveCSV(self):
        try:
            self.papersDataFrame.to_csv('data/papersData.csv')
            return True
        except:
            return False
