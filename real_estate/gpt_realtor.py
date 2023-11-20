import requests

# Replace YOUR_API_KEY with your actual Realtor.ca API key
api_key = "YOUR_API_KEY"

# Set the API endpoint URL and parameters
url = "https://api2.realtor.ca/Listing.svc/PropertySearch_Post"
params = {
    "CultureId": 1,
    "ApplicationId": 1,
    "PropertySearchTypeId": 1,
    "TransactionTypeId": 2,
    "PriceMin": 0,
    "PriceMax": 1000000,
    "BedRange": "1-0",
    "BathRange": "1-0",
    "RecordsPerPage": 10,
    "LongitudeMin": -79.62,
    "LongitudeMax": -79.2,
    "LatitudeMin": 43.55,
    "LatitudeMax": 43.85,
    "SortOrder": "A",
    "SortBy": "1",
    "ZoomLevel": 10,
    "PropertyTypeGroupID": 1,
    "MaximumResults": 10,
    "BuildingTypeId": 1
}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299",
    "Authorization": "Bearer " + api_key
}

# Make the API request
response = requests.post(url, json=params, headers=headers)

# Print the results
print(dir(response))
print(response)


# scrape realtor.ca for apartments in toronto with 1 bedroom and price between $200,000 and $800,000


