import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class company:
    def __init__(self):
        country_of_company_list=[]
        company_name_list=[]
        company_link_list=[]
        establish_year=[]
        self.country_of_company_list=country_of_company_list
        self.company_name_list=company_name_list
        self.company_link_list=company_link_list
        self.establish_year=establish_year

    def get_company_details(self,driver,source1,overview):
        soup1=BeautifulSoup(source1,"lxml")
     
        company_name=soup1.find('div',class_='company-name-container')
        if company_name==None:
            company_name=soup1.find('div',class_='company-item')
        self.company_name_list=(company_name.text)
        c_link=company_name.find('a').get('href')

        self.company_link_list=(c_link)




        source2=requests.get(c_link)
        soup2=BeautifulSoup(source2.text,'lxml')
        year=soup2.find_all('td',class_='field-title')
        try:
            for y in year:
                if y.text=='Year Established':
                    break
            year_es=y.findNext('div',class_='content-value').text
            year_es=int(year_es)
            
        except:

            try:
                advertise=driver.find_element(By.CLASS_NAME,'gdpr-close')
                advertise.click()
            except:

                n=WebDriverWait(driver,0.5).until(EC.presence_of_all_elements_located((By.CLASS_NAME,'tab-name')))[1]
                n.click()
                m=WebDriverWait(driver,3).until(EC.presence_of_element_located((By.CLASS_NAME,'company-basicInfo')))
                for yi,y in enumerate(m.text.split()):
                    if y=='Established':
                        break
                year_es=(m.text).split()[yi+1]
                year_es=int(year_es)

        self.establish_year=(year_es)
            


        self.country_of_company_list=(overview['Place of Origin:'])

        return  [self.company_name_list,self.country_of_company_list,self.company_link_list,self.establish_year]
