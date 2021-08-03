# from .bots import amazon, aliexpress, ebay, pubmed
# from .database import excel, mongodb, postgresql

def RunWebscraper():
    """Main function, get the user inputs, import the bots for scraping and conect with the databases"""
    bot = str(input("Website to scrape: "))
    print(bot)

if __name__ == '__main__':
    print(RunWebscraper.__doc__)