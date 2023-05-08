from selenium import webdriver
from fake_useragent import UserAgent
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import requests
from bs4 import BeautifulSoup


#Class Structure for Card Page
class Item:
    def __init__(self, itemID) -> None:
        #Options
        options = webdriver.ChromeOptions()
        # options.add_argument("--headless")
        
        #User Agents
        ua = UserAgent()
        userAgent = ua.random
        options.add_argument(f'user-agent={userAgent}')
        
        #Item ID + URL
        self.itemID = itemID
        self.site = f"https://www.tcgplayer.com/product/{itemID}"
        print(self.site)

        #Start Driver Load Page
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        driver.get(self.site)
        # time.sleep(2)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'product-details__name')))

        #HTML Parse
        html = driver.page_source
        self.soup = BeautifulSoup(html, "html.parser")

    def getMarketPrice(self) -> int:
        marketprice = self.soup.find("div", {"class": "charts-price"}).text
        try:
            return float(marketprice[1:]) #not change friendly
        except:
            return None
        #TODO Make exception cases for things that have no market price
    
    def getItemName(self):
        itemName = self.soup.title
        return (itemName.string)
    
start_time = time.time()
test = Item(123456)
print("--- %s seconds ---" % (time.time() - start_time))

    
        




