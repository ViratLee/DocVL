import requests, json, io, datetime#, configparser
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
#print('{} {}'.format(cmic_config['user.auth'], cmic_config['user.password']))
url = cmic_config['webservices.rest.url']
req_headers = { 
    'Authorization': '{} {}'.format(cmic_config['user.auth'], cmic_config['user.password']),#;'Basic QkFQUEVTQjpLbjR5SWFnQEtx', # UAT
    'User-Agent':'Mozilla/5.0'
}
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

def retrievePolicyDetail(policyNo):
    policy_detail_url = '{}/{}'.format(url,'rest/AIAService/policy/retrievePolicy/RetrievePolicyDetail')
    json_data_str = '{"policyNo":"'+policyNo+'","companyId":"1"}'
    url_data = {'url': policy_detail_url, 'data': json_data_str }
    get_url = '{url}?json={data}'.format(**url_data)
    request_data = 'request:{}'.format(get_url)
    print(request_data)
    r = requests.get(get_url,  headers=req_headers,verify=False)
    response_code = '-------------response:{}-------------'.format(r.status_code)
    print(response_code)
    output = r.json()
    policyList = output['policyList']
    policy = policyList[0]
    holdingList = policy['holdingList']
    holding = holdingList[0]
    holdingPartyRelationList = holding['holdingPartyRelationList']
    agent_party_id = ''
    for holdingPartyRelation in holdingPartyRelationList:
        holdingPartyRelCd = holdingPartyRelation['holdingPartyRelCd']
        holding_party = holdingPartyRelation['partyId']
        businessKey = holdingPartyRelation['businessKey']
        if holdingPartyRelCd == '30':
            agent_party_id = holding_party
    return agent_party_id

def searchProducerByPartyId(partyId):
    search_procedure_by_party_id_url = '{}/{}'.format(url,'rest/AIAService/agency/searchProducer/SearchByPartyId')
    json_data_str = '{"partyId":"'+partyId+'","companyId":"1"}'
    url_data = {'url': search_procedure_by_party_id_url, 'data': json_data_str }
    get_url = '{url}?json={data}'.format(**url_data)
    request_data = 'request:{}'.format(get_url)
    print(request_data)
    r = requests.get(get_url,  headers=req_headers,verify=False)
    response_code = '-------------response:{}-------------'.format(r.status_code)
    print(response_code)
    output = r.json()
    producer_list = output['producerList']
    producer_cd = ''
    relatedProducerId = ''
    for producer in producer_list:
        business_key = producer['businessKey']
        producerRelationList = producer['producerRelationList']
        if 'AADMIN:AGENT' in business_key:
            producer_cd = producer['producerCd']
            break
    found = False
    for producer in producer_list:
        producerRelationList = producer['producerRelationList']
        if found == True:
            break
        for producerRelation in producerRelationList:
            producerRelationRoleCd = producerRelation['producerRelationRoleCd']
            if producerRelationRoleCd == '11':
                relatedProducerId = producerRelation['relatedProducerId']
                found = True
                break
    retrieve_procedure_by_procedure_id_url = '{}/{}'.format(url,'rest/AIAService/agency/retrieveProducer/RetrieveProducer')
    json_data_str = '{"producerId":"'+relatedProducerId+'","companyId":"1"}'
    url_data = {'url': retrieve_procedure_by_procedure_id_url, 'data': json_data_str }
    get_url = '{url}?json={data}'.format(**url_data)
    request_data = 'request:{}'.format(get_url)
    print(request_data)
    r = requests.get(get_url,  headers=req_headers,verify=False)
    response_code = '-------------response:{}-------------'.format(r.status_code)
    print(response_code)
    output = r.json()
    producerList = output['producerList']
    producerCd = ''
    for producer in producerList:
        producerCategory = producer['producerCategory']
        if producerCategory == '2':
            producerCd = producer['producerCd']
    return producer_cd, producerCd
