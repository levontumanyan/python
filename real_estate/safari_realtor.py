from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# Initialize the headless browser
caps = DesiredCapabilities.SAFARI.copy()
caps['safari:options'] = {'args': '-headless'}
browser = webdriver.Safari(desired_capabilities=caps)

# Navigate to the search results page for apartments in Toronto
browser.get('https://www.realtor.ca/on/toronto/apartments-for-sale')

# Wait for the page to load
browser.execute_script("return document.readyState == 'complete'")

# Extract the search results
results = browser.find_elements('xpath', '//div[@class="card-body pt-2 px-2 px-md-3 px-lg-4"]')
if results:
    listings = results[0].find_elements('xpath', './/div[@class="card m-0 p-0 card-list__card"]')

    # Print the search results
    for listing in listings:
        print(listing.text)
else:
    print("No search results found.")

# Close the browser
browser.quit()
