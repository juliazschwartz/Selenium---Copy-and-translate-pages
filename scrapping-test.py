#This script is the first step. Its to find all the urls from the main pages and sublinks of the company website
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
browser = webdriver.Chrome()
browser.get("https://www.classcentral.com")
time.sleep(1)




# finding the SUBLINKS
indexed_url = [] 
links = browser.find_elements(By.TAG_NAME,'a') #finding all the sub_links

for link in links:
                    
                        url = link.get_attribute("href")
                        if url.find("'") != -1:
                                continue
                        url = url.split('#')[0] 
                        if url[0:4] == 'http':
                                indexed_url.append(url)


for url in indexed_url:     
    if(url.split("/")[2] == "www.classcentral.com") :
        if(len(url.split("/")) > 4) :
            name =  url.split("/")[4]
        else :
            name =  url.split("/")[3]
    
        if(name == "") :
            name = "index"
        
   
    # print(name)
    browser.get(url)
    time.sleep(1)
    indexed_url = [] # 

    elem = browser.find_element(By.TAG_NAME, "body")

    no_of_pagedowns = 20

    while no_of_pagedowns:
        elem.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.2)
        no_of_pagedowns-=1
      

    html = browser.page_source
    time.sleep(2)
    file = open(name + ".html", "w", encoding="utf-8")
    file.write(html)
    file.close()
    
    


browser.close()
