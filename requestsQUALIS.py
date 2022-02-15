import requests
import os
from locators import *



class qualisDetector(object):
    def getJSON_list(self,ISSNList):
        API = API_Locators.API
        self._rankList = []
        for i,ISSN in enumerate(ISSNList):
            url = API + ISSN
            r = requests.get(url)
            print(i,'of', len(ISSNList))
            self._rankList.append(r.json()['data'])
    
        return self._rankList

    def getRank_list(self): 
        mainRanks = []
        otherRanks = []
        for rank in self._rankList:
            mainAreas = list(filter(lambda y: y['area'] in API_Locators.AREAS['main'], rank))
            otherAreas = list(filter(lambda y: y['area'] not in API_Locators.AREAS['main'], rank))

            mainRanks.append(" ".join(map(lambda y: y['area'] + ' - ' +  y['estrato'], mainAreas)))
            otherRanks.append(" ".join(map(lambda y: y['area'] + ' - ' +  y['estrato'], otherAreas)))
        return mainRanks, otherRanks












