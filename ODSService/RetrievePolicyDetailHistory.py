import requests, json, io, datetime, json #configparser,
from retrieveLookupIgmList import retrieveLookupTEditList
import yaml
def load_yaml_config():
    with open('cmic_config.yaml', 'r') as f:
        yaml_file = yaml.safe_load(f)
        #pp.pprint(yaml_file)
        return yaml_file

# config = configparser.ConfigParser()
# config.read('cmic_config.ini')
env = 'uat'
config = load_yaml_config()
cmic_config = config[env]
#policy_list =['T135487297']
#policy_list =['T890077861']
#policy_list =['T890148978']
#policy_list =['T890184291']
#policy_list =['T215190718']
#policy_list =['T189685948']
#policy_list =['01224:2019000029:00']
#policy_list =['01373:2019000071:00']
#policy_list =['T206016539','T890065161']
#policy_list =['06652:2014000003:00']
#policy_list = ['02995:2011080380:00']
#policy_list = ['02753:1999000160:00']
#policy_list = ['02310:2008000040:00']
#policy_list = ['T890053296','T206016445']
#policy_list = ['P318745918','P403550364','T060434784','T080489599','T111906271']
#policy_list = ['01252:2010005350:00']
#policy_list = ['U880165343']
####deduct####

#policy_list = ['T205950201']
#policy_list = ['T205950405']

#policy_list = ['05726:2009000090:00']
#policy_list = ['P321232256']
#policy_list = ['T005629923']
#policy_list = ['T098833263']
#policy_list = ['T205950298']
#policy_list = ['T206016584']
#policy_list = ['T301787941']
#policy_list = ['T205950780','T205950793']
#policy_list = ['T115159914']
#policy_list = ['T456196034','T456196940','T456196953','T456196966','T456196979','T456196092','T456196102','T456196144','T456196157']
#policy_list = ['T456195996','T456196005','T456195983','T456195967','T456196018','T456196047','T456196021','T456196128','T456196131','T456196982','T456196995']
#policy_list = ['T456195996','T456196005','T456195983']
#policy_list = ['T456196034','T456196940','T456196953','T456196966','T456196979','T456196092','T456196102','T456196144','T456196157']
#policy_list = ['T141458676']
#policy_list = ['T141458676','T157200520','P024881975','T156283182','P062428594','P024881975','T162665684','P062428594']
#policy_list = ['T157200520','T162664025','P253058346','P024881975','T220205274','T213075547','T080801410','T141458676','T156283182','T220992053','T110516497','P062428594','T162665684']
#policy_list = ['T214919000','P253742416','T218963007','T221526059','T214687688','T215701259']
#policy_list = ['T221526059']
policy_list = ['01504:2010002720:01']
#policy_list = ['T222089443']#HSHP prod
#policy_list = ['T456193574']#HSHP uat
#policy_list = ['T410230949']#HSHP prod

year = '2020'
month = '12'#'10'#'05'
dt = '15'#'16'#'01'
history_date_name = '{}_{}_{}'.format(year, month, dt)
history_date_req = '{}-{}-{}'.format(year, month, dt)

def write_output_file(o, line, printoutput=False):
    try:
        if printoutput == True:
           text = '{}'.format(line)
           print(text)
        o.write(line)
        o.write("\n")
    except IOError:
        raise

