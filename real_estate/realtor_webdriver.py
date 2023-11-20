from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the headless browser
options = webdriver.ChromeOptions()
options.add_argument('headless')
browser = webdriver.Chrome(options=options)

# Navigate to the search results page for apartments in Toronto
browser.get('https://www.realtor.ca/map#view=list&Sort=1-D&GeoIds=g30_hxo4s6s7&GeoName=Toronto%2C+ON&PropertyTypeGroupID=1&PropertySearchTypeId=1&TransactionTypeId=2&PriceMin=0&PriceMax=1000000&BedsRange=1-0&BathsRange=1-0')

# Wait for the search results to load
wait = WebDriverWait(browser, 10)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'listing__content')))

# Extract the search results
results = browser.find_elements_by_class_name('listing__content')

# Print the search results
for result in results:
    print(result.text)

# Close the browser
browser.quit()

