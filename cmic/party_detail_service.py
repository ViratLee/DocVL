import requests, json, io, datetime, configparser
from PartyDetail import PartyDetail

def load_yaml_config():
    with open('cmic_config.yaml', 'r') as f:
        yaml_file = yaml.safe_load(f)
        #pp.pprint(yaml_file)
        return yaml_file

class partyDetailService:
	def __init__(self,env):
        # config = configparser.ConfigParser()
        # config.read('cmic_config.ini')
        config = load_yaml_config()
        self.cmic_config = config[env]

	def callService(party_id):
		req_headers = { 
        	'Authorization': '{} {}'.format(self.cmic_config['user.auth'], self.cmic_config['user.password']),
    		'User-Agent':'Mozilla/5.0'
		}
		url = self.cmic_config['webservices.rest.url']
		url = '{}/{}'.format(url,'rest/AIAService/party/retrieveParty/RetrievePartyDetail') 
		json_data_str = '{"partyId":"'+party_id+'","companyId":"1"}'
		url_data = {'url': url, 'data': json_data_str }
		get_url = '{url}?json={data}'.format(**url_data)
		request_data = 'request:{}'.format(get_url)
		try:
			r = requests.get(get_url,  headers=req_headers,verify=False)
			response_code = '-------------response:{}-------------'.format(r.status_code)
			output = r.json()
			partyList = output['partyList']
			party = partyList[0]
		except as e:
			print(e)