def call_retrieve_policy_detail_history():
    url = cmic_config['webservices.rest.url']
    req_headers = { 
        'Authorization': '{} {}'.format(cmic_config['user.auth'], cmic_config['user.password']),#;'Basic QkFQUEVTQjpLbjR5SWFnQEtx', # UAT
        'User-Agent':'Mozilla/5.0'
    }
    url = '{}/{}'.format(url,'rest/AIAService/policy/retrievePolicy/RetrievePolicyDetailHistory') 
    count = 0
    now = datetime.datetime.now()
    curDt = '{:%Y-%m-%d_%H%M}'.format(now)
    output_path = cmic_config['output.path']
    resultFilter =  '"resultFilter":"policyHistoryList,coverageHistoryList,coveragePartyRelationHistoryList,lifeParticipantHistoryList, \
    underwritingReviewList,policyStatusHistoryList,policyBonusHistoryList,policyPayRecordHistoryList,groupPolicyPlanHistoryList"'
    for p in policy_list:
        try:
            oFileName = '{}{}_{}_{}_{}_{}.json'.format(output_path,'RetrievePolicyDetailHistory','Resp',p.replace(':','_'),history_date_name,curDt)
            if oFileName:
                o = None
                with io.open(oFileName,'a',encoding='utf8') as o:
                    count += 1
                    input("Press any key to continue...")
                    print('###{}###'.format(count))
                    json_data_str = '{"policyNo":"'+p+'","incidentDate":"'+history_date_req+'","companyId":"1", '+resultFilter+'}'
                    #{"policyNo":"T177972883","incidentDate":"2018-07-10","companyId":"1"}
                    url_data = {'url': url, 'data': json_data_str }
                    get_url = '{url}?json={data}'.format(**url_data)
                    request_data = 'request:{}'.format(get_url)
                    write_output_file(o,request_data,True)
                    r = requests.get(get_url,  headers=req_headers, verify=False)
                    response_code = '-------------response:{}-------------'.format(r.status_code)
                    write_output_file(o,response_code,True)
                    parsed = json.dumps(r.json(), indent=4) 
                    write_output_file(o,parsed)
                    output = r.json()
                    try:
                        policyHistoryList = output['policyHistoryList']
                        policyHistory = policyHistoryList[0]
                        coverageHistoryList = policyHistory['coverageHistoryList']
                        covNum = ''
                        productCd = ''
                        lifeCovStatus = ''
                        #list_effdt(coverageHistoryList)
                        #participatingIndList(coverageHistoryList)
                        #findrationTable2Cd(coverageHistoryList)
                        #list_haley_field(coverageHistoryList)
                        list_coverage_field(coverageHistoryList)
                        #findEffectiveDt(p,coverageHistoryList)
                        # for coverageHistory in coverageHistoryList:
                        #     coverage = coverageHistory
                        #     effDt = coverage['effDt']
                        #     if not effDt:
                        #         print('pol {} not found effDt !!!!!!!!!!!!!!!!!!!!!!!!!!!!!'.format(p))
                        #     else: 
                        #         print('pol {} found effDt {}'.format(p, effDt))
                        # for coverageHistory in coverageHistoryList:
                        #     covNum = coverageHistory['covNum']
                        #     productCd = coverageHistory['productCd']
                        #     lifeCovStatus = coverageHistory['lifeCovStatus']
                        #     sumAssuredAmt = coverageHistory['sumAssuredAmt']
                        #     print('******covNum:{}, productCd:{}, sumAssuredAmt:{}*****'.format(covNum, productCd, sumAssuredAmt))
                        #     lifeParticipantHistoryList = coverageHistory['lifeParticipantHistoryList']
                        #     for lifeParticipant in lifeParticipantHistoryList:
                        #         ratingTable2Cd = lifeParticipant['ratingTable2Cd']
                        #         if not ratingTable2Cd:
                        #             break
                        #     subCode = findSubPlanCode(ratingTable2Cd)
                        #     print('covNum:{}, productCd:{}, ratingTable2Cd:{}, subCode:{}, lifeCovStatus:{}'.format(covNum, productCd, ratingTable2Cd,subCode, lifeCovStatus))
                    except AttributeError as error:
                        print(error)
        except Exception as e:
            print(e)
            break

def participatingIndList(coverageHistoryList):
    for coverageHistory in coverageHistoryList:
        print(f"covNum:{coverageHistory['covNum']}, productCd:{coverageHistory['productCd']}, participatingInd:{coverageHistory['participatingInd']}, inforcePlan:{coverageHistory['inforcePlan']},  suppBenCd:{coverageHistory['suppBenCd']}, relCvgNum:{coverageHistory['relCvgNum']}") 

def findEffectiveDt(policy_no, coverageHistoryList):
    for coverageHistory in coverageHistoryList:
        productCd = coverageHistory['productCd']
        if not coverageHistory['effDt']:
            print(f'pol {policy_no}, productCd:{productCd} not found effDt !!!')
        else:
            print(f'pol {policy_no}, productCd:{productCd} found effDt ')

