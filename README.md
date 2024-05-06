<h1>Automatically Copying Websites Contents</h1>
This project was made as a challenge in a company contest, to automatically scrap and translate to hindi all pages from this particularly company (around 100 pages). For that, I used the Selenium webdriver and pyautogui library. The generated pages includes the original HTML, CSS and Javascript files and links, having the same behaviour as the original website. It has one deep level of links (when click to a button, redirecting to another page).
I written some codes to make this challenge. The order is the following:
<ul>
  <li>
    1 - scrapping.py  - To list all the links we need to scrap (1 and 2 layer); Run that to get the list
  </li>
    <li>
    2 - generate-pages.py  - To scrap and copy the content of all the pages  on the previous list
  </li>
     <li>
    3 - translates.py  - To translate and replace the content of this generated files to hindi
  </li>
    <li>
   4 - generate-index.py  - To include all the external javascript and dependencies in these pages
  </li>
</ul>

