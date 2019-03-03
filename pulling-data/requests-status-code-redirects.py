import requests

# URL will redirect to https
response = requests.get('http://github.com/')

print(response.url)  # https://github.com/ 
print(response.status_code)  # 200
print(response.history)  # [<Response [301]>]

r = requests.get('http://github.com/', allow_redirects=False)
print(r.url)  # http://github.com/
print(r.status_code)  # 301
print(r.history)  # []