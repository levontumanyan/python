import selenium_wrapper
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

WEBSITE_2022 = "https://www.gta-homes.com/pre-construction-condos-2022/"
WEBSITE_2023 = "https://www.gta-homes.com/pre-construction-condos-2023/"

DT_POSTAL_CODES = [ "M5L", "M5S", "M5K", "M5J", "M5H", "M5G", "M5E", "M5C", "M5B", "M5T", "M4Y", "M4X", "M4W", "M5V", "M5X", "M6G" ]

def is_dt_condo(address):
    for postal_code in DT_POSTAL_CODES:
        if postal_code in address:
            return True
    return False

if __name__ == "__main__":
    browser = webdriver.Safari()

    # Navigate to the search results page for apartments in Toronto
    browser.get(WEBSITE_2022)

    # Wait for the page to load
    browser.execute_script("return document.readyState == 'complete'")

    # Find all the divs with class 'my-class'
    condos_address = selenium_wrapper.find_divs_with_class( browser, "listing-address" )

    condos = selenium_wrapper.find_divs_with_class( browser, "col-listings" )


    # Print the text content of each div
    dt_condos = [ condo.text for condo in condos_address if is_dt_condo(condo.text) ]
    final_list = dt_condos[:]

    browser.get(WEBSITE_2023)

    # Wait for the page to load
    browser.execute_script("return document.readyState == 'complete'")
    
    # Find all the divs with class 'my-class'
    condos_address = selenium_wrapper.find_divs_with_class( browser, "listing-address" )

    condos = selenium_wrapper.find_divs_with_class( browser, "col-listings" )


    # Print the text content of each div
    dt_condos = [ condo.text for condo in condos_address if is_dt_condo(condo.text) ]
    final_list += dt_condos[:]

    # print the final list of all the apartments both 2022 and 2023
    for condo in final_list:
        print(condo)


    while True:
        pass
        
    # Close the web browser
    browser.quit()
