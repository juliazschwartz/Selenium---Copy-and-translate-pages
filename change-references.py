#here it will change some link references
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import googletrans
from googletrans import Translator
from bs4 import BeautifulSoup
from bs4.formatter import HTMLFormatter
from googletrans import Translator
import requests



browser = webdriver.Chrome()
browser.get("https://www.classcentral.com/")



my_dictionary = {}
list = []
tag = "a"
elem = browser.find_elements(By.TAG_NAME, tag)
for e in elem :
        url = e.get_attribute("href") 
        if url not in list :
                
                if (len(url.split("/")) > 2):
                    if(url.split("/")[2] == "www.classcentral.com") :
                      list.append(url)
                      print(url)
        

