from scraper.scraper import Scraper
from utils.save_data import save_data
from utils.multi_threading import MultiThreading

from fake_useragent import UserAgent
import logging.config


def main():

    logging.config.fileConfig("logging.conf")
    logger = logging.getLogger("sLogger")

    ua = UserAgent()

    params = {
        "ae": "0",
        "oa": "1",
        "pt": "2",
        "vl": "3",
        "wg": "4",
        "pf": "5",
        "hi": "6",
        "wi": "7",
        "bp": "8",
        "pac": "9",
        "pas": "10",
        "sho": "11",
        "phy": "12",
        "dri": "13",
        "def": "14"
        }

    query = "&".join([f"showCol%5B{y}%5D={x}" for x, y in params.items()])
    url = f"https://sofifa.com/players?{query}&offset="
    urls = [url + str(offset) for offset in range(0, 18060, 60)]

    # Parameters
    number_of_scraper = 31
    pages = 10

    scrapers = [Scraper(urls[pages*i:min(pages*(i+1), len(urls))], ua.random) for i in range(number_of_scraper)]

    logger.info("Scraping started...")
    multi_threading = MultiThreading(scrapers)
    multi_threading.run()
    logger.info("Scraping finished.")

    logger.info("Generating CSV file...")
    save_data(Scraper.players_scraped)
    logger.info("CSV File is generated.")


if __name__ == '__main__':
    main()    
