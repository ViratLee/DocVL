#perfer, if foo is not None:
import requests, configparser, json
from enum import Enum
class MethodHttp(Enum):
    GET = 1
    POST = 2

class ServiceRequest:
    """
    Service for http request.
    """
    def __init__(self, system_config, req_headers, url ):
        self.system_config = system_config
        self.req_headers = req_headers
        self.url = url
    
    def call_request_service(self, method = MethodHttp.GET, json_data = None, is_verify=False ):
        try:
            url_data = ''
            get_url = ''
            #print('entry 1.')
            if(method == MethodHttp.GET):
                #print('entry 2.')
                if json_data is not None:
                    #print('entry 3.')
                    url_data = {'url': self.url, 'data': json_data }
                    get_url = '{url}?json={data}'.format(**url_data)
                else:
                    #print('entry 4.')
                    get_url = self.url
                return requests.get(get_url,  headers=self.req_headers, verify=is_verify)
            elif(method == MethodHttp.POST):
                #print('entry 5.')
                return requests.post(self.url, data=json_data,  headers=self.req_headers, verify=is_verify)
            #print('entry 6.')
            return
            """
            policyPerlifeList = output['policyPerlifeList']
            if 'policyPerlifeList' in output:
                write_output_file(o,'policy per life size {}'.format(len(policyPerlifeList)), True)    
                for policy in policyPerlifeList:
                    covNum = policy['covNum']
                    partyId = policy['partyId']
                    dash = '------------'
                    if covNum == 'MEM':
                        dash = ''
                    write_output_file(o,'{}covNum {}, partyId {} '.format(dash, covNum, partyId),True)
            else:
                #print('policyPerlifeList is null')    
            write_output_file(o,'*/',True)
            parsed = json.dumps(r.json(), indent=4) 
            write_output_file(o,parsed,True)
            """
        except Exception as e:
            #print('entry 7.')
            #print(e)
            return