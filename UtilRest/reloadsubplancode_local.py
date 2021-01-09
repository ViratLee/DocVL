import configparser
import requests
import json

config = configparser.ConfigParser()
config.read('cmic_config.ini')
cmic_config = config['local']
req_headers = { 
    'Authorization': '{} {}'.format(cmic_config['user.auth'], cmic_config['user.password']),
    'Content-Type': 'application/json',
    'User-Agent':'Mozilla/5.0'
}

url = cmic_config['webservices.rest.url']
url = '{}/{}'.format(url, 'CMiC/api/rest/loadSubPlanCode/false')
print(url)
print('sending...')
r = requests.get(url, headers=req_headers)
response_code = '-------------response:{}-------------'.format(r.status_code)
if r.status_code == 200:
	parsed = json.dumps(r.json(), indent=4) 
	print(parsed)