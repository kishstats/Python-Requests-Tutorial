import requests

url = 'http://api.worldbank.org/countries?format=json'
response = requests.get(url)

# requests has a builtin JSON decoder
country_data = response.json()

countries = country_data[1]

for country in countries:
    print('country: {} {}'.format(country['name'], country['iso2Code']))
