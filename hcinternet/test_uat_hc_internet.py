#pytest .\test_uat_hc_internet.py --junitxml=D:\unittest_result\uat_result_hc_20200120.xml
import pytest, configparser, json, requests
from hcUtil import HCUtil
import yaml
import time

class CmicConfig:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('cmic_config.ini')
        self.cmic_config = config['local']
        self.req_headers = { 
            'Authorization': '{} {}'.format(self.cmic_config['user.auth'], self.cmic_config['user.password']),
            'content-type': 'application/json',
            'User-Agent':'Mozilla/5.0'
        }
      
        root_url = self.cmic_config['cmic.web.path']
        config_yaml_file = None
        with open('cmic_config.yaml', 'r') as f:
            config_yaml_file = yaml.safe_load(f)
        self.conf_file = config_yaml_file['sit']
        url_360 = self.conf_file['webservices.360.url']
        self.claimstatus_req_headers = {
            'Authorization': '{} {}'.format(self.conf_file['webservices.360.user.auth'], self.conf_file['webservices.360.user.password']),
            'User-Agent':'Mozilla/5.0'
        }
        self.claimbalance_url = '{}/{}'.format(root_url,'CMiC/api/external/hcinternet/claimsBalance') 
        self.claimstatus_url = '{}/{}'.format(url_360,'sonora/cmicrest/workflow/getClaimStatus')

class TestUATHCInternet(object):

    @pytest.fixture
    def cmic_read_config(self):
        return CmicConfig()

    def test_claim_balance_pass(self, cmic_read_config, record_xml_property):
        pytest.skip("skipping this test")
        json_file = "sm_claim_balance_0000013230.json"
        hcUtil = HCUtil(cmic_read_config)
        p_dat = hcUtil.read_json_data_as_text(json_file)
        record_xml_property("rest", cmic_read_config.claimbalance_url)
        record_xml_property("policyNumber", '0000013230')
        record_xml_property("send",'')
        r = hcUtil.claim_balance(p_dat)
        record_xml_property("reponse with code ",r.status_code)
        output = r.json()
        assert r is not None, 'r is None'
        assert r.status_code == 200, 'response should = 200'
        assert output['code'] == 'S', 'code should = S' 
        # service_request = ServiceRequest(cmic_read_config.cmic_config, cmic_read_config.req_headers, cmic_read_config.url)
        # r = service_request.call_request_service(MethodHttp.GET,json_data)
        # assert r is not None, 'r is None'
        # assert r.status_code == 200, 'response should = 200'
        # output = r.json()
        # assert output['returnCode'] == 'S', 'code should = S' 
        # assert len(output['policyList']) == 1, 'policyList should = 1'
        # cov_size = len(output['policyList'][0]['coverageList'])
        # record_xml_property("coverageList size", cov_size)

    def test_check_stp_criteria_pass(self, cmic_read_config, record_xml_property):
        pytest.skip("skipping this test")
        req_url = 'http://localhost:8080/CMiC/api/rest/utility/checkstpcriteria/3559688/5000/0'
        record_xml_property("rest", req_url)
        record_xml_property("claimid", '3559688')
        record_xml_property("send",'')
        r = requests.post(req_url,  headers=cmic_read_config.req_headers)
        record_xml_property("reponse with code ",r.status_code)
        output = r.json()
        assert r is not None, 'r is None'
        assert r.status_code == 200, 'response should = 200'
        assert output['code'] == 'S', 'code should = S' 
        message = output['message']
        record_xml_property("message ",message)
        assert 'stp: true' in message, 'stp should true'

    def test_check_opd_ai_stp_edi(self, cmic_read_config, record_xml_property):
        #pytest.skip("skipping this test")
        req_url = 'http://localhost:8080/CMiC/api/external/hcinternet/submitClaim'
        #record_xml_property("rest", req_url)
        json_file = "sm_submit_claim_0000015551_treament_5_edi.json"
        hcUtil = HCUtil(cmic_read_config)
        post_data = hcUtil.read_json_data_as_text(json_file)
        r1 = requests.post(req_url,data=post_data.encode('utf-8'),  headers=cmic_read_config.req_headers)
        record_xml_property("reponse with code ",r1.status_code)
        output1 = r1.json()
        assert r1 is not None, 'r is None'
        assert r1.status_code == 200, 'response should = 200'
        assert output1['code'] == 'S', 'submit claim code should = S' 
        message = output1['message']
        record_xml_property("message ",message)
        data1 = output1['data']
        record_xml_property("data1 ",data1)
        case_id = data1['caseId']
        record_xml_property("case_id ",case_id)
        record_xml_property("delay  ", 20)
        time.sleep(20)
        r2 = hcUtil.claim_status(case_id)
        output2 = r2.json()
        assert output2['code'] == 'S', 'get claimstatus code should = S' 
        data2 = output2['data']
        activity = data2['activity']
        record_xml_property("activity ",activity)
        assert activity == "Accept", 'activity should Accept'
        # assert 'stp: true' in message, 'stp should true'

    def test_check_ipd_ai_stp_edi(self, cmic_read_config, record_xml_property):
        #pytest.skip("skipping this test")
        req_url = 'http://localhost:8080/CMiC/api/external/hcinternet/submitClaim'
        #record_xml_property("rest", req_url)
        json_file = "sm_submit_claim_T140023374_treament_1.json"
        hcUtil = HCUtil(cmic_read_config)
        post_data = hcUtil.read_json_data_as_text(json_file)
        r1 = requests.post(req_url,data=post_data.encode('utf-8'),  headers=cmic_read_config.req_headers)
        record_xml_property("reponse with code ",r1.status_code)
        output1 = r1.json()
        assert r1 is not None, 'r is None'
        assert r1.status_code == 200, 'response should = 200'
        assert output1['code'] == 'S', 'submit claim code should = S' 
        message = output1['message']
        record_xml_property("message ",message)
        data1 = output1['data']
        record_xml_property("data1 ",data1)
        case_id = data1['caseId']
        record_xml_property("case_id ",case_id)
        record_xml_property("delay  ", 20)
        time.sleep(20)
        r2 = hcUtil.claim_status(case_id)
        output2 = r2.json()
        assert output2['code'] == 'S', 'get claimstatus code should = S' 
        data2 = output2['data']
        activity = data2['activity']
        record_xml_property("activity ",activity)
        assert activity == "DataEntry", 'activity should DataEntry'
        # assert 'stp: true' in message, 'stp should true'