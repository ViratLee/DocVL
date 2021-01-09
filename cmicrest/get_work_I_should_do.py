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

def get_work_by_page_v1(req_data,page):
    url = cmic_config['cmic.web.path']
    now = datetime.datetime.now()
    curDt = '{:%Y-%m-%d_%H%M}'.format(now)
    output_path = cmic_config['output.path']#http://localhost:8080/CMiC/api/rest/getWorkIShouldDo/{page}
    url = '{}/{}/{}'.format(url,'CMiC/api/rest/getWorkIShouldDo',page)
    post_url = {'url': url, 'data': req_data }
    request_data = 'post request:{}'.format(post_url)
    oFileName = '{}{}_{}_{}.json'.format(output_path,'getWorkIShouldDo',page,curDt)
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
    return r

def get_work_by_page_v2(req_data,page):
    url = cmic_config['cmic.web.path']
    now = datetime.datetime.now()
    curDt = '{:%Y-%m-%d_%H%M}'.format(now)
    output_path = cmic_config['output.path']#http://localhost:8080/CMiC/api/rest/getWorkIShouldDo/{page}
    url = '{}/{}/{}'.format(url,'CMiC/api/rest/getWorkIShouldDo',page)
    post_url = {'url': url, 'data': req_data }
    request_data = 'post request:{}'.format(post_url)
    print('sending...')
    r = requests.post(url, data=req_data.encode('utf-8'), headers=req_headers)
    response_code = '-------------response:{}-------------'.format(r.status_code)
    if r.status_code != 200:
        print('exit')
        return
    countwork(r)
    return r

def countwork(r):
	response_data = r.json()
	data = response_data['data']
	work_length = len(data)
	print(f'{work_length}')

if __name__ == '__main__':
	req_data = readJsonDataAsText('get_work_I_should_do_req.json')
	get_work_by_page_v2(req_data,'PreAuthMedical')