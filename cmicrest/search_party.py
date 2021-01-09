import sys, requests, json, io, datetime, json#configparser, json
import yaml

def load_yaml_config():
    with open('cmic_config.yaml', 'r') as f:
        yaml_file = yaml.safe_load(f)
        return yaml_file

config = load_yaml_config()
cmic_config = config['local']
req_headers = { 
    'Authorization': '{} {}'.format(cmic_config['user.auth'], cmic_config['user.password']),
    'Content-Type': 'application/json',
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

def readJsonDataAsText(jsonkey):
    #with open(data_sumit['case_validate_json'],encoding='utf-8') as f:
    with open(jsonkey,encoding='utf-8') as f:
        content = f.read()
    #print(type(content))
    #print(content)
    return content

def search_party(req_data):
    url = cmic_config['cmic.web.path']
    now = datetime.datetime.now()
    curDt = '{:%Y-%m-%d_%H%M}'.format(now)
    output_path = cmic_config['output.path']#http://localhost:8080/CMiC/api/rest/claim/documentRecordSearch
    url = '{}{}'.format(url,'/CMiC/api/rest/party/searchParty')
    post_url = {'url': url, 'data': req_data }
    request_data = 'post request:{}'.format(post_url)
    oFileName = '{}_{}_{}.json'.format(output_path,'searchParty',curDt)
    with io.open(oFileName,'a',encoding='utf-8') as o:
        write_output_file(o,'/*',True)
        #write_output_file(o,request_data,True)
        print(f'sending...{url}')
        r = requests.post(url, data=req_data.encode('utf-8'), headers=req_headers)
        response_code = '-------------response:{}-------------'.format(r.status_code)
        write_output_file(o,response_code,True)
        write_output_file(o,'*/',True)
        if r.status_code != 200:
            print('exit')
            return
        parsed = json.dumps(r.json(), indent=4) 
        write_output_file(o, parsed, False)
        response = r.json()
        list_policy(response['data'])
    return parsed

def search_party2(req_data):
    url = cmic_config['cmic.web.path']
    now = datetime.datetime.now()
    curDt = '{:%Y-%m-%d_%H%M}'.format(now)
    output_path = cmic_config['output.path']#http://localhost:8080/CMiC/api/rest/claim/searchParty
    url = '{}{}'.format(url,'/CMiC/api/rest/party/searchParty')
    post_url = {'url': url, 'data': req_data }
    request_data = 'post request:{}'.format(post_url)
    print(f'sending...{url}')
    r = requests.post(url, data=req_data.encode('utf-8'), headers=req_headers)
    response_code = '-------------response:{}-------------'.format(r.status_code)
    if r.status_code != 200:
        print('exit')
        return
    parsed = json.dumps(r.json(), indent=4) 
    response = r.json()
    list_policy(response['data'])
    return parsed

def list_policy(dataList):
    for data in dataList:
        print(f'partyId: {data["partyId"]}, policyNo: {data["policyNo"]}')
    

if __name__ == '__main__':
    #pols = ['T205950492','T205950308','T205953813','T205953813','T205953813','T205953813','T205950405','T205951129','T205950625','T205950531']
    #pols = ['T205950528','T205950492','T143362317','T206016597','T206016607','T090292132','T206016610','T206016610','T206016526','T206016555']
    #pols = ['T205950230','T205950298','T206016584','T205950298','T206016584','T205950298','T206016584','T205950298','T206016584','T205950256']
    #pols = ['T205950201','T205950201','T205950256','T205950201','T205950256','T206016607','T206016584','T205950298','T206016584','T205950298']
    #pols = ['T205950065','T206016571','T205950269','T205950256','T205950201','T205950201','T205950256','T205950256','T205950201','T205950201']
    #pols = ['T205950256','T205950256','T205950201','T206016607','T205950256','T205950201','T205950201','T205950256','T205950256','T205950201']
    pols = ['T205950256','T205950201','T205950201','T205950256','T205950256','T205950201','T205950201','T205950256','T205950201','T205950256']
    count = 0
    for pol in pols:
        req_data = readJsonDataAsText('search_party_req.json')
        json_req_data = json.loads(req_data)
        count = count + 1
        print(f'count {count}')
        update_data = {"policyNumber": pol}
        json_req_data.update(update_data)
        req_data = json.dumps(json_req_data, indent=4)
        search_party2(req_data)
        input()