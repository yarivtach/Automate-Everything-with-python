import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import time

"""
This function is used to get the driver for the chrome browser
@param url: The url of the website to be scraped
@return: The driver for the chrome browser
"""
def get_driver(url):
    # This lines starts the chrome browser
    service = Service('d:\\_WORK\\Courses\\Automate Everything with python\\chromdriver\\chromedriver.exe')
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(service=service , options=options)
    driver.get(url)
    return driver

def clean_text(text):
    """
    This function is used to clean the text from the website
    @param text: The text to be cleaned
    @return: The cleaned text
    """
    output = text.split(":")[1]
    return output

def main():
    driver = get_driver("http://automated.pythonanywhere.com")
    time.sleep(2) # When we want to get the data from the website about changing value, we need to hold the scraping and then continue
    value = "/html/body/div[1]/div/h1[1]"
    element = driver.find_element(by = "xpath", value = value) # CAN BE WRITE AS (By.XPATH, value = "/html/body/div[1]/div/h1[1]")
    return element

print(main().text)

# ------- Automate LOGIN ---------