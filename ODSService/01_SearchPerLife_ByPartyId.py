import requests, json, io, datetime#, configparser
from policy_service import policyService
import yaml
# import pprint
# pp = pprint.PrettyPrinter(indent=4)

def load_yaml_config():
    with open('cmic_config.yaml', 'r') as f:
        yaml_file = yaml.safe_load(f)
        #pp.pprint(yaml_file)
        return yaml_file

config = load_yaml_config()
cmic_config = config['prod']
req_headers = { 
    'Authorization': '{} {}'.format(cmic_config['user.auth'], cmic_config['user.password']),#;'Basic QkFQUEVTQjpLbjR5SWFnQEtx', # UAT
    'User-Agent':'Mozilla/5.0'
}
req_headers['Authorization'] = '{} {}'.format(cmic_config['user.auth'], cmic_config['user.password'])
url = cmic_config['webservices.rest.url']
# config = configparser.ConfigParser()
# config.read('cmic_config.ini')
# cmic_config = config['prod']
# print('{} {}'.format(cmic_config['user.auth'], cmic_config['user.password']))
# url = cmic_config['webservices.rest.url']
# req_headers = { 
#     'Authorization': '{} {}'.format(cmic_config['user.auth'], cmic_config['user.password']),#;'Basic QkFQUEVTQjpLbjR5SWFnQEtx', # UAT
#     'User-Agent':'Mozilla/5.0'
# }
url = '{}/{}'.format(url,'rest/AIAService/policy/searchPolicy/SearchPolicyPerlifeByPartyId')
#party_list =['84746367','197053844']
#party_list =['67592922']
#party_list =['249576882']
#party_list =['18763061','18619551'] # GPSE
#party_list =['18643000']# GPSE
#party_list =['18728440']# GPSE
#party_list =['18785041']
#party_list =['18643000'] 
#party_list =['68927991']
#party_list =['66850199'] # prod
#party_list =['79220572'] # prod
#party_list =['391595740'] # prod
#party_list =['31988147']# GPSE
#party_list =['386372533']
#party_list =['393869115']
#party_list =['379573464']
#party_list =['396866155']
party_list =['64920655']


output_path = cmic_config['output.path']
#dedupe_mode = ', "dedupeMode":"partyDedupe"'
dedupe_mode = ''
def write_output_file(o, line, printoutput=False):
    try:
        if printoutput == True:
           text = '{}'.format(line)
           print(text)
        o.write(line)
        o.write("\n")
    except IOError:
        raise
def callService():
    count = 0
    now = datetime.datetime.now()
    curDt = '{:%Y-%m-%d_%H%M}'.format(now)
    for p in party_list:
        try:
            oFileName = '{}_{}_{}_{}_{}.json'.format(output_path,'SearchPolicyPerlifeByPartyId',p,'Resp',curDt)
            with io.open(oFileName,'a',encoding='utf8') as o:
                count += 1
                print('###{}###'.format(count))
                json_data_str = '{"partyId":"'+p+'","companyId":"1" ' + dedupe_mode + '}'
                url_data = {'url': url, 'data': json_data_str }
                get_url = '{url}?json={data}'.format(**url_data)
                request_data = 'request:{}'.format(get_url)
                write_output_file(o,'/*',True)
                write_output_file(o,request_data,True)
                r = requests.get(get_url, headers=req_headers, verify=False)
                response_code = '-------------response:{}-------------'.format(r.status_code)
                write_output_file(o,response_code,True)
                #parsed = json.dumps(r.json(),ensure_ascii=False, indent=4) 
                output = r.json()
                policyPerlifeList = output['policyPerlifeList']
                write_output_file(o,'policy per life size {}'.format(len(policyPerlifeList)), True)
                write_output_file(o,'*/',True)
                parsed = json.dumps(r.json(),ensure_ascii=False,  indent=4)
                write_output_file(o,parsed,True)
                len_pol = len(policyPerlifeList)
                print(f'{len_pol}')
                find_hnw_product(policyPerlifeList)
                #if len(policyPerlifeList) > 0:
                     # policy = policyPerlifeList[0]
                     # policy_service = policyService(policy)
                     # pol_num_set = policy_service.unique_policy_number(o, policyPerlifeList)
                     # write_output_file(o,'/*policy all {}, but policy unique {}'.format(len(policyPerlifeList), len(pol_num_set)),True)
                     # for policy in pol_num_set:
                     #     covNum = policy['covNum']
                     #     productCd = policy['productCd']
                     #     polNum = policy['polNum']
                     #     p_policy = f'**********found HNW {covNum}/{polNum}/{productCd}'
                     #     write_output_file(o,p_policy,True)
                     # write_output_file(o,'*/',True)
                    
        except Exception as e:
            print(e)
            break

def find_hnw_product(policyPerlifeList):
    found = False
    hnw_product = ['990E07','990D07','990F07']
    policy_list=[]
    for policy in policyPerlifeList:
        covNum = policy['covNum']
        productCd = policy['productCd']
        polNum = policy['polNum']
        policyStatus = policy['policyStatus']
        if productCd in hnw_product:
            print(f'**********found HNW {covNum}/{polNum}/{productCd}/{policyStatus}')
            found = True
    return found

def main():
    callService()
if __name__ == '__main__':
    main()
#parsed = json.loads(r.json())
#print(json.dumps(parsed, indent=4, sort_keys=True)
#output = r.json()
#print(output['code'])
#print(output['message'])
#print(output['data'])
#print(r.headers['content-type'])