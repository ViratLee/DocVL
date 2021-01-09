import requests, json, io, datetime, configparser, base64, codecs
config = configparser.ConfigParser()
config.read('cmic_config.ini')
cmic_config = config['sit']
url = cmic_config['webservices.360.url']
req_headers = { 
    'Authorization': '{} {}'.format(cmic_config['webservices.360.user.auth'], cmic_config['webservices.360.user.password']),
    #'Authorization': '{} {}'.format(cmic_config['webservices.360.user.auth'], base64_auth),
    'User-Agent':'Mozilla/5.0'
}
url = '{}/{}'.format(url,'sonora/cmicrest/queries/doquery')
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

def buildPostData():
    my_data = {
        "queryName": "getOutstandingWork",
        "params": [{
                    "key": "LOGINID_USER",
                    "value": "mclm022"
                 },
                 {
                    "key": "TOTALWORKTIME",
                    "value": "90"
                 },
                 {
                    "key": "TOTALWORKTIMETO",
                    "value": ""
                 }
        ],
        "rowPerPages": 2147483647,
        "startPage": 1
    }
    return my_data  
    
def callService():
    try:
        oFileName = '{}{}_{}_{}.json'.format(output_path,'360_doquery','Resp',curDt)
        with io.open(oFileName,'a',encoding='utf-8') as o:            
            payload = buildPostData()
            url_data = {'url': url, 'data': payload }
            post_url = '{url}:payload={data}'.format(**url_data)
            request_data = 'post request:{}'.format(post_url)
            write_output_file(o,'/*',True)
            write_output_file(o,request_data,True)
            r = requests.post(url, verify=False, headers=req_headers, json=payload)
            response_code = '-------------response:{}-------------'.format(r.status_code)
            write_output_file(o,response_code,True)
            write_output_file(o,'*/',True)
            parsed = json.dumps(r.json(),ensure_ascii=False, indent=4) 
            write_output_file(o,parsed,True)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    callService()