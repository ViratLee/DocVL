import requests, json, io, datetime#, configparser
from policy_service import policyService
import yaml
def load_yaml_config():
    with open('cmic_config.yaml', 'r') as f:
        yaml_file = yaml.safe_load(f)
        #pp.pprint(yaml_file)
        return yaml_file

config = load_yaml_config()
# config = configparser.ConfigParser()
# config.read('cmic_config.ini')
cmic_config = config['prod']
#print('{} {}'.format(cmic_config['user.auth'], cmic_config['user.password']))
url = cmic_config['webservices.rest.url']
req_headers = { 
    'Authorization': '{} {}'.format(cmic_config['user.auth'], cmic_config['user.password']),#;'Basic QkFQUEVTQjpLbjR5SWFnQEtx', # UAT
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
url = '{}/{}'.format(url,'rest/AIAService/policy/retrievePolicy/RetrievePolicy') 
#policy_list =['U881138502','P051080422']
#policy_list =['T303726971']
#policy_list = ['P014153008']
#policy_list = ['T075599355','T002283922']
#policy_list = ['P703811059']
policy_list = ['0000104957']
#policy_list = ['T196444826','T176169862','P741093622','T180099818','P740224285']
#policy_list = ['T004455240','T100707876','T204026893','P304642119','T206291943','P302818916','T116941998','P303023661','P301430599','T207248092','P307256858','T078893621','T096485516','T199227532','T212383201','T208201562','T000045699','T210294839','P304640742']
#'T164618367','U880818263','T164618370',
#'P303259011','U880840095','T154367466','T164618383',
#'T206951102','T174364614','T199951976','T200015141','U880869584','T099209883','U881841297','T990528058']
count = 0
now = datetime.datetime.now()
curDt = '{:%Y-%m-%d_%H%M}'.format(now)
output_path = cmic_config['output.path']
for policy_number in policy_list:
    try:
        count += 1
        oFileName = '{}{}_{}_{}_{}.json'.format(output_path,'RetrievePolicy',policy_number,'Resp',curDt)
        with io.open(oFileName,'a',encoding='utf8') as o:
            input("Press any key to continue...")
            print('###{}###'.format(count))
            json_data_str = '{"policyNo":"'+policy_number+'","companyId":"1"}'
            url_data = {'url': url, 'data': json_data_str }
            get_url = '{url}?json={data}'.format(**url_data)
            request_data = 'request:{}'.format(get_url)
            write_output_file(o,'/*',True)
            write_output_file(o,request_data,True)
            r = requests.get(get_url,  headers=req_headers,verify=False)
            response_code = '-------------response:{}-------------'.format(r.status_code)
            write_output_file(o,response_code,True)
            write_output_file(o,'*/',True)
            parsed = json.dumps(r.json(), indent=4) 
            write_output_file(o,parsed,True)
            # output = r.json()
            # policyList = output['policyList']
            # policy = policyList[0]
            """
            policy_service = policyService(policy)
            policy_service.holding(o, policy_number)
            policy_service.coverage(o, policy_number)
            """
            # holdingList = policy['holdingList']
            # holding = holdingList[0]
            # holdingPartyRelationList = holding['holdingPartyRelationList']
            # write_output_file(o,'/*------polno {}-------------'.format(policy_number),True)
            # for holdingPartyRelation in holdingPartyRelationList:
            #    holdingPartyRelCd = holdingPartyRelation['holdingPartyRelCd']
            #    partyId = holdingPartyRelation['partyId']
            #    write_output_file(o,'holdingPartyRelCd:{} - partyId:{}'.format(holdingPartyRelCd, partyId),True)
            # write_output_file(o,'---------------------------*/',True)
    except Exception as e:
        print(e)
        break
#parsed = json.loads(r.json())
#print(json.dumps(parsed, indent=4, sort_keys=True)
#output = r.json()
#print(output['code'])
#print(output['message'])
#print(output['data'])
#print(r.headers['content-type'])