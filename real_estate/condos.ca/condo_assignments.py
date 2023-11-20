from bs4 import BeautifulSoup
import requests

WEBSITE = "https://torontoassignments.com"

DT_POSTAL_CODES = [ "M5L", "M5S", "M5K", "M5J", "M5H", "M5G", "M5E", "M5C", "M5B", "M5T", "M4Y", "M4X", "M4W", "M5V", "M5X", "M6G" ]

def is_toronto_condo(text):
    if "Toronto" in text:
        return True
    return False

if __name__ == "__main__":

    # Navigate to the search results page for apartments in Toronto
    response = requests.get(WEBSITE)

    # Wait for the page to load

    soup = BeautifulSoup(response.content, "html.parser")
    #assignments = soup.find_all("div", class_="col-md-4 col-sm-6 col-xs-12")
    assignments = soup.find_all("p", class_="address")

    for assignment in assignments:
        if is_toronto_condo(assignment.get_text()):
            print(assignment.get_text())
