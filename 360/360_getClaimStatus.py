import requests, json, io, datetime, base64, codecs #configparser, 
import yaml

def load_yaml_config():
    with open('cmic_config.yaml', 'r') as f:
        yaml_file = yaml.safe_load(f)
        #pp.pprint(yaml_file)
        return yaml_file

# config = configparser.ConfigParser()
# config.read('cmic_config.ini')
config = load_yaml_config()
cmic_config = config['sit']
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
url = '{}/{}'.format(url,'sonora/cmicrest/workflow/getClaimStatus') 
#case_id_list = ['1128189','1128244'] #uat
#case_id_list = ['16796'] #prod
#case_id_list = ['1128265','1128269','1128270'] #uat
#case_id_list = ['1128277'] #uat
#case_id_list = ['7143786'] 
#case_id_list = ['1139015','1139014'] 
#case_id_list = ['18921','18924','18925'] # deduct case
#case_id_list = ['6831714'] #prod  4232711 
#case_id_list = ['17108'] #sit
#case_id_list = ['1140266']

# sit life case
#case_id_list = ['19065']
#hnw case ###
#case_id_list = ['19038','19056','19057','19058']
#case_id_list = ['19658']#,'19625','19628']
#case_id_list = ['7676577','7676600','7678646','7682010','7682049','7682071','7682104','7688305','7689091','7691608']
#case_id_list = ['1142434','1142435']'
#case_id_list = ['19993','20073','19958']
#case_id_list = ['1151271','1145153']
#case_id_list = ['1134381']
#case_id_list = ['9167342'] #1136338
case_id_list = ['20641']


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
        oFileName = '{}{}_{}_{}_{}.json'.format(output_path,'getClaimStatus',case_id,'Resp',curDt)
        with io.open(oFileName,'a',encoding='utf8') as o:
            print('###{}###'.format(count))
            url_data = {'url': url, 'data': case_id }
            get_url = '{url}/{data}'.format(**url_data)
            request_data = 'request:{}'.format(get_url)
            write_output_file(o,'/*',True)
            write_output_file(o,request_data,True)
            r = requests.get(get_url,  headers=req_headers, verify=False)
            print(type(r))
            response_code = '-------------response:{}-------------'.format(r.status_code)
            write_output_file(o,response_code,True)
            write_output_file(o,'*/',True)
            parsed = json.dumps(r.json(), indent=4) 
            write_output_file(o,parsed,True)
            output = r.json()
            code = output['code']
            print('code:{}'.format(code))
            #print('decode-utf-8:{}'.format(decode_text.decode('utf-8','ignore')))
           # print('{}'.format(decode_text.decode('UTF-8','backslashreplace')))
            #str = decode_text.decode(UTF-8','ignore')
            #print('{}'.format(str))
    except Exception as e:
        print(e)
        break