# Functions of the webscraper
from proxies import ReturnProxy
from bots.aliexpress import AliexpressMain
from bots.amazon import AmazonMain
from bots.ebay import EbayMain
from bots.pubmed import PubmedMain
from database.excel import ExcelMain
from database.mongodb import MongodbMain
from database.postgresql import PostgreSQLMain

# third party modules
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from os import getcwd
import time


def RunWebscraper():
    """Main function, get the user inputs, import the bots for scraping and conect with the databases"""
    driver = GetDriver()
    driver.get("https://pubmed.ncbi.nlm.nih.gov/")
    print(driver.current_url)
    time.sleep(5)
    driver.quit()

def GetDriver(**kwargs):
    """Return a selenium webdriver instance, used to control the browser"""
    options = Options()
    options.binary_location = 'C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe'
    options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
    driver = webdriver.Chrome(executable_path=f"{getcwd()}\chromedriver.exe", options=options)
    return driver

if __name__ == '__main__':
    RunWebscraper()