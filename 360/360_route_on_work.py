import requests
import json, io, datetime, configparser, json
config = configparser.ConfigParser()
config.read('cmic_config.ini')
cmic_config = config['uat']
req_headers = { 
    'Authorization': '{} {}'.format(cmic_config['webservices.360.user.auth'], cmic_config['webservices.360.user.password']),
    'User-Agent':'Mozilla/5.0'
}

def route_to_deduct(caseid):
    url = cmic_config['webservices.360.url']
    url = '{}/{}'.format(url,'sonora/cmicrest/workflow/routeOnWork/{}/dispatch/DEDUCT'.format(caseid)) 
    print(url)
    print('routeOnWork deduct...{}'.format(caseid))
    r = requests.post(url, headers=req_headers)
    response_code = '-------------response:{}-------------'.format(r.status_code)
    print(response_code)
    parsed = json.dumps(r.json(), indent=4) 
    print(parsed)

def route_to_preauth(caseid):
    url = cmic_config['webservices.360.url']
    url = '{}/{}'.format(url,'sonora/cmicrest/workflow/routeOnWork/{}/dispatch/REJECT'.format(caseid)) 
    print(url)
    print('routeOnWork ADJUT...{}'.format(caseid))
    r = requests.post(url, headers=req_headers)
    response_code = '-------------response:{}-------------'.format(r.status_code)
    print(response_code)
    parsed = json.dumps(r.json(), indent=4) 
    print(parsed)

def route_to_data_entry(caseid):
    url = cmic_config['webservices.360.url']
    url = '{}/{}'.format(url,'sonora/cmicrest/workflow/routeOnWork/{}/dispatch/DIRECTD'.format(caseid)) 
    print(url)
    print('routeOnWork DATE ENTRY...{}'.format(caseid))
    r = requests.post(url, headers=req_headers)
    response_code = '-------------response:{}-------------'.format(r.status_code)
    print(response_code)
    parsed = json.dumps(r.json(), indent=4) 
    print(parsed)

if __name__ == '__main__':
    # route_to_deduct('19172')
    # route_to_deduct('19173')
    # route_to_deduct('19174')
    # route_to_deduct('19175')
    route_to_data_entry('1152495')