def findrationTable2Cd(coverageHistoryList):
    for coverageHistory in coverageHistoryList:
        covNum = coverageHistory['covNum']
        productCd = coverageHistory['productCd']
        lifeCovStatus = coverageHistory['lifeCovStatus']
        sumAssuredAmt = coverageHistory['sumAssuredAmt']
        print(f'******covNum:{covNum}, productCd:{productCd}, sumAssuredAmt:{sumAssuredAmt}*****')
        lifeParticipantHistoryList = coverageHistory['lifeParticipantHistoryList']
        for lifeParticipant in lifeParticipantHistoryList:
            ratingTable2Cd = lifeParticipant['ratingTable2Cd']
            if not ratingTable2Cd:
                break
            subCode = findSubPlanCode(ratingTable2Cd)
            print(f'covNum:{covNum}, productCd:{productCd}, ratingTable2Cd:{ratingTable2Cd}, subCode:{subCode}, lifeCovStatus:{lifeCovStatus}')
            

def findSubPlanCode(value):
    print('findSubPlanCode {}'.format(value))
    subCode = ''
    if value:
        for ingTedit in IngTeditList:
            tableValue = ingTedit['tableValue']
            if value == tableValue:
                tableValueDesc = ingTedit['tableValueDesc']
                valueDesc = tableValueDesc.split()
                print('valueDesc {}'.format(valueDesc))
                subCode = valueDesc[-1]
                print('subCode {}'.format(subCode))
                break
    return subCode

def list_effdt(coverageHistoryList):
    for coverage in coverageHistoryList:
        covNum = coverage['covNum']
        productCd = coverage['productCd']
        lifeCovStatus = coverage['lifeCovStatus']
        effDt = coverage['effDt']
        oldPlanNo = coverage['oldPlanNo']
        planNo = coverage['planNo']
        planEffDt = coverage['planEffDt']
        participatingInd = coverage['participatingInd']
        print(f'covNum:{covNum}, productCd:{productCd},planNo: {planNo}, oldPlanNo: {oldPlanNo},planEffDt: {planEffDt}, effDt:{effDt}, lifeCovStatus:{lifeCovStatus}, participatingInd:{participatingInd}')

def list_haley_field(coverageHistoryList):
    for coverage in coverageHistoryList:
        covNum = coverage['covNum']
        productCd = coverage['productCd']
        lifeCovStatus = coverage['lifeCovStatus']
        planNo = coverage['planNo']
        participatingInd = coverage['participatingInd']
        suppBenCd = coverage['suppBenCd']
        inforcePlan = coverage['inforcePlan']
        print(f'covNum:{covNum}, productCd:{productCd},planNo: {planNo}, lifeCovStatus:{lifeCovStatus}, participatingInd:{participatingInd}, suppBenCd:{suppBenCd} , inforcePlan:{inforcePlan}')

def list_coverage_field(coverageHistoryList):
    for coverage in coverageHistoryList:
        covNum = coverage['covNum']
        productCd = coverage['productCd']
        lifeCovStatus = coverage['lifeCovStatus']
        planNo = coverage['planNo']
        participatingInd = coverage['participatingInd']
        matuityTransferInd = coverage['matuityTransferInd']
        print(f'covNum:{covNum}, productCd:{productCd},planNo: {planNo}, lifeCovStatus:{lifeCovStatus}, participatingInd:{participatingInd}, matuityTransferInd:{matuityTransferInd}')
        # if matuityTransferInd is not None:
        #     input()
                        
# def find_par(coverageHistoryList):
#     for coverage in coverageHistoryList:
#         covNum = coverage['covNum']
#         if covNum == '01':
#             participatingInd = coverage['participatingInd']
#             productCd = coverage['productCd']
#             planNo = coverage['planNo']
#             lifeCovStatus = coverage['lifeCovStatus']
#             print(f'covNum:{covNum}, productCd:{productCd},planNo: {planNo}, lifeCovStatus:{lifeCovStatus}, participatingInd:{participatingInd}, suppBenCd:{suppBenCd}' )
            
def callService():
    # global IngTeditList
    # retrieve_lookup = retrieveLookupTEditList(env)
    # r = retrieve_lookup.callService()
    # output = r.json()
    # IngTeditList = output['IngTeditList']
    call_retrieve_policy_detail_history()
def main():
    callService()
if __name__ == '__main__':
    main()  
#parsed = json.loads(r.json())
#print(json.dumps(parsed, indent=4, sort_keys=True)
#output = r.json()
#print(output['code'])
#print(output['message'])
#print(output['data'])
#print(r.headers['content-type'])