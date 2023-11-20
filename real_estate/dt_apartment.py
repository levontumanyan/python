import requests
from bs4 import BeautifulSoup

# Define the search parameters
location = "toronto"
price_range = "$200,000-$800,000"
num_bedrooms = "1"

# Send a GET request to the search page
url = f"https://www.realtor.ca/map#q={location}&p={price_range}&nbr={num_bedrooms}&sort=1"
response = requests.get(url)

# Parse the HTML response using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Extract the apartment listings
apartments = soup.find_all("div", class_="listing-details")

# Print the address and price of each apartment
for apartment in apartments:
    address = apartment.find("div", class_="listing-address").text.strip()
    price = apartment.find("span", class_="listing-price").text.strip()
    print(f"{address} - {price}")
