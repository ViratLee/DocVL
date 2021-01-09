import requests, json
class HCUtil:
    """
    Service for HC Internet Util.
    """
    def __init__(self, system_config):
        self.system_config = system_config
     
    def claim_balance(self, post_data):
        #write_output_file(o,CmicConfig.claim.balance.url,write_file)
        r = requests.post(self.system_config.claimbalance_url, data=post_data.encode('utf-8'), headers=self.system_config.req_headers)
        response_code = '-------------response:{}-------------'.format(r.status_code)
        #write_output_file(o,response_code,write_file)
        return r
        #write_output_file(o,parsed,write_file)

    def claim_status(self, case_id):
        url = self.system_config.claimstatus_url
        url_data = {'url': url, 'data': case_id }
        get_url = '{url}/{data}'.format(**url_data)
        print(get_url)
        r = requests.get(get_url,  headers=self.system_config.claimstatus_req_headers, verify=False)
        response_code = '-------------response:{}-------------'.format(r.status_code)
        print(response_code)
        return r

    def read_json_data_as_text(self, file_data):
        print('readJson')
        with open(file_data,encoding='utf-8') as f:
            content = f.read()
        return content    