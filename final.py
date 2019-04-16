from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from itertools import cycle


def get_lines_from_file(filename):
    file = open(filename, "r")
    result = []

    for line in file:
        line = line.replace("\n", "")
        result.append(str(line))

    return result


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

        return element

    except NoSuchElementException:
        return None


def main():


    for url in get_lines_from_file("url_list.txt"):
        # print("Asking url: " + url)
        browser = request(url)
        result_line = url
        for link_selector in get_lines_from_file("link_selector_list.txt"):
            # print("   Checking link selector: " + link_selector)
            link_element = find_elements(browser, link_selector)
            if (link_element):

                result_line += " |Link selector: " + link_selector

                mainPageLink = link_element.get_attribute('href')

                mainPageBrowser = request(mainPageLink)

                for mainPageSelector in get_lines_from_file("main_page_selector_list.txt"):
                    # print("      Checking main page selector: " + mainPageSelector)
                    main_page_element = find_elements(mainPageBrowser, mainPageSelector)

                    if (main_page_element):
                        result_line += " |Main page selector: " + mainPageSelector

                        break

                for dateSelector in get_lines_from_file("date_selector_list.txt"):
                    date_element = find_elements(mainPageBrowser, dateSelector)

                    if (date_element):
                        result_line += " |Date selector: " + dateSelector

                        break

                for authorSelector in get_lines_from_file("author_selector_list.txt"):
                    author_element = find_elements(mainPageBrowser, authorSelector)

                    if (author_element):
                        result_line += " |Author selector: " + authorSelector

                        break

                #
                # for date_selector in get_lines_from_file("date_selector_list.txt"):
                #     find_elements()

                break

        print(result_line)

    # link_selectors, link_selectors_length = link_selector_list_process()
    #
    # # print(link_selectors)
    # # print(link_selectors_length)
    #
    # for i in range(urls_length):
    #     for i2 in range(link_selectors_length):
    #         # print(urls[i])
    #         # print(link_selectors[i2])
    #         elements = request(urls[i], link_selectors[i2])
    #     # if elements != 0:
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
