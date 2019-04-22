from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import SelectorStatistics
from SelectorStatistics import SelectorStatistics


def get_lines_from_file(filename):
    file = open(filename, "r")
    result = []

    for line in file:
        line = line.replace("\n", "")
        if line != "":
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

        return browser


    except Exception:
        print("Az oldalt nem sikerült betölteni: '" + url + "'")


def find_elements(browser, selector):
    try:
        element = browser.find_element_by_css_selector(selector)

        return element

    except NoSuchElementException:
        return None


def main():
    LinkSelectorStatistics = SelectorStatistics()
    MainContentSelectorStatistics = SelectorStatistics()
    DateSelectorStatistics = SelectorStatistics()
    AuthorSelectorStatistics = SelectorStatistics()

    urls = get_lines_from_file("url_list.txt")
    for url in urls:
        # print("Asking url: " + url)
        browser = request(url)
        if browser:

            result_line = url
            link_selectors = get_lines_from_file("link_selector_list.txt")
            for link_selector in link_selectors:
                # print("   Checking link selector: " + link_selector)
                link_element = find_elements(browser, link_selector)
                if (link_element):

                    result_line += " |Link selector: " + link_selector
                    LinkSelectorStatistics.increment(link_selector)

                    mainPageLink = link_element.get_attribute('href')

                    mainPageBrowser = request(mainPageLink)

                    if mainPageBrowser:

                        main_content_selectors = get_lines_from_file("main_content_selector_list.txt")
                        for main_content_selector in main_content_selectors:
                            # print("      Checking main page selector: " + mainPageSelector)
                            main_content_element = find_elements(mainPageBrowser, main_content_selector)

                            if (main_content_element):
                                result_line += " |Main content selector: " + main_content_selector
                                MainContentSelectorStatistics.increment(main_content_selector)

                                break

                        date_selectors = get_lines_from_file("date_selector_list.txt")
                        for dateSelector in date_selectors:
                            date_element = find_elements(mainPageBrowser, dateSelector)

                            if (date_element):
                                result_line += " |Date selector: " + dateSelector
                                DateSelectorStatistics.increment(dateSelector)

                                break

                        author_selectors = get_lines_from_file("author_selector_list.txt")
                        for authorSelector in author_selectors:
                            author_element = find_elements(mainPageBrowser, authorSelector)

                            if (author_element):
                                result_line += " |Author selector: " + authorSelector
                                AuthorSelectorStatistics.increment(authorSelector)

                                break

                    break

        print(result_line)

    print("Link selector statistics:")
    LinkSelectorStatistics.print()

    print("Main page selector statistics:")
    MainContentSelectorStatistics.print()

    print("Date selector statistics:")
    DateSelectorStatistics.print()

    print("Author selector statistics:")
    AuthorSelectorStatistics.print()

    LinkSelectorStatistics.chart()
    MainContentSelectorStatistics.chart()
    DateSelectorStatistics.chart()
    AuthorSelectorStatistics.chart()


if __name__ == '__main__':
    main()
