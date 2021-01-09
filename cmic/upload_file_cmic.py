import sys, requests, json, io, datetime, configparser, json
import pprint
import yaml
pp = pprint.PrettyPrinter(indent=4)
# config = configparser.ConfigParser()
# config.read('cmic_config.ini')
# cmic_config = config['local']
# req_headers = { 
#     'Authorization': '{} {}'.format(cmic_config['user.auth'], cmic_config['user.password']),
#     'Content-Type': 'multipart/form-data',
#     'User-Agent':'Mozilla/5.0'
# }

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

def settled(post_data):
    url = cmic_config['cmic.web.path']
    now = datetime.datetime.now()
    curDt = '{:%Y-%m-%d_%H%M}'.format(now)
    output_path = cmic_config['output.path']
    url = '{}/{}'.format(url,'CMiC/api/rest/claim/settleClaim')
    print(url)
    print('sending...')
    r = requests.post(url, data=post_data.encode('utf-8'), headers=req_headers)
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

def send_data_to_server(image_path, temperature):
    image_filename = os.path.basename(image_path)
    multipart_form_data = {
        'image': (image_filename, open(image_path, 'rb')),
        'temperature': ('', str(temperature)),
    }
    response = requests.post('http://www.example.com/api/v1/sensor_data/', files=multipart_form_data, headers=req_headers)
    print(response.status_code)

req_headers = {
    #'Authorization': '{} {}'.format(local['user.auth'], local['user.password']),
    'Content-Type': 'multipart/form-data',
    'User-Agent':'Mozilla/5.0'
}

if __name__ == '__main__':
    print('upload file')
    #url = cmic_config['cmic.web.path']
    cmic_config_data = load_yaml_config()
    local = cmic_config_data['local']
    req_headers['Authorization'] = '{} {}'.format(local['user.auth'], local['user.password'])
    url = local['cmic.web.path']
    url = '{}/{}'.format(url,'CMiC/api/rest/standardBilling/upload')
    #http://localhost:8080/CMiC/api/rest/standardBilling/upload
    print(url)
    #open('file.txt', 'wb')  # create an empty demo file
    files = {'file': open('D:\\BuildVersion.txt', 'rb')}
    r = requests.post(url,  files=files, headers=req_headers)
    response_code = '-------------response:{}-------------'.format(r.status_code)
    print(response_code)
   
    #requests.Request('POST', 'http://example.com', files=files).prepare().body.decode('ascii'))
