import requests
url = 'thadculwcm01'
resp = requests.get(url, auth=("msnpeid","J#G5sJfF"))
response_code = '-------------response:{}-------------'.format(resp.status_code)
print(response_code)