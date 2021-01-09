import requests
import json
#url = 'http://127.0.0.1:5000/api/json_data'
# payload = {}
# headers = {}
# response = requests.request('POST', url, headers = headers, data = payload, allow_redirects=False, timeout=5)
# print(type(response))
# print(response.text)
# parsed = json.dumps(response.json(), indent=4) 
# print(type(parsed))
# print(parsed)

r = requests.post('http://127.0.0.1:5000/api/json_data')
#print(r)
#print(r.status_code)
#print(type(r.json()))
response = json.dumps(r.json(), indent=4)
print(response)