import requests
from src.company import company
from src.products import products
# from company import company
# from products import products
from bs4 import BeautifulSoup
from selenium import webdriver
import lxml
import html5lib
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lxml import html
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pymongo
from pymongo import MongoClient
import dns


class alibab:
    def __init__(self):
        c=company.company()
        p=products.product()
        self.c=c
        self.p=p
        self.links_of_all_product=[]
        self.title_of_all_product=[]
        self.page_links=[]
        os.environ['PATH']="C:/Users/abc/Desktop/sel driver"


    def run(self,links):
        driver=webdriver.Chrome()
        driver.get(links)
        return driver

    def run_driver(self,driver):
        
        # driver=webdriver.Chrome()
        # self.driver=driver
        # self.driver.get(url)
        
        self.links_of_all_product=self.p.links_of_all_products(driver)
        return self.links_of_all_product
        # print(self.links_of_all_product)
        # return driver


    
    def get(self,driver):

        source1=driver.page_source
        
        prices=self.p.get_prices(driver,source1)[0]
        link=self.p.get_prices(driver,source1)[1]
        
        [overview,title]=self.p.get_overview(source1)
        company_detail=self.c.get_company_details(driver,source1,overview)
        normal_prices=products.price_normalizer(prices)
        name_func_feature=products.name_func_feature(overview,title)


        return [normal_prices,overview,name_func_feature,link,company_detail]

    def get_name_of_search(self,search_text):
        for i in range(2):
            self.page_links.append(f'https://www.alibaba.com/trade/search?SearchText={search_text}&page={i+1}&f0=y')
        return self.page_links

        
    
def save_todb(result,i):
    cluster = MongoClient("mongodb+srv://ali3515:35154174@cluster0.h3tum.mongodb.net/?retryWrites=true&w=majority")
    db=cluster["alibaba"]
    collection=db['products']

    if (collection.count_documents({})!=0 and i==0):
        collection.delete_many({})
    dict1={"_id":i,"Name":result[2][0],"Function":result[2][1],"Feature":result[2][2],"Country":result[4][1],"Link":result[3],"Price":result[0],"Overview":result[1]}
    collection.insert_one(dict1)
    
    collection2=db['company']
    if (collection2.count_documents({})!=0 and i==0):
        collection2.delete_many({})
    

    dict2={"id":i,"Name":result[4][0],"Link":result[4][2],"Country":result[4][1],"Established Year":result[4][3]}
    collection2.insert_one(dict2)



# c1=alibab()
# c1.run_driver(search_text)

# a=c1.run()
# print(a)
# save_todb(a)



