import requests, json, io, datetime
#configparser, base64, codecs, sys
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
url = '{}/{}'.format(url,'sonora/cmicrest/workflow/getClaimInfo') 
#case_id_list = ['1128984'] #uat
#case_id_list = ['3416654'] #prod
#case_id_list = ['5068338'] #
#case_id_list = ['1130834']
#case_id_list = ['1135778']
#case_id_list = ['19419', '19420']
#case_id_list = ['19550','19551','19552']
#case_id_list = ['8044950','8073489']
#case_id_list = ['1144395','1144396','1144397','1144398','1144400']
case_id_list = ['9344181']
#case_id_list = ['7676577','7676600','7678646','7682010','7682049','7682071','7682104','7688305','7689091','7691608']
count = 0
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

# for case_id in case_id_list:
#     try:
#         count += 1
#         oFileName = '{}{}_{}_{}_{}.json'.format(output_path,'getClaimInfo',case_id,'Resp',curDt)
#         with io.open(oFileName,'a',encoding='utf-8') as o:
#             print('###{}###'.format(count))
#             url_data = {'url': url, 'data': case_id }
#             get_url = '{url}/{data}'.format(**url_data)
#             request_data = 'request:{}'.format(get_url)
#             write_output_file(o,'/*',True)
#             write_output_file(o,request_data,True)
#             r = requests.get(get_url,  headers=req_headers, verify=False)
#             response_code = '-------------response:{}-------------'.format(r.status_code)
#             write_output_file(o,response_code,True)
#             write_output_file(o,'*/',True)
#             parsed = json.dumps(r.json(),ensure_ascii=False, indent=4) 
#             write_output_file(o,parsed,True)
            # output = r.json()
            # jsonData = output['data']['jsonData']
            # decode_text = base64.b64decode(jsonData)
            # print('---------------------------------------------')
            # print(decode_text)
            # claim_info = decode_text.decode('UTF-8', errors='ignore')
            # print('---------------------------------------------')
            # print(claim_info)
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
    # except Exception as e:
    #     print(e)
    #     break
def get_claiminfo1():
    for case_id in case_id_list:
        try:
            global count
            count += 1
            oFileName = '{}{}_{}_{}_{}.json'.format(output_path,'getClaimInfo',case_id,'Resp',curDt)
            with io.open(oFileName,'a',encoding='utf-8') as o:
                print(f'###{count}###')
                url_data = {'url': url, 'data': case_id }
                get_url = '{url}/{data}'.format(**url_data)
                request_data = 'request:{}'.format(get_url)
                write_output_file(o,'/*',True)
                write_output_file(o,request_data,True)
                r = requests.get(get_url, headers=req_headers, verify=False)
                response_code = '-------------response:{}-------------'.format(r.status_code)
                write_output_file(o,response_code,True)
                write_output_file(o,'*/',True)
                parsed = json.dumps(r.json(), ensure_ascii=False, indent=4) 
                write_output_file(o,parsed,True)
                # output = r.json()
                # jsonData = output['data']['jsonData']
                # decode_text = base64.b64decode(jsonData)
                # print('---------------------------------------------')
                # print(decode_text)
                # claim_info = decode_text.decode('UTF-8', errors='ignore')
                # print('---------------------------------------------')
                # print(claim_info)
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
def cmic_phase_type(phase_type):
    phase_type_no = ""
    if phase_type == 'Admission':
        phase_type_no = "01"
    elif phase_type == 'Discharge':
        phase_type_no = "02"
    return phase_type_no;

def get_claiminfo2():
    for case_id in case_id_list:
        try:
            print('###{}###'.format(case_id))
            url_data = {'url': url, 'data': case_id }
            get_url = '{url}/{data}'.format(**url_data)
            #request_data = 'request:{}'.format(get_url)
            #write_output_file(o,'/*',True)
            #write_output_file(o,request_data,True)
            r = requests.get(get_url,  headers=req_headers, verify=False)
            #response_code = '-------------response:{}-------------'.format(r.status_code)
            res = r.json()
            data = res['data']
            #print(f" requestOriginal:{data['requestOriginal']}")
            message = (
                f"case id:{data['caseId']},"
                #f"party id:{data['partyId']},"
                #f"policyNo :{data['policyNo']},"
                #f" phase :{cmic_phase_type(data['phase'])} - {data['phase']},"
                #f" edi:{data['edi']},"
                #f" ediInd:{data['ediInd']},"
                #f" stp:{data['stp']},"
                f" assessResult:{data['assessResult']},"
                f" activity:{data['activity']},"
                f" owner:{data['owner']},"
                f" ai:{data['ai']},"
                f" ipdOpd:{data['ipdOpd']},"
                f" risk:{data['risk']},"
                f" requestOriginal:{data['requestOriginal']}"
            )
            print(message)
        except Exception as e:
            #print(e)
            break

if __name__ == '__main__':
    count = 0
    get_claiminfo1()