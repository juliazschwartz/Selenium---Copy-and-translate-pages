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
