import os
import pandas as pd
from urllib3 import Retry

class papersData(object):

    def __init__(self) -> None:
        self.dirName = 'data'
        try:
            os.makedirs('data')
            print("Directory" , self.dirName ,  "Created ")
        except FileExistsError:
            print("Accessing" , self.dirName )

        columns = ['Title','Link']
        self.papersDataFrame = pd.DataFrame(columns=columns)
    
    
    @property
    def titles(self):
        return self.papersDataFrame['Title']

    @property
    def links(self):
        return self.papersDataFrame['Link']
    
    @titles.setter
    def titles(self, titlesList):
        self.papersDataFrame['Title'] = titlesList

    @links.setter
    def links(self, linksList):
        self.papersDataFrame['Link'] = linksList
        


    
    def saveCSV(self):
        try:
            self.papersDataFrame.to_csv('data/papersData.csv')
            print("Saving in" , self.dirName )
            return True
        except:
            return False
