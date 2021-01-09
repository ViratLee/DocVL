import sys, requests, json, io, datetime, json#configparser, json
from pprint import pprint
import yaml


def load_yaml_config():
    with open('cmic_config.yaml', 'r') as f:
        yaml_file = yaml.safe_load(f)
        return yaml_file

def read_json_data_as_text(json_file):
    with open(json_file,encoding='utf-8') as f:
        content = f.read()
    return content

#http://thadcdlwce01:19080/sonora/cmicrest/workflow/createWork
def new_case(claim_info_data):
    url = cmic_config['webservices.360.url']
    url = '{}/{}'.format(url,'sonora/cmicrest/workflow/createWork')
    print(url)
    print('sending...')
    r = requests.post(url, data=claim_info_data.encode('utf-8'), headers=req_headers)
    response_code = '-------------response:{}-------------'.format(r.status_code)
    print(response_code)
    #[{"code":"S","message":"Success","data":{"caseId":20582}}]
    parsed = json.dumps(r.json(), indent=4) 
    output = r.json()
    data = output['data']
    print('code:{}'.format(data['caseId']))

config = load_yaml_config()
cmic_config = config['sit']
req_headers = { 
    'Authorization': '{} {}'.format(cmic_config['webservices.360.user.auth'], cmic_config['webservices.360.user.password']),
    'Content-Type': 'application/json',
    'User-Agent':'Mozilla/5.0'
}

if __name__ == '__main__':
    #file_name_IB = 'claim_info_to_OPD_pol_T202054663.json'
    file_name_CS = 'claim_info_to_OPD_pol_0000013332.json'
    #file_name_IB = 'claim_info_to_OPD_pol_T149940241.json'
    file_name_IB = 'claim_info_to_OPD_pol_P330003641.json'
    
    clm_info_data = read_json_data_as_text(file_name_IB)
    # clm_info_json = json.loads(clm_info_data)
    # clm_info_json['ipdOpd'] = 'IPD'
    # clm_info_json['claimType'] = 'Cashless'
    # p_dat = json.dumps(clm_info_json, indent=4)
    new_case(clm_info_data)