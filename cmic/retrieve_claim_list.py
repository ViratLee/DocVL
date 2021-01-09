import requests, json, io, datetime, json #, configparser
import yaml
def load_yaml_config():
    with open('cmic_config.yaml', 'r') as f:
        yaml_file = yaml.safe_load(f)
        #pp.pprint(yaml_file)
        return yaml_file

config = load_yaml_config()
# config = configparser.ConfigParser()
# config.read('cmic_config.ini')
cmic_config = config['local']
url = cmic_config['webservices.rest.url']
req_headers = { 
    'Authorization': '{} {}'.format(cmic_config['user.auth'], cmic_config['user.password']),#;'Basic QkFQUEVTQjpLbjR5SWFnQEtx', # UAT
    'User-Agent':'Mozilla/5.0',
    'Content-type': 'application/json'
}


url = '{}{}'.format(url,'/CMiC/api/rest/claim/retrieveClaimList') 
now = datetime.datetime.now()
curDt = '{:%Y-%m-%d_%H%M}'.format(now)
output_path = cmic_config['output.path']

def get_claim_list():
    try:
        claimStatus = '70'
        companyId = '051'
        get_url = f'{url}?claimStatus={claimStatus}&companyId={companyId}'
        print(get_url)
        request_data = 'request:{}'.format(get_url)
        r = requests.get(get_url, headers=req_headers, verify=False)
        print(r)
        response_code = '-------------response:{}-------------'.format(r.status_code)
        parsed = json.dumps(r.json(), indent=4) 
        print(parsed)
        output = r.json()
        lstOfClaimSnapshot = output['lstOfClaimSnapshot']
        print(len(lstOfClaimSnapshot))
    except Exception as e:
        print(e)

def main():
    get_claim_list()
if __name__ == '__main__':
    main()  
#parsed = json.loads(r.json())
#print(json.dumps(parsed, indent=4, sort_keys=True)
#output = r.json()
#print(output['code'])
#print(output['message'])
#print(output['data'])
#print(r.headers['content-type'])