import os
import pandas as pd

class papersData(object):

    def __init__(self) -> None:
        self.dirName = 'data'
        try:
            os.makedirs('data')
            print("Directory" , self.dirName ,  "Created ")
        except FileExistsError:
            print("Accessing" , self.dirName )

        columns = ['Title','Link','ISSN']
        self.papersDataFrame = pd.DataFrame(columns=columns)

    
    @property
    def titles(self):
        return self.papersDataFrame['Title']

    
    @titles.setter
    def titles(self, titlesList):
        self.papersDataFrame['Title'] = titlesList


    @property
    def links(self):
        return self.papersDataFrame['Link']

    @links.setter
    def links(self, linksList):
        self.papersDataFrame['Link'] = linksList

    @property
    def ISSN(self):
        return self.papersDataFrame['ISSN']
    
    @ISSN.setter
    def ISSN(self,ISSN_List):
        self.papersDataFrame['ISSN'] = ISSN_List

    @property
    def mainRank(self):
        return self.papersDataFrame['Main Rank']

    @mainRank.setter
    def mainRank(self,mainRankList):
        self.papersDataFrame['Main Rank'] = mainRankList
        

    def appendData(self,data):
        self.papersDataFrame = pd.concat([self.papersDataFrame, pd.DataFrame(data)], ignore_index = True, axis = 0)
    

    
    def saveCSV(self):
        try:
            self.papersDataFrame.to_csv('data/papersData.csv')
            print("Saving in" , self.dirName )
            return True
        except:
            print("Saving Failed")
            return False

    def openCSV(self):
        self.papersDataFrame = pd.read_csv('data/papersData.csv',index_col=0)