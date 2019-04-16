from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from itertools import cycle


def url_list_process():
    raw_url_list = open("url_list.txt", "r")
    urls = []

    for url in raw_url_list:
        url = url.replace("\n", "")
        urls.append(str(url))
    url_list_length = len(urls)

    return urls, url_list_length


def link_selector_list_process():
    link_selector_list = open("link_selector_list.txt", "r")
    link_selectors = []

    for link_selector in link_selector_list:
        link_selector = link_selector.replace("\n", "")
        link_selectors.append(str(link_selector))
    link_selector_list_length = len(link_selectors)

    return link_selectors, link_selector_list_length


def main_page_selector_list_process():
    main_page_selelector_list = open("main_page_selector_list.txt", "r")
    main_page_selectors = []

    for main_page_selector in main_page_selelector_list:
        main_page_selector = main_page_selector.replace("\n", "")
        main_page_selectors.append(str(main_page_selector))
    main_page_selector_list_length = len(main_page_selectors)

    return main_page_selectors, main_page_selector_list_length


def date_selector_list_process():
    date_selelector_list = open("date_selector_list.txt", "r")
    date_selectors = []

    for date_selector in date_selelector_list:
        date_selector = date_selector.replace("\n", "")
        date_selectors.append(str(date_selector))
    date_selector_list_length = len(date_selectors)

    return date_selectors, date_selector_list_length


def author_selector_list_process():
    author_selelector_list = open("author_selector_list.txt", "r")
    author_selectors = []

    for author_selector in author_selelector_list:
        author_selector = author_selector.replace("\n", "")
        author_selectors.append(str(author_selector))
    author_selector_list_length = len(author_selectors)

    return author_selectors, author_selector_list_length


def set_chrome_driver_location():
    chrome_driver_location = "./chromedriver.exe"
    return chrome_driver_location


def request(url, find_element):
    try:
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--silent')
        options.add_argument('--disable-gpu')
        options.add_argument('--log-level=3')

        browser = webdriver.Chrome(executable_path=set_chrome_driver_location(), chrome_options=options)
        browser.get(url)
        source = browser.page_source
        elements = browser.find_element_by_css_selector(find_element)
        current_url = browser.current_url

        print(current_url, find_element, "JÓ!")

        return elements, options, current_url

    except Exception:
        print(url, find_element, "NEM passzol")
        pass


def main():
    first_article_page = []
    urls, urls_length = url_list_process()
    # print(urls_length)
    # print(urls)

    link_selectors, link_selectors_length = link_selector_list_process()

    # print(link_selectors)
    # print(link_selectors_length)

    for i in range(urls_length):
        for i2 in range(link_selectors_length):
            # print(urls[i])
            # print(link_selectors[i2])
            elements = request(urls[i], link_selectors[i2])
        # if elements != 0:
        #     print(urls[i], link_selectors[i2])
        # else:
        #     print("teszt 2")
        #     # print(elements)

    #
    #
    # # link_selectors = link_selector_list_open()
    #
    #
    # for url in urls:
    #     url = url.split()
    #     url = str(url)
    #     url = url.strip()
    #
    #     url = url.replace("['", "")
    #     url = url.replace("']", "")
    #     print(url)
    #
    #
    #
    #
    #     for link_selector in link_selectors:
    #         link_selector = link_selector.split()
    #         link_selector = str(link_selector)
    #         link_selector = link_selector.strip()
    #         link_selector = link_selector.replace("['", "")
    #         link_selector = link_selector.replace("']", "")
    #
    #         print(link_selector)
    #
    #
    #         try:
    #
    #             elements, options, current_url = request(url, link_selector)
    #         except Exception:
    #             print("nem passzol rá")
    #             pass
    #
    #         if not elements == []:
    #             for element in elements:
    #                 element = element.get_attribute('href')
    #                 print(element)
    #                 while len(first_article_page) < 1:
    #                     first_article_page.append(element)
    #
    #                 #     elements, options, current_url = request(first_article_page[0], '.entry-title>a')
    #                 #     print('A jelenlegi oldal:', current_url)
    #                 #     print(first_article_page)
    #                 #
    #                 # else:
    #                 #     print("nincs ilyen az oldalon")
    #
    #
    #
    #
    #     # request(url, find_element)
    #


if __name__ == '__main__':
    main()