def getAgentLeaderPartyIdByAgentCode(agent_code):
    retrieve_agent_withagency_url = '{}/{}'.format(url,'rest/AIAService/agency/retrieveProducer/RetrieveAgentWithAgency')
    json_data_str = '{"producerCd":"'+agent_code+'","companyId":"1"}'
    url_data = {'url': retrieve_agent_withagency_url, 'data': json_data_str }
    get_url = '{url}?json={data}'.format(**url_data)
    request_data = 'request:{}'.format(get_url)
    print(request_data)
    r = requests.get(get_url,  headers=req_headers,verify=False)
    output = r.json()
    agentWithAgencyList = output['agentWithAgencyList']
    agentWithAgency = agentWithAgencyList[0]
    agencyLeaderIndividualId = agentWithAgency['agencyLeaderPartyId']
    print('agencyLeaderIndividualId:{}'.format(agencyLeaderIndividualId))
    agencyLeaderIndividualName = ''
    searchProducer_SearchByPartyId_url = '{}/{}'.format(url,'rest/AIAService/agency/searchProducer/SearchByPartyId')
    json_data_str = '{"partyId":"'+agencyLeaderIndividualId+'","companyId":"1"}'
    url_data = {'url': searchProducer_SearchByPartyId_url, 'data': json_data_str }
    get_url = '{url}?json={data}'.format(**url_data)
    request_data = 'request:{}'.format(get_url)
    print(request_data)
    r = requests.get(get_url,  headers=req_headers,verify=False)
    output = r.json()
    producerList = output['producerList']
    producer = producerList[0]
    corpIndvInd = producer['corpIndvInd']
    producerId = ''
    if corpIndvInd == 'C':
        producerId = producer['producerId']
    else:
        print('not found producerId, corpIndvInd is {}'.format(corpIndvInd))
    corpNmLocal = ''
    if producerId:
        RetrieveProducerDetail_url = '{}/{}'.format(url,'rest/AIAService/agency/retrieveProducer/RetrieveProducerDetail')
        json_data_str = '{"producerId":"'+producerId+'","companyId":"1"}'
        url_data = {'url': RetrieveProducerDetail_url, 'data': json_data_str }
        get_url = '{url}?json={data}'.format(**url_data)
        request_data = 'request:{}'.format(get_url)
        print(request_data)
        r = requests.get(get_url,  headers=req_headers,verify=False)
        output = r.json()
        producerList = output['producerList']
        producer = producerList[0]
        carrierAppointmentList = producer['carrierAppointmentList']
        carrierAppointment = carrierAppointmentList[0]
        corpNmLocal = carrierAppointment['corpNmLocal']
    return agencyLeaderIndividualId,  corpNmLocal
def main():
    policy_no = 'T166717033'
    print('policy no {}'.format(policy_no))
    party_id = retrievePolicyDetail(policy_no)
    print('got party id:{}'.format(party_id))
    print('*******************************************************************************')
    agent_code, agency_code = searchProducerByPartyId(party_id)
    print('got agent_code:{}, got agency_code:{}'.format(agent_code,  agency_code))
    print('*******************************************************************************')
    agency_id, agency_name = getAgentLeaderPartyIdByAgentCode(agent_code)
    print('got agency_id:{}, got agency_name:{}'.format(agency_id,  agency_name))
if __name__ == '__main__':
    main()  
"""
print('got producer_cd {},producerIdAgency {}'.format(producer_cd, producerIdAgency))
retrieve_producer_url = '{}/{}'.format(url,'rest/AIAService/agency/retrieveProducer/RetrieveProducer')
json_data_str = '{"producerId":"'+producerIdAgency+'","companyId":"1"}'
url_data = {'url': retrieve_producer_url, 'data': json_data_str }
get_url = '{url}?json={data}'.format(**url_data)
request_data = 'request:{}'.format(get_url)
r = requests.get(get_url,  headers=req_headers,verify=False)
output = r.json()
producer_list = output['producerList']
producerCd = ''
for producer in producer_list:
    producerCategory = producer['producerCategory']
    if producerCategory == '2':
       producerCd = producer['producerCd']
       break
"""