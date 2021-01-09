import requests, json, io, datetime, configparser
config = configparser.ConfigParser()
config.read('cmic_config.ini')
cmic_config = config['local']
url = cmic_config['cmic.web.path']
req_headers = { 
    'Authorization': '{} {}'.format(cmic_config['user.auth'], cmic_config['user.password']),
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
url = '{}/{}'.format(url,'CMiC/api/external/hcinternet/ICD10CodeList') 
now = datetime.datetime.now()
curDt = '{:%Y-%m-%d_%H%M}'.format(now)
output_path = cmic_config['output.path']
try:
    oFileName = '{}{}_{}_{}.json'.format(output_path,'HC-ICD10CodeList','Resp',curDt)
    with io.open(oFileName,'a',encoding='utf8') as o:
        request_data = 'request:{}'.format(url)
        write_output_file(o,'/*',True)
        write_output_file(o,request_data,True)
        r = requests.get(url,  headers=req_headers,verify=False)
        response_code = '-------------response:{}-------------'.format(r.status_code)
        write_output_file(o,response_code,True)
        write_output_file(o,'*/',True)
        parsed = json.dumps(r.json(), indent=4) 
        write_output_file(o,parsed,False)
except Exception as e:
    print(e)