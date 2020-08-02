from selenium import webdriver
import time


def get_titles():
    driver = webdriver.Chrome(r'F:\chromedriver.exe')
    driver.get('https://www.nytimes.com/')

    # Wait until the page load completely
    time.sleep(20)
    element = driver.find_elements_by_xpath('//article//h2')

    # Append title to the list
    titles = []
    for title in element:
        titles.append(title.text)

    driver.quit()
    return titles