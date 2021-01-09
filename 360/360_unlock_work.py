import requests
import json, io, datetime, configparser, json
config = configparser.ConfigParser()
config.read('cmic_config.ini')
cmic_config = config['sit']
req_headers = { 
    'Authorization': '{} {}'.format(cmic_config['webservices.360.user.auth'], cmic_config['webservices.360.user.password']),
    'User-Agent':'Mozilla/5.0'
}

def unlockWork(caseid):
    url = cmic_config['webservices.360.url']
    url = '{}/{}'.format(url,'sonora/cmicrest/workflow/unlock/{}'.format(caseid)) 
    print(url)
    print('unpend work...')
    r = requests.post(url, headers=req_headers)
    response_code = '-------------response:{}-------------'.format(r.status_code)
    print(response_code)
    parsed = json.dumps(r.json(), indent=4) 
    print(parsed)

if __name__ == '__main__':
    unlockWork('20479')


    