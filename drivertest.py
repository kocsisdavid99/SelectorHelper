from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True
driver = webdriver.Chrome(executable_path='./chromedriver.exe', chrome_options=options)
driver.get('https://eu.udacity.com/')
html = driver.page_source
print(html)
