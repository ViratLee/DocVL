import sys, requests, json, io, datetime, configparser, json
import yaml
req_headers = {
    'Authorization': '',
    'User-Agent':'Mozilla/5.0',
    'Content-Type': 'application/json'
}
#"policyNo": "T206016607"
post_data = """
{
    "batchNo": "",
    "policyNo": "00000A4270",
    "providerCode": "",
    "dischargeDateFrom": null,
    "dischargeDateTo": null,
    "typeOfTreatment": "",
    "aiStatus":"10", 
    "page": 1,
    "pageSize": 65535
}
"""
post_data2 = """
{
    "batchNo": "02563071102",
    "policyNo": "00000M0872",
    "providerCode": "1001390001",
    "dischargeDateFrom": "2020-10-31T17:00:00.000Z",
    "dischargeDateTo": "2020-11-09T17:00:00.000Z",
    "typeOfTreatment": "2",
    "aiStatus": "10",
    "page": 1,
    "pageSize": 65535
}
"""
# use safe_load instead load
def load_yaml_config():
    with open('cmic_config.yaml', 'r') as f:
        yaml_file = yaml.safe_load(f)
        #pp.pprint(yaml_file)
        return yaml_file

def write_output_file(o, line, printoutput=False):
    try:
        if printoutput == True:
           text = '{}'.format(line)
           print(text)
        o.write(line)
        o.write("\n")
    except IOError:
        raise

def search(url,data):
    print(f'sending... {url}')
    #search_data = json.dumps(data, indent=4)
    #print(type(data))
    print("----request-----")
    print(data)
    # search_data = json.loads(data)
    # print(type(search_data))
    # print(search_data)
    # search = json.dumps(search_data, indent=4)
    # print(type(search))
    # print(search)
    r = requests.post(url, data=data.encode('utf-8'), headers=req_headers)
    #r = requests.post(url, data=search_data, headers=req_headers)
    response_code = '-------------response:{}-------------'.format(r.status_code)
    print(response_code)
    parsed = json.dumps(r.json(), indent=4) 
    print(parsed)
    if r.status_code == 200:
      return True
    else:
      return False    

now = datetime.datetime.now()#- datetime.timedelta(days=1)
today = '{:%Y-%m-%d}'.format(now)
submit_dt = '{}{}'.format(today,'T00:00:00.000Z')#"2019-03-06T17:00:00.000Z"

def readJsonDataAsText(jsonkey):
    #with open(data_sumit['case_validate_json'],encoding='utf-8') as f:
    with open(data_sumit[jsonkey],encoding='utf-8') as f:
        content = f.read()
    #print(type(content))
    #print(content)
    return content




if __name__ == '__main__':
    print('search billing')
    #url = cmic_config['cmic.web.path']
    cmic_config_data = load_yaml_config()
    local = cmic_config_data['local']
    req_headers['Authorization'] = '{} {}'.format(local['user.auth'], local['user.password'])
    url = local['cmic.web.path']
    url = '{}/{}'.format(url,'CMiC/api/rest/billing/search')
    search(url, post_data2)
    #http://localhost:8080/CMiC/api/rest/billing/search
    #requests.Request('POST', 'http://example.com', files=files).prepare().body.decode('ascii'))
