import requests, json, io, datetime, json #, configparser
import yaml
def load_yaml_config():
    with open('cmic_config.yaml', 'r') as f:
        yaml_file = yaml.safe_load(f)
        #pp.pprint(yaml_file)
        return yaml_file

config = load_yaml_config()
# config = configparser.ConfigParser()
# config.read('cmic_config.ini')
cmic_config = config['uat']
national_id_list = ['1100400370601']
url = cmic_config['webservices.rest.url']
req_headers = { 
    'Authorization': '{} {}'.format(cmic_config['user.auth'], cmic_config['user.password']),#;'Basic QkFQUEVTQjpLbjR5SWFnQEtx', # UAT
    'User-Agent':'Mozilla/5.0',
    'Content-type': 'application/json'
}


url = '{}{}'.format(url,'/rest/AIAService/party/searchParty/SearchParty') 
now = datetime.datetime.now()
curDt = '{:%Y-%m-%d_%H%M}'.format(now)
output_path = cmic_config['output.path']

def buildPostData(p):
    my_data = [{
    "companyId": "1",
    "firstName": '',
    "lastName": '',
    "nationId": "{}".format(p),
    "birthDate": '',
    "sex": ''
    } ] 
    return my_data 

#m_data = '{json=[{\'firstName\':null,\'lastName\':null,\'companyId\':\'1\',\'sex\':null,\'nationId\':\'1100400370601\',\'birthDate\':null}]}'
companyId = '1'
firstName = 'วิยะดา'
lastName = 'null'
nationId = ''
#nationId = '3100905021201'
sex = 'null'
birthDate = 'null'

def write_output_file(o, line, printoutput=False):
    try:
        if printoutput == True:
           text = '{}'.format(line)
           print(text)
        o.write(line)
        o.write("\n")
    except IOError:
        raise

def readJsonDataAsText(json_file):
    #with open(data_sumit['case_validate_json'],encoding='utf-8') as f:
    with open(json_file,encoding='utf-8') as f:
        content = f.read()
    #print(type(content))
    #print(content)
    return content

def call_search_party(post_data):
    try:
        print(type(post_data))
        oFileName = '{}{}_{}_{}.json'.format(output_path,'SearchParty','Resp',curDt)
        if oFileName:
        #    o = None
            with io.open(oFileName,'a',encoding='utf8') as o:
                #json_data_str = '{"policyNo":"'+p+'","incidentDate":"'+history_date_req+'","companyId":"1", '+resultFilter+'}'
                #{"policyNo":"T177972883","incidentDate":"2018-07-10","companyId":"1"}
                #url_data = {'url': url, 'data': json_data_str }
                #get_url = '{url}?json={data}'.format(**url_data)
                #request_data = 'request:{}'.format(get_url)
                #write_output_file(o,request_data,True)
                print(url)
                #r = requests.post(url, verify=False, headers=req_headers, json=data=json.dumps(data)post_data)
                json_data_str = '{"firstName":"'+firstName+'","companyId":"1", "lastName:"'+lastName+ '", "nationId:"'+nationId+', "sex:"'+sex+', "birthDate:"'+birthDate+'"}'
                #json_data_str = '{"firstName":,"companyId":"1", "lastName":, "nationId:"'+nationId+', "sex":, "birthDate":}'
                #json_data_str = '{"companyId":"1","nationId":"'+nationId+'"}'
                #json_data_str = '{"companyId":"1","nationId":"3669800037950"}' 
                #json_data_str = '{"companyId":"1","nationId":"110XXXX673942"}'
                json_data_str = '{"companyId":"1","nationId":"3509901447259"}'
                json_data_str = '{"companyId":"1","firstName":"วิยะดา"}'
                url_data = {'url': url, 'data': json_data_str }
                get_url = '{url}?json={data}'.format(**url_data)
                print(get_url)
                request_data = 'request:{}'.format(get_url)

                #r = requests.post(url, verify=False, headers=req_headers, json=json.dumps(json_data_str))
                r = requests.get(get_url, headers=req_headers, verify=False)
                print(r)
                response_code = '-------------response:{}-------------'.format(r.status_code)
                write_output_file(o,response_code,True)
                parsed = json.dumps(r.json(), indent=4) 
                print(parsed)
                write_output_file(o,parsed)
    except Exception as e:
        print(e)

def main():
    post_data = readJsonDataAsText('search_party_request_3509900153081.json')
    call_search_party(post_data)
if __name__ == '__main__':
    main()  
#parsed = json.loads(r.json())
#print(json.dumps(parsed, indent=4, sort_keys=True)
#output = r.json()
#print(output['code'])
#print(output['message'])
#print(output['data'])
#print(r.headers['content-type'])