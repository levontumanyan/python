# imports
#from bs4 import BeautifulSoup
#import requests
from selenium import webdriver


# 1. input :Search any listing #, address or neighbourhood
# 2. find on the main page the search box and input the string from the step 1.
# 3. 
def main():
	main_page_url = "https://housesigma.com/web/en"
	sold_recently_url = "https://housesigma.com/web/en/recommend/more/1"

	# Start a new Firefox browser instance
	browser = webdriver.Firefox()

	# Navigate to the website you want to scrape
	browser.get(sold_recently_url)

	# Find the element you want to interact with using its CSS selector
	
	
	# Enter text into the search box
	search_box.send_keys("Search Term")

	# Click the search button to submit the form
	search_button = browser.find_element_by_css_selector("input[type='submit']")
	search_button.click()

	# Wait for the page to load before getting the HTML
	# You can use explicit wait or implicit wait
	# browser.implicitly_wait(10)

	# Get the HTML of the page
	html = browser.page_source

	# Close the browser
	browser.quit()

	# Use BeautifulSoup to parse the HTML
	soup = BeautifulSoup(html, "html.parser")

	# Find the elements you want to scrape
	results = soup.find_all("div", class_="result")

	# Print the text of each result
	for result in results:
		print(result.text)




	#print(search_box)

	# search_box = soup.find("span", {"class": "ListingPrice"}).text

if __name__ == '__main__':
	main()