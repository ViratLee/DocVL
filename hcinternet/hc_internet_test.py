import requests, json, io, datetime#, configparser

#config = configparser.ConfigParser()
#config.read('cmic_config.ini')

def load_yaml_config():
    with open('cmic_config.yaml', 'r') as f:
        yaml_file = yaml.safe_load(f)
        return yaml_file

config = load_yaml_config()

cmic_config = config['local']
url = cmic_config['webservices.rest.url']
req_headers = { 
    'Authorization': '{} {}'.format(cmic_config['user.auth'], cmic_config['user.password']),
    'User-Agent':'Mozilla/5.0'
}
def write_output_file(o, line, printoutput=False):
    try:
        if printoutput == True:
           text = '{}'.format(line)
           print(text)
        o.write(line)
        o.write("\n")
    except IOError:
        raise
url = '{}/{}'.format(url,'CMiC/api/external/hcinternet/retrieveClaimList') 
now = datetime.datetime.now()
curDt = '{:%Y-%m-%d_%H%M}'.format(now)
output_path = cmic_config['output.path']
try:
    param_list = {'companyId':'051','providerCode':'1085390014','treatmentType':'1','hospitalizationDtFrom':'2017-10-26 00:00:00','hospitalizationDtTo':'2018-10-29 00:00:00'}
   # param_list = {'companyId':'051','providerCode':'1085390014','treatmentType':'4'}
    json_data_str = ''
    for k, v in param_list.items():
        if not json_data_str:
            json_data_str = '{}={}'.format(k,v)
        json_data_str = '{}&{}={}'.format(json_data_str,k,v)
    oFileName = '{}{}_{}_{}.json'.format(output_path,'HC-retrieveClaimList','Resp',curDt)
    with io.open(oFileName,'a',encoding='utf8') as o:
        url_data = {'url': url, 'data': json_data_str }
        get_url = '{url}?{data}'.format(**url_data)
        request_data = 'request:{}'.format(get_url)
        write_output_file(o,'/*',True)
        write_output_file(o,request_data,True)
        r = requests.get(get_url,  headers=req_headers,verify=False)
        response_code = '-------------response:{}-------------'.format(r.status_code)
        write_output_file(o,response_code,True)
        write_output_file(o,'*/',True)
        parsed = json.dumps(r.json(), indent=4) 
        write_output_file(o,parsed,False)
        #policyList = output['policyList']
        #policy = policyList[0]
        #policy_service = policyService(policy)
        #policy_service.holding(o, policy_number)
        #policy_service.coverage(o, policy_number)
except Exception as e:
    print(e)