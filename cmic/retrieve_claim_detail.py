import requests, json, io, datetime#, configparser
import sys
import yaml
def load_yaml_config():
    with open('cmic_config.yaml', 'r') as f:
        yaml_file = yaml.safe_load(f)
        #pp.pprint(yaml_file)
        return yaml_file

config = load_yaml_config()
# config = configparser.ConfigParser()
# config.read('cmic_config.ini')
cmic_config = config['prod']
url = cmic_config['webservices.rest.url']
req_headers = { 
    'Authorization': '{} {}'.format(cmic_config['user.auth'], cmic_config['user.password']),#;'Basic QkFQUEVTQjpLbjR5SWFnQEtx', # UAT
    'User-Agent':'Mozilla/5.0'
}
url = '{}/{}'.format(url,'rest/AIAService/claim/retrieveClaim/RetrieveClaimDetail')
now = datetime.datetime.now()
curDt = '{:%Y-%m-%d_%H%M}'.format(now)
output_path = cmic_config['output.path']
#claim_id_list = ['394415791693','394421550148']
#claim_id_list = ['15469598']#uat
#claim_id_list = ['51954519']#prd

#claim_id_list = ['36832568','36832567']#prd
#claim_id_list = ['28711949']#prd
claim_id_list = ['28711949','28711946','25862883','40738351','36418815','28711951','30407411','28711944','30407410','28711941','28711945','35765967','33102622','28711947','28711943','33102586','35765966','36418818','25862881','33102620','36418817','25862879','28711948','33102619','36418816','35765968','25862880','28711953','25862877','25862878','33102621','25862882','35765969','33102587','36418814','35765970','28711950','28711940']


def write_output_file(o, line, printoutput=False):
    try:
        if printoutput == True:
           text = '{}'.format(line)
           print(text)
        o.write(line)
        o.write("\n")
    except IOError:
        raise
def callService():
    count = 0
    for clm_id in claim_id_list:
        try:
                oFileName = '{}{}_claimid_{}_{}_{}.json'.format(output_path,'RetrieveClaimDetail',clm_id,'Resp',curDt)
                with io.open(oFileName,'a',encoding='utf-8') as o:            
                    count += 1
                    print('###{}###'.format(count))
                    #payload =  '{"resultFilter":"claimLossEventInfoList, claimBenefitList, claimParticipantList","claimList":[{"claimId":"'+clm_id+'","companyId":"1"}]}'
                    #payload =  '{"resultFilter":"claimBenefitList, claimLossEventInfoList, claimParticipantList, claimPolicyList, policyObj, policyProductObj, caseObj, claimStatusList, finActivityClaimRltnList, paymentList, paymentFormDetailList, claimNotesList, medicalTreatmentObj, claimPolicyCoverageList, claimBenefitCoverageList, requirementInfoList","claimId":"'+clm_id+'","companyId":"1"}'
                    payload3 =  '{"resultFilter":"claimBenefitList,claimLossEventInfoList,claimMedicalTreatmentRelationList,medicalTreatmentList,claimParticipantList,claimPolicyList,claimPolicyCoverageList,claimBenefitCoverageList,policyObj,policyProductObj,caseObj,requirementInfoList,claimNotesList,paymentList,claimStatusList,finActivityClaimRltnList,paymentFormDetailList,medicalTreatmentObj,policyBenefitMasterObj","claimId":"'+clm_id+'","companyId":"1"}'
                    #payload2 = '{"resultFilter":"claimBenefitList, claimLossEventInfoList, claimParticipantList, claimPolicyList, policyObj,policyProductObj,caseObj,claimStatusList,finActivityClaimRltnList,paymentList,paymentFormDetailList,claimNotesList,medicalTreatmentObj, claimPolicyCoverageList, requirementInfoList","claimList":[{"claimId":"'+clm_id+'","companyId":"1"}]}'
                    url_data = {'url': url, 'data': payload3 }
                    #post_url = '{url}:payload={data}'.format(**url_data)
                    get_url = '{url}?json={data}'.format(**url_data)
                    #request_data = 'post request:{}'.format(post_url)
                    request_data = 'get request:{}'.format(get_url)
                    write_output_file(o,'/*',True)
                    write_output_file(o,request_data,True)
                    r = requests.get(get_url,  headers=req_headers,verify=False)
                    #r = requests.post(url, data=payload, headers=req_headers,verify=False)
                    response_code = '-------------response:{}-------------'.format(r.status_code)
                    write_output_file(o,response_code,True)
                    write_output_file(o,'*/',True)
                    if r.status_code != 200:
                        print('exit')
                        return
                    parsed = json.dumps(r.json(), ensure_ascii=False, indent=4) 
                    write_output_file(o,parsed,False)
                    output = r.json()
                    claimList = output['claimList']
                    clam = claimList[0]
                    keyPolicyNo = clam['keyPolicyNo']
                    claimId = clam['claimId']
                    careCardType = clam['careCardType']
                    claimNo = clam['claimNo']
                    print(f'claimId:{claimId}, careCardType:{careCardType}')
                    if careCardType == '2':
                        claimLossEventInfoList = clam['claimLossEventInfoList']
                        for clmLostEvnIfo in claimLossEventInfoList:
                            lossEventDt = clmLostEvnIfo['lossEventDt']
                            lossEventType = clmLostEvnIfo['lossEventType']
                            print(f'claimNo:{claimNo}, lossEventDt:{lossEventDt}, lossEventType:{lossEventType}')
                            if lossEventDt == '2020-10-29':
                                if lossEventType == '1':
                                   print(f'found {claimNo}')
                                   
                    # write_output_file(o,'/*',True)
                    # keyPolNo = 'claimId:{}'.format(claimId)
                    # write_output_file(o,keyPolNo,True)
                    # write_output_file(o,'/*',True) 
        except Exception as e:
            print(e)
            break
def main():
    callService()
if __name__ == '__main__':
    main()