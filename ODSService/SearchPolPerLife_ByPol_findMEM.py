import requests, json, io, datetime
import yaml
def load_yaml_config():
    with open('cmic_config.yaml', 'r') as f:
        yaml_file = yaml.safe_load(f)
        #pp.pprint(yaml_file)
        return yaml_file

config = load_yaml_config()
cmic_config = config['prod']
url = cmic_config['webservices.rest.url']
req_headers = { 
    'Authorization': '{} {}'.format(cmic_config['user.auth'], cmic_config['user.password']),#;'Basic QkFQUEVTQjpLbjR5SWFnQEtx', # UAT
    'User-Agent':'Mozilla/5.0'
}
url = '{}/{}'.format(url,'rest/AIAService/policy/searchPolicy/SearchPolicyPerlifeByPolicy') 
#pol_cert_list ={'0000013891': '0000000005'}
#pol_cert_list ={'0000014252': '0000000003'}
#pol_cert_list ={'02104': '1998000090'}
#pol_cert_list ={'02104': '1998000050'}
#pol_cert_list = {'02310':'2004000350'}
#pol_cert_list ={'07233': '2007000090'}
#pol_cert_list ={'02342': '2000003230'}
#uat
#pol_cert_list ={'0000015191': '252671'}
#prod
#pol_cert_list ={'0000085360': '0191407316'}
#pol_cert_list ={'0000014503': '0000000413'}
#pol_cert_list ={'0000102972':'00-58-0001'}
#pol_cert_list ={'00000A4270':'0000000005'}
#pol_cert_list ={'00000F2769':'0000000002'}
pol_cert_list ={'0000011144':'01711790'}

dedupe_mode = ', "dedupeMode":"partyDedupe"'
#dedupe_mode = ', "dedupeMode":"policyDedupe"'
#dedupe_mode = ''
now = datetime.datetime.now()
curDt = '{:%Y-%m-%d_%H%M}'.format(now)
output_path = cmic_config['output.path']

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
    for p, c in pol_cert_list.items():
        try:
            cert_param = ''
            if c:
                cert_param = ',"certificateNum":"{}"'.format(c)
                oFileName = '{}_{}_pol_{}_cert_{}_{}_{}.json'.format(output_path,'SearchPolicyPerlifeByPolicy',p,c,'Resp',curDt)
            else: 
                oFileName = '{}{}_pol_{}_{}_{}.json'.format(output_path,'SearchPolicyPerlifeByPolicy',p,'Resp',curDt)
            with io.open(oFileName,'a',encoding='utf8') as o:
                count += 1
                print('###{}###'.format(count))
                json_data_str = '{"policyNo":"'+p+'"'+cert_param+',"relationShip":"I","companyId":"1"' + dedupe_mode + '}'
                url_data = {'url': url, 'data': json_data_str }
                get_url = '{url}?json={data}'.format(**url_data)
                request_data = 'request:{}'.format(get_url)
                write_output_file(o,'/*',True)
                write_output_file(o,request_data,True)
                r = requests.get(get_url, verify=False, headers=req_headers)
                response_code = '-------------response:{}-------------'.format(r.status_code)
                write_output_file(o,response_code,True)
                output = r.json()
                policyPerlifeList = output['policyPerlifeList']
                if 'policyPerlifeList' in output:
                    write_output_file(o,'policy per life size {}'.format(len(policyPerlifeList)), True)    
                    for policy in policyPerlifeList:
                        covNum = policy['covNum']
                        partyId = policy['partyId']
                        dash = '------------'
                        if covNum == 'MEM':
                            dash = ''
                        write_output_file(o,'{}covNum {}, partyId {} '.format(dash, covNum, partyId),True)
                else:
                    print('policyPerlifeList is null')    
                write_output_file(o,'*/',True)
                parsed = json.dumps(r.json(), indent=4) 
                write_output_file(o,parsed,True)
        except Exception as e:
            print(e)
            break
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