import requests, json, io, datetime, configparser
config = configparser.ConfigParser()
config.read('cmic_config.ini')
cmic_config = config['local']
#url = cmic_config['webservices.rest.url']
url = cmic_config['cmic.web.path']

req_headers = { 
    'Authorization': '{} {}'.format(cmic_config['user.auth'], cmic_config['user.password']),
    'content-type': 'application/json',
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
url = '{}/{}'.format(url,'CMiC/api/external/hcinternet/getFurtherClaim') 
now = datetime.datetime.now()
curDt = '{:%Y-%m-%d_%H%M}'.format(now)
output_path = cmic_config['output.path']
try:
    #payload = '{"partyId": "249687410","accidentDt": "2018-10-05"}'
    payload = '{"partyId":"380936279","accidentDt":"2020-01-12","treatmentType":"4"}'
    oFileName = '{}{}_{}_{}.json'.format(output_path,'HC-getFurtherClaim','Resp',curDt)
    with io.open(oFileName,'a',encoding='utf8') as o:
        #url_data = {'url': url, 'data': payload }
        #get_url = '{url}?{data}'.format(**url_data)
        #request_data = 'request:{}'.format(get_url)
        write_output_file(o,'/*',True)
        write_output_file(o,url,True)
        r = requests.post(url,data=payload,  headers=req_headers,verify=False)
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