import requests, json, io, datetime, configparser, base64, codecs, sys
config = configparser.ConfigParser()
config.read('cmic_config.ini')
cmic_config = config['uat']
url = cmic_config['webservices.360.url']
req_headers = { 
    'Authorization': '{} {}'.format(cmic_config['webservices.360.user.auth'], cmic_config['webservices.360.user.password']),
    #'Authorization': '{} {}'.format(cmic_config['webservices.360.user.auth'], base64_auth),
    'User-Agent':'Mozilla/5.0'
}
url = '{}/{}'.format(url,'sonora/cmicrest/user/getUserInfo') 
user_id_list = ['M'] #uat
#user_id_list = ['2714106'] #prod

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
for user_id in user_id_list:
    try:
        count += 1
        oFileName = '{}{}_{}_{}_{}.json'.format(output_path,'getUserInfo',user_id,'Resp',curDt)
        with io.open(oFileName,'a',encoding='utf8') as o:
            print('###{}###'.format(count))
            url_data = {'url': url, 'data': user_id }
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
            #claim_info = jsonData.decode(decoding='UTF-8',errors='strict')
            #decode_text = base64.b64decode(jsonData)
            #print(decode_text)
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