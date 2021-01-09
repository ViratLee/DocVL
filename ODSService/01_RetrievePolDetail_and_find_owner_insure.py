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
#dedupe_mode = ', "dedupeMode":"partyDedupe"'
dedupe_mode = ''
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
url = '{}/{}'.format(url,'rest/AIAService/policy/retrievePolicy/RetrievePolicyDetail') 
#policy_list =['U881138502','P051080422']
#policy_list =['T303726971']
#policy_list = ['P014153008']
#policy_list = ['T075599355','T002283922']
#policy_list = ['T130230928']
#policy_list = ['T060434784','P318745918','P403550364','T080489599','T111906271','T990560595']

#policy_list = ['02342'] #GPSE
#policy_list = ['07233:2007000090:00'] #GPSE
#polNum : "02104:1998000090:00"
#policy_list = ['01180:2003000070:00'] #GPSE
#policy_list = ['02104:1998000090:00'] #GPSE
#policy_list = ['02104:1999000580:00'] #GPSE
#policy_list = ['01180:2003000070:00'] #GPSE
#policy_list = ['02104100'] #GPSE
#policy_list = ['08339:2016000013:00'] #GPSE
#policy_list = ['02310:2004000350:00'] #GPSE
#policy_list = ['02310118'] #GPSE
#policy_list = ['T183115498','T186104642','T155202643','T122254064','T140401792','T175660294','T170952033']
#policy_list = ['T123747059']
#policy_list = ['T205950256']
#policy_list = ['T205950201']
#policy_list = ['T205950201']
#policy_list = ['T680711683','U890902745','U890901225','T680705961','U890904264','T690105179']
#policy_list = ['T680711683','T680705961'] #HNW
#policy_list = ['T205950230','T206016526','T206016555'] #HNW
#policy_list = ['T205950065','T205953635'] #HNW
#policy_list = ['T680711683','T680705961'] #HNW
#policy_list = ['P103486644']
#policy_list = ['T157200520','P024881975']
#policy_list = ['T156283182','P062428594']
#policy_list = ['T141458676','T157200520','P024881975','T156283182','P062428594','P024881975','T162665684','P062428594']
#policy_list = ['T157200520','T162664025','P253058346','P024881975','T220205274','T213075547','T080801410','T141458676','T156283182','T220992053','T110516497','P062428594','T162665684']
#policy_list = ['T221526059']
#policy_list = ['T214919000','P253742416','T218963007','T221526059','T214687688','T215701259']
#uat hshp 
#policy_list = ['T456193066','T456193354']
#policy_list = ['T410230949'] #preauth, prd
#policy_list = ['U881426599'] #preauth, prd
#policy_list = ['T217624295','U882611028']#,#'T221622157','T221622076','U882608811','T220649982']
#prod
#policy_list = ['T165814283']
policy_list = ['P402063331']
#nwh
#T205950308
#T205949898/990D07
def findFieldInPolicy(policy):
    polNum = policy['polNum']
    effDt = policy['effDt']
    eftEndDt = policy['eftEndDt']
    message = (
        f"polNum :{policy['polNum']}, "
        f"productCd :{policy['productCd']}, "
        f"effDt :{policy['effDt']}, "
        f"eftEndDt :{policy['eftEndDt']}"
    )
    print(message)

# def findCoverageList(policy):
#     coverageList = policy['coverageList']
#     for(coverageList )
#     ProductCd

now = datetime.datetime.now()
curDt = '{:%Y-%m-%d_%H%M}'.format(now)
output_path = cmic_config['output.path']
count = 0
for policy_number in policy_list:
    try:
        count += 1
        oFileName = '{}{}_{}_{}_{}.json'.format(output_path,'RetrievePolicyDetail',policy_number.replace(':','_'),'Resp',curDt)
        with io.open(oFileName,'a',encoding='utf8') as o:
            #input("Press any key to continue...")
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
            parsed = json.dumps(r.json(),ensure_ascii=False, indent=4) 
            write_output_file(o,parsed,False)
            output = r.json()
            policyList = output['policyList']
            policy = policyList[0]
            #findFieldInPolicy(policy)

            policy_service = policyService(policy)
            policy_service.findInsureParty()
            policy_service.findOwnerPartyId()

            #policy_service.all_coverage()
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