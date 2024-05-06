#Run this script to translate the generated pages
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import googletrans
from googletrans import Translator

translator = Translator(service_urls=['translate.googleapis.com'])
browser = webdriver.Chrome()
browser.get("https://www.classcentral.com/report/category/best-courses/")
time.sleep(1)

elem = browser.find_element(By.TAG_NAME, "body")
no_of_pagedowns = 20

while no_of_pagedowns:
        elem.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.2)
        no_of_pagedowns-=1
      
replacements = {}
tags = ["h1", "h2", "h3", "h4", "h5", "h6", "h7", "h8", "p", "span", "li", "label", "small", "a", "i"]
   

for tag in tags :
    elem = browser.find_elements(By.TAG_NAME, tag)
    for e in elem :
        if (e.text != ""):
         chave = e.text
         traducao = translator.translate(e.text, dest="hi").text
         replacements[chave] = traducao
         
        
html = browser.page_source
time.sleep(1)
file = open("bt-test.html", "w", encoding="utf-8")
file.write(html)
file.close()


browser.close()


with open('bt-test.html') as infile, open('bt-test3.html', 'w',encoding="utf-8")  as outfile:
    for line in infile:
        for src, target in replacements.items():
            line = line.replace(src, target)
        outfile.write(line)
