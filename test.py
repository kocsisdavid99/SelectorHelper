from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


raw_url_list = open("url_list.txt", "r")

for row in raw_url_list:
    row = row.split()
    row = str(row)
    row = row.strip()
    
   
    row = row.replace("['","")
    row = row.replace("']","")
    row = row.replace("', '›","")
    print(row)

link_selectors = ['.entry-title>a',
                  'a.post-title',
                  'a.title',
                  '.news-title>a',
                  '.post-title>a']



first_article_page = []

def request(url, find_element):


    options = Options()
    options.add_argument('--headless')
    options.add_argument('--silent')
    options.add_argument('--disable-gpu')
    options.add_argument('--log-level=3')

    browser = webdriver.Chrome(executable_path='./chromedriver.exe', chrome_options=options)
    browser.get(url)
    source = browser.page_source
    elements = browser.find_elements_by_css_selector(find_element)
    current_url = browser.current_url

    return elements, options, current_url


elements, options, current_url = request('http://akuaku.pl/blog/','.entry-title>a')


if not elements == []:
    for element in elements:
        element = element.get_attribute('href')
        print(element)
        while len(first_article_page) < 1:
            first_article_page.append(element)

    elements, options, current_url = request(first_article_page[0],'.entry-title>a')
    print('A jelenlegi oldal:',current_url)
    print(first_article_page)
        
else:
    print("nincs ilyen az oldalon")




        


    




