import json
import requests
# import pandas as pd

#url = "https://sandbox.repliers.io/listings?listings=true&operator=AND&sortBy=updatedOnDesc&status=A"
url = "https://sandbox.repliers.io/listings?listings=true&operator=AND&sortBy=updatedOnDesc&status=A"

headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "REPLIERS-API-KEY": "KwA03clrvzOTgB8IwPOZzOJ1kucwBR"
}

#response = requests.get(url, headers=headers)
#payload = {"sewer": ["string"]}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    # Get the JSON data from the response
    data = response.json()
    #print(data)
else:
    print("Error:", response.status_code)


num_of_pages = data["numPages"]
print(num_of_pages)
print(data["listings"][0])

for listing in data["listings"]:
    print(listing["soldDate"])

# for page in range(1, num_of_pages):
#     print(page)
#     url1 = f"https://sandbox.repliers.io/listings?listings=true&pageNum={page}&operator=AND&sortBy=updatedOnDesc&status=A"
#     response1 = requests.get(url1, headers=headers)
#     if response1.status_code == 200:
#     # Get the JSON data from the response
#         data1 = response1.json()
#         json_data = json.dumps(data1, indent=4)
#         with open("listings.txt", "a") as listings:
#     # Writing data to a file
#             listings.write(json_data)
#     #print(data)
#     else:
#         print("Error:", response1.status_code)




