from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Find the email input box and enter the email address
def find_by_id(browser, id):
    return browser.find_element(By.ID, id)

def send_keys(selenium_html_object, input):
    selenium_html_object.send_keys(input)

def find_by_xpath(browser, xpath):
    return browser.find_element(By.XPATH, xpath)

def click(browser, selenium_html_object):
    browser.execute_script("arguments[0].click();", selenium_html_object)

def find_divs_with_class(browser, class_name):
    """
    Find all the divs on a page with a given class name using the provided Selenium driver object.
    """
    wait = WebDriverWait(browser, 10)
    divs = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, f"div.{class_name}")))
    return divs

