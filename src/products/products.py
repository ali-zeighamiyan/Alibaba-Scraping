from turtle import title
from selenium.webdriver.common.by import By
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class product:
    def __init__(self):

        self.overview=[]
        self.prices_of_all_product=[]
        self.product_links=[]
        self.links=[]
        self.titles=[]
    
    def links_of_all_products(self,driver):

        self.product_links=(WebDriverWait(driver,5).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'elements-title-normal'))))
        # for links in self.product_links:
        #     self.links.append(links.get_attribute('href'))
        return self.product_links


    def get_prices(self,driver,source1):
        link=driver.current_url


        try:
            price=WebDriverWait(driver,20).until(EC.presence_of_element_located((By.ID,'buy-sample'))).find_element(By.CLASS_NAME,'sample-item').text

            self.prices_of_all_product=(price)

        except:
            try:
                #price=driver.find_element(By.CLASS_NAME,'price-item').text
                price=WebDriverWait(driver,1).until(EC.presence_of_element_located((By.CLASS_NAME,'price-item'))).text
                self.prices_of_all_product=(price)
            
            except:
                try:
                    soup1=BeautifulSoup(source1,"lxml")
                    container=soup1.find('div',id='container')
                    price=container.find('div',class_='promotion-price').text
                    self.prices_of_all_product=(price)
                except:
                    try:
                        price=WebDriverWait(driver,1).until(EC.presence_of_element_located((By.CLASS_NAME,'product-price'))).text
                        self.prices_of_all_product=(price)
                    except:
                        self.prices_of_all_product=('not found')
        return [self.prices_of_all_product,link]
    def get_overview(self,source1):
        
        detail_type_list=[]
        detail_list=[]
    

        soup1=BeautifulSoup(source1,"lxml")
        detail_types=soup1.findAll('span',class_='attr-name')
        
        detail=soup1.findAll('div',class_='text-ellipsis')
        
        for det_type,det in zip(detail_types,detail):
    

            detail_type_list.append(det_type.text)
            detail_list.append(det.text)
        
        

        new_dict = {detail_type_list[m]: detail_list[m] for m in range(len(detail_type_list))}
        # self.overview.append(new_dict)
        self.new_dict=new_dict

        title1=soup1.find('div',class_='product-title').find('h1').text
        return [new_dict,title1]


def price_normalizer(price):
########### normalize prices and convert to float
    price=price.replace(',','')
    for i2,p in enumerate(price):
        if p=="$":
            price1=price[i2+1:]
        
    for i3,p1 in enumerate(price1):
        if p1=="/":
            price1=price1[0:i3]

    
    if price1!='not found':
        price1=float(price1)
    return price1
        #############

def name_func_feature(overview,title):

    m=0
    for t1,type in enumerate(overview):
        if type=='Product name:':
            All_names=(overview['Product name:'])
            m=1
        
        elif type=='Product Name::':
            All_names=(overview['Product Name::'])
            m=1
        elif type=='Product Name:':
            All_names=(overview['Product Name:'])
            m=1
    if m==0:
        All_names=(title)


    
    n=0
    for t2,type2 in enumerate(overview):
        if type2=='Function:':
            All_funcs=(overview['Function:'])
            n=1
        
        elif type2=='Function::':
            All_funcs=(overview['Function::'])
            n=1

    if n==0:
        All_funcs=(None)
    ###############

    s=0
    for t3,type3 in enumerate(overview):
        if type3=='Feature:':
            All_feature=(overview['Feature:'])
            s=1
        
        elif type3=='Feature::':
            All_feature=(overview['Feature::'])
            s=1

    if s==0:
        All_feature=(None)
        
    return [All_names,All_funcs,All_feature]