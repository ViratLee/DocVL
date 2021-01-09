import requests, json, io, datetime, configparser, base64, codecs
import pprint

pp = pprint.PrettyPrinter(indent=4)
config = configparser.ConfigParser()
config.read('cmic_config.ini')
cmic_config = config['sit']
url = cmic_config['webservices.360.url']
req_headers = { 
    'Authorization': '{} {}'.format(cmic_config['webservices.360.user.auth'], cmic_config['webservices.360.user.password']),
    #'Authorization': '{} {}'.format(cmic_config['webservices.360.user.auth'], base64_auth),
    'User-Agent':'Mozilla/5.0'
}
url = '{}/{}'.format(url,'sonora/cmicrest/workflow/sendBackToEdit')#It is called by click edit claim from Eligible page. 
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
        "group": "CMC_SUPER",
        "userId": "mclm022",
        "comment": ""
    }
    return my_data  
    
def callService(caseid):
    try:
        oFileName = '{}{}_{}_{}.json'.format(output_path,'sendBackToEdit','Resp',curDt)
        with io.open(oFileName,'a',encoding='utf-8') as o:            
            payload = buildPostData()
            url_data = {'url': url, 'caseid':caseid ,'data': payload }
            post_url = '{url}:payload={data}'.format(**url_data)
            request_data = 'post request:{}'.format(post_url)
            pp.pprint(request_data)
            #write_output_file(o,'/*',True)
            #write_output_file(o,request_data,True)
            posturl = '{url}/{caseid}'.format(**url_data)
            pp.pprint(posturl)
            r = requests.post(posturl, verify=False, headers=req_headers, json=payload)
            response_code = '-------------response:{}-------------'.format(r.status_code)
            pp.pprint(response_code)
            #write_output_file(o,response_code,True)
            #write_output_file(o,'*/',True)
            parsed = json.dumps(r.json(),ensure_ascii=False, indent=4) 
            pp.pprint(parsed)
            #write_output_file(o,parsed,True)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    callService(20479)