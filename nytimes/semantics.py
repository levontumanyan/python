import requests

url = "http://api.nytimes.com/svc/semantic/v2/concept"
#url1 = "http://api.nytimes.com/svc/semantic/v2/concept/name/nytd_per/Obama, Barack.json"
url1 = "https://api.nytimes.com/svc/mostpopular/v2/emailed/1.json"


query = {
    "api-key": "b6kop174AF95tUFkbvaW4KP6Euefgmuv",
    #"q": "python"
}

query1 = {
    "api-key": "ev6w2cRLGAoJoP28pwG20CIYYM9pGGoe",
    #"q": "python"
}


response = requests.get(url1, params=query1)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Request failed with status code:", response.status_code)