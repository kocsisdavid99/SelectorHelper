from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from itertools import cycle



def set_chrome_driver_location():
    chrome_driver_location = "./chromedriver.exe"
    return chrome_driver_location


def request(url):
    try:
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--silent')
        options.add_argument('--disable-gpu')
        options.add_argument('--log-level=3')

        browser = webdriver.Chrome(executable_path=set_chrome_driver_location(), chrome_options=options)
        browser.get(url)
        source = browser.page_source

        return browser


    except Exception:
        print(url, "Az oldalt nem sikerült betölteni")




def find_elements(browser, selector):

    try:
        element = browser.find_element_by_css_selector(selector)

    except NoSuchElementException:
        return None








def main():
    source = request("http://akuaku.pl/blog/")
    find_elements(source, ".entry-title>a")




main()

