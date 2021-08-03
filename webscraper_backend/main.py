from proxies import ReturnProxy
from bots.aliexpress import AliexpressMain
from bots import aliexpress, amazon, ebay, pubmed
from database import excel, mongodb, postgresql

def RunWebscraper():
    """Main function, get the user inputs, import the bots for scraping and conect with the databases"""
    PROXY = ReturnProxy
    al = AliexpressMain
    am = amazon.AmazonMain
    eb = ebay.EbayMain
    pb = pubmed.PubmedMain
    exc = excel.ExcelMain
    mdb = mongodb.MongodbMain
    psql = postgresql.PostgreSQLMain
    print(PROXY())

def GetDriver():
    """Return the driver with the ajusted parameters"""
    pass

if __name__ == '__main__':
    RunWebscraper()