import requests
import json
import io
import datetime
import configparser

config = configparser.ConfigParser()
config.read('cmic_config.ini')
cmic_config = config['local']
req_headers = { 
    'Authorization': '{} {}'.format(cmic_config['user.auth'], cmic_config['user.password']),
    'Content-Type': 'application/json',
    'User-Agent':'Mozilla/5.0'
}

def submit_claim(post_data):
    url = cmic_config['webservices.rest.url']
    now = datetime.datetime.now()
    curDt = '{:%Y-%m-%d_%H%M}'.format(now)
    output_path = cmic_config['output.path']
    url = '{}/{}'.format(url,'CMiC/api/rest/utility/submitClaim')
    print(url)
    print('sending...')
    r = requests.post(url, data=post_data.encode('utf-8'), headers=req_headers)
    response_code = '-------------response:{}-------------'.format(r.status_code)
    print(response_code)
    parsed = json.dumps(r.json(), indent=4) 
    print(parsed)

def readJsonDataAsText(file_data):
    print('readJson')
    with open(file_data,encoding='utf-8') as f:
        content = f.read()
    return content    

if __name__ == '__main__':
    #json_file = readJsonDataAsText("sm_submit_claim_0000012749_treament_5_edi.json")
    #p_dat1 = readJsonDataAsText("sm_submit_claim_0000012749_treament_5_nonedi.json")
    #p_dat = readJsonDataAsText("sm_submit_claim_P250309425_treament_4_nonedi.json")
        #"hospitalizationDate" : "2019-08-05T00:00:00.000Z",
    #p_dat = readJsonDataAsText("sm_submit_claim_IB_P252894695_treament_4_edi.json")    
    #json_file = "sm_submit_claim_IB_T178018380_treament_1.json"
    #json_file = "sm_submit_claim_P601480663_treament_4.json"
    #json_file = "sm_submit_claim_0000012749_treament_5_edi.json"
    #json_file = "sm_submit_claim_0000011144_treament_5_nonedi.json"
    #json_file = "sm_submit_claim_0000011144_treament_5.json"
    json_file = "sm_submit_claim_T167215411_treament_1.json"
    #json_file = "sm_submit_claim.json"
    p_dat = readJsonDataAsText(json_file)
    #today = datetime.datetime.now()
    
    #yesterday = today - datetime.timedelta(days = 260)
    #tomorrow = today + datetime.timedelta(days = 1) 
    #set today
    #cur_dt = '{:%Y-%m-%d}T00:00:00.000Z'.format(today)#20190820
    #cur_dt = '{:%Y-%m-%d}T00:00:00.000Z'.format(yesterday)#20190820
    #date_dt = '{:%y.%m.%d}'.format(now)#19.08.20
    # print(type(p_dat))
    # p_dat_json = json.loads(p_dat)
    # p_dat_json['accidentDt'] = cur_dt
    # p_dat_json['consultationDt'] = cur_dt
    # p_dat_json['hospitalizationDate'] = cur_dt
    # p_dat_str = json.dumps(p_dat_json, indent=4)
    # print(type(p_dat_json))
    print(p_dat)
    submit_claim(p_dat)