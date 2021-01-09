import requests
import json
import io
import datetime
import configparser
config = configparser.ConfigParser()
config.read('cmic_config.ini')
cmic_config = config['local']
root_url = cmic_config['cmic.web.path']

req_headers = { 
    'Authorization': '{} {}'.format(cmic_config['user.auth'], cmic_config['user.password']),
    'content-type': 'application/json',
    'User-Agent':'Mozilla/5.0'
}
write_file = True
def write_output_file(o, line, printoutput=False):
    try:
        if printoutput == True:
           text = '{}'.format(line)
           print(text)
        o.write(line)
        o.write("\n")
    except IOError:
        raise

url = '{}/{}'.format(root_url,'CMiC/api/external/hcinternet/claimsBalance') 
now = datetime.datetime.now()
curDt = '{:%Y-%m-%d_%H%M}'.format(now)
output_path = cmic_config['output.path']

def claim_balance(post_data,o):
    write_output_file(o,url,write_file)
    print('sending...')
    r = requests.post(url, data=post_data.encode('utf-8'), headers=req_headers)
    response_code = '-------------response:{}-------------'.format(r.status_code)
    write_output_file(o,response_code,write_file)
    parsed = json.dumps(r.json(), indent=4) 
    write_output_file(o,parsed,write_file)
 
def readJsonDataAsText(file_data):
    print('readJson')
    with open(file_data,encoding='utf-8') as f:
        content = f.read()
    return content    

if __name__ == '__main__':
    #json_file = "sm_claim_balance_0000014917.json"
    #json_file = "sm_claim_balance_P331561344.json"
    json_file = "sm_claim_balance_P093502984.json"
    p_dat = readJsonDataAsText(json_file)
    try:
        oFileName = '{}{}_{}_{}.json'.format(output_path,'HC-claimbalance','Resp',curDt)
        with io.open(oFileName,'a',encoding='utf8') as o:
            claim_balance(p_dat,o)
    except Exception as e:
        print(e)