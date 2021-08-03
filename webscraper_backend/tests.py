import selenium
import pandas as pd
import numpy as np
from proxies import ReturnProxy
from bots.aliexpress import AliexpressMain
from bots.amazon import AmazonMain
from bots.ebay import EbayMain
from bots.pubmed import PubmedMain
from database.excel import ExcelMain
from database.mongodb import MongodbMain
from database.postgresql import PostgreSQLMain
import unittest

class TestProxy(unittest.TestCase):
    
    def test_proxy(self):
        """\033[1;92m Proxy function return test \033[0;0m"""
        self.assertEqual(ReturnProxy(), "Esta é uma proxy")

class TestBots(unittest.TestCase):
    
    def test_aliexpress(self):
        """\033[1;92m Aliexpress function return test \033[0;0m"""
        self.assertEqual(AliexpressMain(), "Aliexpress testcase")
    
    def test_amazon(self):
        """\033[1;92m Amazon function return test\033[0;0m"""
        self.assertEqual(AmazonMain(), "Amazon testcase")
    
    def test_ebay(self):
        """\033[1;92m Ebay function return test\033[0;0m"""
        self.assertEqual(EbayMain(), "Ebay testcase")
    
    def test_pubmed(self):
        """\033[1;92m Pubmed function return test\033[0;0m"""
        self.assertEqual(PubmedMain(), "PubmedMain testcase")

class TestDatabases(unittest.TestCase):
    
    def test_excel(self):
        """\033[1;92m Excel function CRUD test\033[0;0m"""
        self.assertEqual(ExcelMain(), "Excel testcase")
    
    def test_mongodb(self):
        """\033[1;92m Mongodb function CRUD test\033[0;0m"""
        self.assertEqual(MongodbMain(), "Mongodb testcase")
    
    def test_postgresql(self):
        """\033[1;92m PostgreSQL function CRUD test\033[0;0m"""
        self.assertEqual(PostgreSQLMain(), "PostgreSQL testcase")
    

if __name__ == '__main__':
    unittest.main()
