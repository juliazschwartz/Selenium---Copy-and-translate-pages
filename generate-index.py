# import modules
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import googletrans
from googletrans import Translator
import pyautogui
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--lang=hi')  # set your language 

browser = webdriver.Chrome(options=options)
browser.set_window_size(1600, 800)
browser.get("http://classcentral.com/help")



header = browser.find_element(By.TAG_NAME, "header")
button = header.find_element(By.CSS_SELECTOR, "button[data-name='LARGE_UP_MAIN_NAV_TRIGGER']")
input = browser.find_element(By.CSS_SELECTOR, "input[data-name='AUTOCOMPLETE_SEARCHBOX']")
    # follow = browser.find_element(By.CSS_SELECTOR, "button[data-name='FOLLOW']") # SO PROS SUBJECTS
    # image = browser.find_element(By.ID, "learning-illus")
div = header.find_element(By.CLASS_NAME, "symbol-report")
elem = browser.find_element(By.TAG_NAME, "body")

# image = browser.find_element(By.ID, "learning-illus")
div = header.find_element(By.CLASS_NAME, "symbol-report")
elem = browser.find_element(By.TAG_NAME, "body")



actionChains = ActionChains(browser)
actionChains.context_click(on_element=header).perform()


for i in range(3):
    pyautogui.sleep(1)
    pyautogui.press('up')

pyautogui.press('enter')

# time.sleep(4) 
# actionChains.move_to_element(sanduiche).perform()
# time.sleep(2) 
# actionChains.move_to_element(rankings).perform()
# time.sleep(2) 
# actionChains.move_to_element(year).perform()
# time.sleep(2) 
# actionChains.move_to_element(providers).perform()
time.sleep(2) 
pyautogui.moveTo(300, 210) 
for i in range(20):
    pyautogui.move(0,30)
    pyautogui.sleep(2)
time.sleep(1)
pyautogui.moveTo(402, 210) 
pyautogui.sleep(2)
pyautogui.moveTo(500, 210) 
actionChains.click(input).perform()
actionChains.click(header).perform()

time.sleep(2) 

no_of_pagedowns = 60
while no_of_pagedowns:
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.2)
    no_of_pagedowns-=1

#get the html source code
html = browser.page_source
time.sleep(2)
#create the archive (important NOT to be utf-8 encoded)
file = open("help" + ".html", "a", encoding="utf-8" )
file.write("<!DOCTYPE html>")
file.write(html)
file.close()


# browser.close()
# # translates to hindi
# translator = Translator(service_urls=['translate.googleapis.com'])
# replacements = {} #dictionary for the translation
# tags = ["h1", "h2", "h3", "h4", "h5", "h6", "h7", "h8", "p", "span", "li", "label", "small", "a", "i", "strong", "title", "button", "font", "div"] #tags that contains text to be translated
# for tag in tags :
#     elem = browser.find_elements(By.TAG_NAME, tag)
#     for e in elem :
#         if (e.text != ""):
#             chave = e.text
#             traducao = translator.translate(e.text, dest="hi").text
#             replacements[chave] = traducao
            


# # creates a new translated file in hindi
# with open('coursera-teste.html') as infile, open('coursera-teste-hindi.html', 'w', encoding="utf-8")  as outfile:
#         for line in infile:
#             for k,value  in replacements.items():
#                 line = line.replace(k, replacements[k])
#             outfile.write(line)


        

# with open('index-original-language.html') as infile:
#     for line in infile:
# #          print(line)
# f = open('index-original-language.html');
# html = f.read()
# parsed_html = BeautifulSoup(html, features="html.parser");
# paragrafo = parsed_html.body.findAll('span')
# for p in paragrafo:
#     if  (p == "bookmarks"):
#             p = 'इस प्रकार'
        

# #replace the href attribute from <a> tags

# my_dictionary = {}
# tag = "a"
# elem = browser.find_elements(By.TAG_NAME, tag)
# for e in elem :
#         url = e.get_attribute("href") 
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
# browser.close()
# with open('coursera-teste.html') as infile, open('coursera-teste2.html', 'w', encoding="utf-8") as outfile:
#     for line in infile:
#         for src, target in my_dictionary.items():
#                  line = line.replace(src, target)
#         outfile.write(line)
        
# #append the javascript       

javascript = ['<script src = "https://www.classcentral.com/webpack/7540.b7f3ab16c1d7d344980b.js"></script>',
'<script src = "https://www.classcentral.com/webpack/4826.ea570b7100e8c5e53e11.js"></script>',
'<script src = "https://www.classcentral.com/webpack/analytics.2edefc668ab4db842c41.js"></script>',
'<script src = "https://www.classcentral.com/webpack/Auth.44e05080311528b179c7.js"></script>',
'<script src = "https://www.classcentral.com/webpack/MarkComplete.e9560adcebc4ad54e6bf.js"></script>',
'<script src = "https://www.classcentral.com/webpack/messages-intl-icu-en-yml.64477e124174f9d771be.js"></script>',
'<script src = "https://www.classcentral.com/webpack/Misc.a66f8a686e276f997313.js"></script>',
'<script src = "https://www.classcentral.com/webpack/UserActions.30ee83ef27eafec0be61.js"></script>']

file = open("help" + ".html", "a")
for script in javascript :
    file.write(script)
file.close() 