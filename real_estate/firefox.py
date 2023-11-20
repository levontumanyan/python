from selenium import webdriver
from selenium.webdriver.firefox.options import Options

# Initialize the headless browser
options = Options()
options.headless = True
browser = webdriver.Firefox(options=options)

# Navigate to the search results page for apartments in Toronto
browser.get('https://www.realtor.ca/on/toronto/apartments-for-sale')

# Extract the search results
results = browser.find_elements_by_xpath('//div[@class="card-body pt-2 px-2 px-md-3 px-lg-4"]')

# Print the search results
for result in results:
    print(result.text)

# Close the browser
browser.quit()
