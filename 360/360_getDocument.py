import requests, json, io, datetime, configparser, base64, codecs, sys
config = configparser.ConfigParser()
config.read('cmic_config.ini')
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
url = '{}/{}'.format(url,'sonora/cmicrest/document/getDocument')

#case_id_list = ['1128984'] #uat
#case_id_list = ['3416654'] #prod
#case_id_list = ['5068338'] #
#case_id_list = ['1130834']
#case_id_list = ['1135778']
case_id_list = ['3561790']

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
        oFileName = '{}{}_{}_{}_{}.json'.format(output_path,'getDocument',case_id,'Resp',curDt)
        with io.open(oFileName,'a',encoding='utf-8') as o:
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
            parsed = json.dumps(r.json(),ensure_ascii=False, indent=4) 
            write_output_file(o,parsed,True)
            """
            output = r.json()
            jsonData = output['data']['jsonData']
            decode_text = base64.b64decode(jsonData)
            print('---------------------------------------------')
            print(decode_text)
            claim_info = decode_text.decode('UTF-8', errors='ignore')
            print('---------------------------------------------')
            print(claim_info)
            """
            #claim_info = jsonData.decode('windows-1252')
            #print(claim_info)
            #print(type(jsonData))
            #print('json:{}'.format(jsonData))
            #decode_text = base64.b64decode(jsonData)
            #print(decode_text)
            #print(type(decode_text))
            #claim_info = decode_text.decode('windows-1252')
            #print(claim_info)

            #print('byte b64decode:{}'.format(decode_text))
    except Exception as e:
        print(e)
        break