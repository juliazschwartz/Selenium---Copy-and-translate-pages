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
        

    
#         if (len(url.split("/")) > 2):
         
#          if(url.split("/")[2] == "www.classcentral.com") :
#             if(len(url.split("/")) > 4) :
#                 name =  url.split("/")[4]
#             else :
#                 name =  url.split("/")[3]
    
#             if(name == "") :
#                  name = "index"
#             url = "/"+ name
#             my_dictionary[url] = "/" + name + ".html"   
# print(my_dictionary)
            
# with open('coursera-teste.html',  encoding="cp437") as infile, open('chemical-engineering.html', 'w',  encoding="cp437") as outfile:
#     for line in infile:
#         for src, target in my_dictionary.items():
#                  line = line.replace(src, target)
#         outfile.write(line)