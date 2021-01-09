import requests, json, io, datetime#, configparser
import yaml

def load_yaml_config():
    with open('cmic_config.yaml', 'r') as f:
        yaml_file = yaml.safe_load(f)
        #pp.pprint(yaml_file)
        return yaml_file


class retrieveLookupTEditList:
	def __init__(self, env):
		#self.config = configparser.ConfigParser()
		self.config = load_yaml_config()
		#self.config.read('cmic_config.ini')
		#self.cmic_config = self.config['uat']
		#print(env)
		self.cmic_config = self.config[env]

	def write_output_file(self, o, line, printoutput=False):
	    try:
	        if printoutput == True:
	           text = '{}'.format(line)
	           print(text)
	        o.write(line)
	        o.write("\n")
	    except IOError:
	        raise
	def callService(self):
		url = self.cmic_config['webservices.rest.url']
		req_headers = { 
		    'Authorization': '{} {}'.format(self.cmic_config['user.auth'], self.cmic_config['user.password']),#;'Basic QkFQUEVTQjpLbjR5SWFnQEtx', # UAT
		    'User-Agent':'Mozilla/5.0'
		}
		url = '{}/{}'.format(url,'rest/AIAService/lookup/retrieveLookup/RetrieveLookupIgmTeditList') 
		now = datetime.datetime.now()
		curDt = '{:%Y-%m-%d_%H%M}'.format(now)
		output_path = self.cmic_config['output.path']
		oFileName = '{}{}_{}_{}.json'.format(output_path,'RetrieveLookupIgmTeditList','Resp',curDt)
		with io.open(oFileName,'a',encoding='utf8') as o:
			json_data_str = '{"companyId":"1","tableName":"STB2"}'
			url_data = {'url': url, 'data': json_data_str}
			get_url = '{url}?json={data}'.format(**url_data)
			request_data = 'request:{}'.format(get_url)
			self.write_output_file(o,request_data, False)
			r = requests.get(get_url,  headers=req_headers, verify=False)
			response_code = '-------------response:{}-------------'.format(r.status_code)
			self.write_output_file(o,response_code, False)
			parsed = json.dumps(r.json(), indent=4) 
			self.write_output_file(o,parsed, False)
		return r