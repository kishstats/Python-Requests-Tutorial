import requests

with requests.Session() as s:
    # sets cookie
    res = s.get('https://httpbin.org/cookies/set/abc/123')
    print('res: {}'.format(res.text))

    # returns cookies
    res = s.get('https://httpbin.org/cookies')
    print('res: {}'.format(res.text))
    # Outputs
    # res: {
    #   "cookies": {
    #     "abc": "123"
    #   }
    # }

    print(s.cookies)  # RequestsCookieJar object
    print('actual cookies: {}'.format(s.cookies.get_dict()))  # actual cookies: {'abc': '123'}
