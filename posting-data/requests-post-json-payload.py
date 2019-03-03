import requests
import json
from pprint import pprint

url = 'https://httpbin.org/post'
headers = {
    'Content-Type': 'application/json',
    # additional headers here, i.e. User Agent
}

data = {'user':'me@example.com'}

# as payload
response = requests.post(url, data=json.dumps(data), headers=headers)

print(response.request.headers)
print('---')

result = response.json()
pprint(result)
