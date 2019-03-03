import requests
from pprint import pprint

url = 'https://httpbin.org/post'
data = {'user':'me@example.com'}

# as form data
response = requests.post(url, data=data)
print(response)  # <Response [200]>

result = response.json()
print(type(result))  # <class 'dict'>
pprint(result)

print(result['form'])
