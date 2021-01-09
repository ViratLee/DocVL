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

def search_document(req_data):
    url = cmic_config['cmic.web.path']
    now = datetime.datetime.now()
    curDt = '{:%Y-%m-%d_%H%M}'.format(now)
    output_path = cmic_config['output.path']#http://localhost:8080/CMiC/api/rest/claim/documentRecordSearch
    url = '{}/{}'.format(url,'CMiC/api/rest/claim/documentRecordSearch')
    post_url = {'url': url, 'data': req_data }
    request_data = 'post request:{}'.format(post_url)
    oFileName = '{}_{}_{}.json'.format(output_path,'documentRecordSearch',curDt)
    with io.open(oFileName,'a',encoding='utf-8') as o:
        write_output_file(o,'/*',True)
        #write_output_file(o,request_data,True)
        print('sending...')
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
        data = response['data']
        totalCase = data[0]["totalCase"]
        print(f'total case {totalCase}')
    return parsed

def search_cmic_document(req_data,rest_path):
    url = cmic_config['cmic.web.path']
    now = datetime.datetime.now()
    curDt = '{:%Y-%m-%d_%H%M}'.format(now)
    output_path = cmic_config['output.path']#http://localhost:8080/CMiC/api/rest/claim/documentRecordSearch
    url = '{}/{}'.format(url,rest_path)
    post_url = {'url': url, 'data': req_data }
    request_data = 'post request:{}'.format(post_url)
    print('sending...')
    print(request_data)
    r = requests.post(url, data=req_data.encode('utf-8'), headers=req_headers)
    response_code = '-------------response:{}-------------'.format(r.status_code)
    print(response_code)
    if r.status_code != 200:
        print('exit')
        return
    parsed = json.dumps(r.json(), indent=4) 
    print(parsed)
    response = r.json()
    data = response['data']
    total =response['total']
    print(f'total case {total}')
    
if __name__ == '__main__':
    json1 = 'document_record_search_req.json'
    json2 = 'iclaim_document_record_search_req2.json'
    req_data = readJsonDataAsText(json1)
    #search_document(req_data)
    document_search_path = 'CMiC/api/rest/claim/documentRecordSearch'
    iClaim_document_search_path = 'CMiC/api/rest/claim/iClaimDocumentRecordSearch'
    #search_cmic_document(req_data2,iClaim_document_search_path)
    search_cmic_document(req_data,document_search_path)