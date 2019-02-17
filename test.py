from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options



options = Options()
options.add_argument('--headless')
options.add_argument('--silent')
options.add_argument('--disable-gpu')
options.add_argument('--log-level=3')
        
browser = webdriver.Chrome(executable_path='./chromedriver.exe', chrome_options=options)

browser.get('http://akuaku.pl/blog/')
source = browser.page_source
elements = browser.find_elements_by_css_selector('.entry-title>a')
if not elements == []:
    print(elements)
else:
    print("csá")




        


    




