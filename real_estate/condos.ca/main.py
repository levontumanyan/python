import selenium_wrapper
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

EMAIL = "levon.tumanyan@yahoo.ca"

WEBSITE = "https://condos.ca/login"

if __name__ == "__main__":
    browser = webdriver.Safari()

    # Navigate to the search results page for apartments in Toronto
    browser.get(WEBSITE)

    # Wait for the page to load
    browser.execute_script("return document.readyState == 'complete'")
    
    # login part
    email_input = selenium_wrapper.find_by_id( browser, "emaillabel" )
    selenium_wrapper.send_keys( email_input, EMAIL )

    password_input = selenium_wrapper.find_by_id( browser, "passwordlabel" )
    selenium_wrapper.send_keys( password_input, "buhrud-haxkor-5qubTy" )

    # find the login button by xpath
    login_button = selenium_wrapper.find_by_xpath( browser, '//button[text()="Log in"]' )

    selenium_wrapper.click( browser, login_button )

    # Wait for the page to load
    browser.execute_script("return document.readyState == 'complete'")

    # Close the web browser


    while True:
        pass

    browser.quit()


#find an element and send keys to it
