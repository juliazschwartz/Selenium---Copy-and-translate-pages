import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import urllib.request as urllib2
from bs4 import *
from urllib.parse  import urljoin
import requests as requests;
import cloudscraper

# webpage = requests.get('https://www.classcentral.com');
# result = webpage.text;
# print(result);

# browser = webdriver.Chrome()

# browser.get("https://medium.com/top-100/december-2013")
# time.sleep(1)

# elem = browser.find_element(By.NAME, "body")

# no_of_pagedowns = 20

# while no_of_pagedowns:
#     elem.send_keys(Keys.PAGE_DOWN)
#     time.sleep(0.2)
#     no_of_pagedowns-=1

# post_elems = browser.find_elements_by_class_name("post-item-title")

# for post in post_elems:
#     print (post.text)

def crawl(page, depth=None):
    indexed_url = [] # a list for the main and sub-HTML websites in the main website
    for i in range(depth):
        # for page in pages:
            if page not in indexed_url:
                indexed_url.append(page)
                try:
                    headers = { 'User-Agent': 'Mozilla/5.0' }
                    # browser = webdriver.Chrome()

                    # browser.get(page)
                    # time.sleep(1)

                    # elem = browser.find_element(By.NAME, "body")

                    # no_of_pagedowns = 20

                    # while no_of_pagedowns:
                    #     elem.send_keys(Keys.PAGE_DOWN)
                    #     time.sleep(0.2)
                    #     no_of_pagedowns-=1
                    #     post_elems = browser.find_element(By.NAME,"img")

                    #     for post in post_elems:
                    #         print (post.text)
                   
                    scraper = cloudscraper.create_scraper() 
                    c = scraper.get(page).text
                except:
                    print( "Could not open %s" % page)
                    continue
                soup = BeautifulSoup(c, 'html.parser')
                # print(soup)
                # file = open("D:\Julia\demofile2.txt", "a")
                # file.write(c)
                # file.close()

                print(soup)
    #             soup = BeautifulSoup(soup.read())
    #             links = soup.find_all('a') #finding all the sub_links
    #             # print(links)
    #             for link in links:
    #                 if 'href' in dict(link.attrs):
    #                     url = urljoin(page, link['href'])
    #                     if url.find("'") != -1:
    #                             continue
    #                     url = url.split('#')[0] 
    #                     if url[0:4] == 'http':
    #                             indexed_url.append(url)
    #     # pages = indexed_url
    # print(indexed_url)
  
    return indexed_url


pagelist="https://www.classcentral.com/";
# # pagelist="https://stackoverflow.com/questions/52725892/how-to-resolve-requests-get-not-working-over-vpn/";
urls = crawl(pagelist, depth=1)


