import os
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
        dirName = 'data'

        try:
            os.makedirs('data')
            print("Directory " , dirName ,  " Created ") 
        except FileExistsError:
            print("Saving in " , dirName ) 
        
        self.papersDataFrame.to_csv('data/papersData.csv')
