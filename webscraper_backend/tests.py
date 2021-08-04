from os import getcwd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
import numpy as np
from proxies import ReturnProxy
from bots.aliexpress import AliexpressMain
from bots.amazon import AmazonMain
from bots.ebay import EbayMain
from bots.news import NewsMain
from bots.pubmed import PubmedMain
from database.excel import ExcelMain
from database.mongodb import MongodbMain
from database.postgresql import PostgreSQLMain
import unittest

class TestProxy(unittest.TestCase):
    
    # def test_proxy(self):
    #     """\033[1;92m Proxy function return test \033[0;0m"""
    #     self.assertEqual(ReturnProxy(), "Esta é uma proxy")
    pass

class TestBots(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.binary_location = 'C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe'
        options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
        self.driver = webdriver.Chrome(executable_path=f"{getcwd() + '/chromedriver.exe'}", options=options)
    
    # def test_aliexpress(self):
    #     """\033[1;92m Aliexpress function return test \033[0;0m"""
    #     self.assertEqual(AliexpressMain(), "Aliexpress testcase")
    
    # def test_amazon(self):
    #     """\033[1;92m Amazon function return test\033[0;0m"""
    #     self.assertEqual(AmazonMain(), "Amazon testcase")
    
    # def test_ebay(self):
    #     """\033[1;92m Ebay function return test\033[0;0m"""
    #     self.assertEqual(EbayMain(), "Ebay testcase")
    
    # def test_pubmed(self):
    #     """\033[1;92m Pubmed function return test\033[0;0m"""
    #     self.driver.get("https://pubmed.ncbi.nlm.nih.gov/")
    #     self.assertEqual(self.driver.current_url, "https://pubmed.ncbi.nlm.nih.gov/")
    
    def test_news(self):
        """\033[1;92m News function return test\033[0;0m"""
        topic = "bacon"
        test = NewsMain(driver=self.driver, topic=topic)
        type_test = pd.DataFrame()
        self.assertEqual(type(test), type(type_test))
    
    def tearDown(self):
        self.driver.quit()

class TestDatabases(unittest.TestCase):
    
    # def test_excel(self):
    #     """\033[1;92m Excel function CRUD test\033[0;0m"""
    #     self.assertEqual(ExcelMain(), "Excel testcase")
    
    # def test_mongodb(self):
    #     """\033[1;92m Mongodb function CRUD test\033[0;0m"""
    #     self.assertEqual(MongodbMain(), "Mongodb testcase")
    
    # def test_postgresql(self):
    #     """\033[1;92m PostgreSQL function CRUD test\033[0;0m"""
    #     self.assertEqual(PostgreSQLMain(), "PostgreSQL testcase")
    pass
    

if __name__ == '__main__':
    unittest.main()
