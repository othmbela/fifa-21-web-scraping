from scraper_utils import extract_info

from bs4 import BeautifulSoup
import requests
import time
import random
import logging


class Scraper(object):
    """
    Extract players information.
    """

    players_scraped = []
    
    def __init__(self, urls, user_agent):
        self.urls = urls
        self.headers = {'UserAgent': user_agent}
        self.logger = logging.getLogger("sLogger")
        
    def get_page(self, url, headers):
        response = requests.get(url, headers=headers)
        if response.status_code:
            soup = BeautifulSoup(response.content, features="html.parser")
            return soup.find('tbody', {'class': 'list'})
        else:
            self.logger.error('Error ' + response.status_code)
            return None
        
    def get_players(self, trs):
        return [extract_info(tr) for tr in trs]

    def scrap(self, urls, headers):
        for url in urls:
            tbody = self.get_page(url, headers)
            if tbody is None:
                continue
            trs = tbody.findAll('tr')
            Scraper.players_scraped.append(self.get_players(trs))
            self.logger.info('Page {} scraped'.format(len(Scraper.players_scraped)))
            time.sleep(random.randint(3, 8))
        
    def start(self):
        self.scrap(self.urls, self.headers)