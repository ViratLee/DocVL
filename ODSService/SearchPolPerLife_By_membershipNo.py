import requests, json, io, datetime#, configparser
import yaml
def load_yaml_config():
    with open('cmic_config.yaml', 'r') as f:
        yaml_file = yaml.safe_load(f)
        #pp.pprint(yaml_file)
        return yaml_file

config = load_yaml_config()
# config = configparser.ConfigParser()
# config.read('cmic_config.ini')
cmic_config = config['uat']
#print('{} {}'.format(cmic_config['user.auth'], cmic_config['user.password']))
url = cmic_config['webservices.rest.url']
req_headers = { 
    'Authorization': '{} {}'.format(cmic_config['user.auth'], cmic_config['user.password']),#;'Basic QkFQUEVTQjpLbjR5SWFnQEtx', # UAT
    'User-Agent':'Mozilla/5.0'
}
url = '{}/{}'.format(url,'rest/AIAService/policy/searchPolicy/SearchPolicyPerlifeByMembershipNo') 
#membership_no_cert_list ={'0191407316': '0000085360'}
membership_no_cert_list ={'3020033102': '01711790'}
now = datetime.datetime.now()
curDt = '{:%Y-%m-%d_%H%M}'.format(now)
output_path = cmic_config['output.path']
pol_uniq = set()
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
    for mem_no, c in membership_no_cert_list.items():
        try:
            cert_param = ''
            if c:
                cert_param = ',"certificateNum":"{}"'.format(c)
                oFileName = '{}{}_pol_{}_cert_{}_{}_{}.json'.format(output_path,'SearchPolicyPerlifeByMembershipNo',mem_no,c,'Resp',curDt)
            else: 
                oFileName = '{}{}_pol_{}_{}_{}.json'.format(output_path,'SearchPolicyPerlifeByMembershipNo',mem_no,'Resp',curDt)
            with io.open(oFileName,'a',encoding='utf8') as o:
                count += 1
                print('###{}###'.format(count))
                json_data_str = '{"membershipNo":"'+mem_no+'"'+cert_param+',"relationShip":"I","companyId":"1"}'
                url_data = {'url': url, 'data': json_data_str }
                get_url = '{url}?json={data}'.format(**url_data)
                request_data = 'request:{}'.format(get_url)
                write_output_file(o,'/*',True)
                write_output_file(o,request_data,True)
                r = requests.get(get_url,  headers=req_headers, verify=False)
                response_code = '-------------response:{}-------------'.format(r.status_code)
                write_output_file(o,response_code,True)
                write_output_file(o,'*/',True)
                parsed = json.dumps(r.json(), indent=4) 
                write_output_file(o,parsed,True) 
                output = r.json()
                policyPerlifeList = output['policyPerlifeList']
                write_output_file(o,'/*',True)
                if 'policyPerlifeList' in output:
                    write_output_file(o,'policy per life size {}'.format(len(policyPerlifeList)), True)    
                    for policy in policyPerlifeList:
                        covNum = policy['covNum']
                        partyId = policy['partyId']
                        polNum = policy['polNum']
                        dash = '------------'
                        if covNum == 'MEM':
                            dash = ''
                        write_output_file(o,'{}covNum {}, partyId {}, polNum {}'.format(dash, covNum, partyId, polNum),True)
                        pol_uniq.add(polNum)
                else:
                    print('policyPerlifeList is null')
                write_output_file(o,'print unique policy', True)
                for policy_number in pol_uniq:
                    write_output_file(o,' polNum {}'.format(polNum),True)
                write_output_file(o,'*/',True)
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