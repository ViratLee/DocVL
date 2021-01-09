import requests
url = 'http://127.0.0.1:5000/'
payload = {}
headers = {}
response = requests.request('GET', url, headers = headers, data = payload, allow_redirects=False, timeout=5)
print(type(response))
print(response.text)
