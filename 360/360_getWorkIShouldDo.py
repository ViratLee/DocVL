import requests, json, io, datetime, configparser, base64, codecs
config = configparser.ConfigParser()
config.read('../notebooks/cmic_config.ini')
cmic_config = config['uat']
#print('{} {}'.format(cmic_config['user.auth'], cmic_config['user.password']))
url = cmic_config['webservices.360.url']
#user_name = 'bclm022'
#password = 'bclm022'
#auth = user_name + ":" + password
#print('auth:{}'.format(auth))
#encode_auth = auth.encode('utf-8')
#print('encode_auth:{}'.format(encode_auth))
#base64_auth = base64.b64encode(encode_auth)
#print('base64_auth:{}'.format(base64_auth))
req_headers = { 
    'Authorization': '{} {}'.format(cmic_config['webservices.360.user.auth'], cmic_config['webservices.360.user.password']),
    #'Authorization': '{} {}'.format(cmic_config['webservices.360.user.auth'], base64_auth),
    'User-Agent':'Mozilla/5.0'
}
url = '{}/{}'.format(url,'sonora/cmicrest/workflow/getNextWork') 
#case_id_list = ['1128080'] #uat
case_id_list = ['2710180'] #prod

def write_output_file(o, line, printoutput=False):
    try:
        if printoutput == True:
           text = '{}'.format(line)
           print(text)
        o.write(line)
        o.write("\n")
    except IOError:
        raise
count = 0
now = datetime.datetime.now()
curDt = '{:%Y-%m-%d_%H%M}'.format(now)
output_path = cmic_config['output.path']
for case_id in case_id_list:
    try:
        count += 1
        oFileName = '{}{}_{}_{}_{}.json'.format(output_path,'getClaimInfo',case_id,'Resp',curDt)
        with io.open(oFileName,'a',encoding='utf8') as o:
            print('###{}###'.format(count))
            url_data = {'url': url, 'data': case_id }
            get_url = '{url}/{data}'.format(**url_data)
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
            code = output['code']
            print('code:{}'.format(code))
            data = output['data']
            jsonData = data['jsonData']
            #print('json:{}'.format(jsonData))
            decode_text = base64.b64decode(jsonData)
            print('byte b64decode:{}'.format(decode_text))
            #print('decode-utf-8:{}'.format(decode_text.decode('utf-8','ignore')))
           # print('{}'.format(decode_text.decode('UTF-8','backslashreplace')))
            #str = decode_text.decode(UTF-8','ignore')
            #print('{}'.format(str))
    except Exception as e:
        print(e)
        break