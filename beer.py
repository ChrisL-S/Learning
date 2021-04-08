import requests
import json
import webbrowser

url = 'https://api.punkapi.com/v2/beers?'
page = 'page=1&per_page=80&'
#abv_gt_num = '20'
#abv_gt = str('?abv_gt='+abv_gt_num)

foodentry = input('Enter food to find a beer accompaniment: ')
food = 'food='+foodentry

response = requests.request("GET", url+page+food)
# print(response.status_code)

beers = response.json()

for beer in beers:
    print(beer["name"])

beerentry = input('Enter one of the beers above for more info: ')

for beer in beers:
    if beerentry.lower() in beer["name"].lower():
        print(json.dumps(beer, indent=4))
        image_url = str(beer["image_url"])
        webbrowser.open(image_url)
        # webbrowser.open(url+'beername='+beer["name"])

#print(json.dumps(beers, indent=4))

"""
for beer in beers:
    if "Lobster thermidor" in beer["food_pairing"]:
        print(json.dumps(beer, indent=4))
"""

# print(beerjson[2])

# print(response.text)
# comment
