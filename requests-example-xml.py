import requests
import xml.etree.ElementTree as ET

url = 'http://api.worldbank.org/countries'

response = requests.get(url)
country_data = response.text

countries = ET.fromstring(country_data)
namespaces = {'wb': 'http://www.worldbank.org'}

for country in countries.findall('wb:country', namespaces):
    name = country.find('wb:name', namespaces).text
    code = country.find('wb:iso2Code', namespaces).text

    print('country: {} - {}'.format(name, code))
