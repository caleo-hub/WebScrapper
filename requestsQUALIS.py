import asyncio
import aiohttp
from locators import *  
from functools import wraps
from asyncio.proactor_events import _ProactorBasePipeTransport




class qualisDetector(object):

    def silence_event_loop_closed(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            try:
                return func(self, *args, **kwargs)
            except RuntimeError as e:
                if str(e) != 'Event loop is closed':
                    raise
        return wrapper
    _ProactorBasePipeTransport.__del__ = silence_event_loop_closed(_ProactorBasePipeTransport.__del__)


    async def get(self,session: aiohttp.ClientSession,ISSN: str,**kwargs) -> dict:
        url = f'https://qualisapi.herokuapp.com/api/qualis/v1/issn/{ISSN}'
        resp = await session.request('GET', url=url, **kwargs)
        self.JSON = await resp.json()
        return self.JSON
    
    async def getJSON_list(self,ISSNList, **kwargs):
        async with aiohttp.ClientSession() as session:
            self._rankList = []
            for ISSN in ISSNList:
                self._rankList.append(self.get(session=session, ISSN=ISSN, **kwargs))

            self.JSONList = await asyncio.gather(*self._rankList)

        return self.JSONList

    def getRank_list(self):
         
        mainRanks = []
        otherRanks = []
        for JSON in self.JSONList:
            rankData = JSON['data']
            mainAreas = list(filter(lambda y: y['area'] in API_Locators.AREAS['main'], rankData))
            otherAreas = list(filter(lambda y: y['area'] not in API_Locators.AREAS['main'], rankData))

            mainRanks.append(" ".join(map(lambda y: y['area'] + ' - ' +  y['estrato'], mainAreas)))
            otherRanks.append(" ".join(map(lambda y: y['area'] + ' - ' +  y['estrato'], otherAreas)))
        return mainRanks, otherRanks












