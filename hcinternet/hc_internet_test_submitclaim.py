import requests
import json
import io
import datetime
import yaml

#import configparser
# config = configparser.ConfigParser()
# config.read('cmic_config.ini')

def load_yaml_config():
    with open('cmic_config.yaml', 'r') as f:
        yaml_file = yaml.safe_load(f)
        return yaml_file

config = load_yaml_config()

cmic_config = config['local']
root_url = cmic_config['cmic.web.path']

req_headers = {
    'Authorization': '{} {}'.format(cmic_config['user.auth'], cmic_config['user.password']),
    'content-type': 'application/json',
    'User-Agent':'Mozilla/5.0'
}
write_file = True

def write_output_file(o, line, printoutput=False):
    try:
        if printoutput == True:
           text = '{}'.format(line)
           print(text)
        o.write(line)
        o.write("\n")
    except IOError:
        raise

url = '{}/{}'.format(root_url,'CMiC/api/external/hcinternet/submitClaim') 
now = datetime.datetime.now()
curDt = '{:%Y-%m-%d_%H%M}'.format(now)
output_path = cmic_config['output.path']

def submit_claim(post_data,o):
    write_output_file(o,url,write_file)
    print('sending...')
    r = requests.post(url, data=post_data.encode('utf-8'), headers=req_headers)
    response_code = '-------------response:{}-------------'.format(r.status_code)
    write_output_file(o,response_code,write_file)
    parsed = json.dumps(r.json(), indent=4) 
    write_output_file(o,parsed,write_file)
 
def readJsonDataAsText(file_data):
    print('readJson')
    with open(file_data,encoding='utf-8') as f:
        content = f.read()
    return content    

def createNormalClaim():
    #normal OL claims.
    assign_dt = '2020-02-07T00:00:00.000Z' #should < 2020/02/08
    json_file = "sm_submit_claim_386185068_T101114251_Cashless_treament_4_phase_02.json"
    str_data = readJsonDataAsText(json_file) #P330003641 403209015
    comfirm_json = json.loads(str_data)
    comfirm_json["claimsSubmission"]["policyNo"] = 'P252275719'
    comfirm_json["claimsSubmission"]["partyId"] = '386323246'
    comfirm_json["claimsSubmission"]["consultationDt"] = '{}'.format(assign_dt)
    comfirm_json["claimsSubmission"]["accidentDt"] = '{}'.format(assign_dt)
    comfirm_json["claimsSubmission"]["hospitalizationDate"] = '{}'.format(assign_dt)
    comfirm_json["claimsSubmission"]["billDtFrom"] = '{}'.format(assign_dt)
    comfirm_json["claimsSubmission"]["billDtTo"] = '{}'.format(assign_dt)
    comfirm_json["claimsSubmission"]["treatmentDate"] = '{}'.format(assign_dt)
    comfirm_json["claimsSubmission"]["dischargeDate"] = '{}'.format(assign_dt)
    p_dat = json.dumps(comfirm_json, indent=4)
    #submit_dt ='2020-06-04T17:00:00.000Z'
    try:
        oFileName = '{}{}_{}_{}.json'.format(output_path,'HC-submitClaim','Resp',curDt)
        with io.open(oFileName,'a',encoding='utf8') as o:
            submit_claim(p_dat,o)
    except Exception as e:
        print(e)
def createiClaim_CS():
    #normal OL claims.
    assign_dt = '2020-01-29T00:00:00.000Z' #should < 2020/02/08
    #json_file = "sm_submit_claim_0000015551_treament_4.json" # make claim iClaim
    #json_file = "sm_submit_claim_0000015551_treament_5.json"
    #json_file = "sm_submit_claim_1000015461_treament_4.json"
    json_file = "sm_submit_claim_0000013332_treament_4.json"
    
    str_data = readJsonDataAsText(json_file) #P330003641 403209015
    comfirm_json = json.loads(str_data)
    # comfirm_json["claimsSubmission"]["policyNo"] = 'P252275719'
    # comfirm_json["claimsSubmission"]["partyId"] = '386323246'
    # comfirm_json["claimsSubmission"]["phase"] = '02'
    # comfirm_json["claimsSubmission"]["treatmentType"] = '4'
    # comfirm_json["claimsSubmission"]["causeOfTreatment"] = 'A'
    comfirm_json["claimsSubmission"]["submissionType"] = 'Cash'
    comfirm_json["claimsSubmission"]["channel"] = '05'
    comfirm_json["claimsSubmission"]["consultationDt"] = '{}'.format(assign_dt)
    comfirm_json["claimsSubmission"]["accidentDt"] = '{}'.format(assign_dt)
    comfirm_json["claimsSubmission"]["hospitalizationDate"] = '{}'.format(assign_dt)
    comfirm_json["claimsSubmission"]["billDtFrom"] = '{}'.format(assign_dt)
    comfirm_json["claimsSubmission"]["billDtTo"] = '{}'.format(assign_dt)
    comfirm_json["claimsSubmission"]["treatmentDate"] = '{}'.format(assign_dt)
    comfirm_json["claimsSubmission"]["dischargeDate"] = '{}'.format(assign_dt)
    p_dat = json.dumps(comfirm_json, indent=4)
    #submit_dt ='2020-06-04T17:00:00.000Z'
    try:
        oFileName = '{}{}_{}_{}.json'.format(output_path,'HC-submitClaim','Resp',curDt)
        with io.open(oFileName,'a',encoding='utf8') as o:
            submit_claim(p_dat,o)
    except Exception as e:
        print(e)

def createiClaim_OL():
    #normal OL claims.
    assign_dt = '2020-01-30T00:00:00.000Z' #should < 2020/02/08
    json_file = "sm_submit_claim_P330003641_Cashless_treament_4_phase_02_channel_05.json" # make claim iClaim
    str_data = readJsonDataAsText(json_file) #P330003641 403209015
    comfirm_json = json.loads(str_data)
    # comfirm_json["claimsSubmission"]["policyNo"] = 'P252275719'
    # comfirm_json["claimsSubmission"]["partyId"] = '386323246'
    comfirm_json["claimsSubmission"]["phase"] = '02'
    comfirm_json["claimsSubmission"]["treatmentType"] = '5'
    comfirm_json["claimsSubmission"]["causeOfTreatment"] = 'I'
    comfirm_json["claimsSubmission"]["submissionType"] = 'Cash'
    comfirm_json["claimsSubmission"]["channel"] = '05'
    comfirm_json["claimsSubmission"]["consultationDt"] = '{}'.format(assign_dt)
    comfirm_json["claimsSubmission"]["accidentDt"] = '{}'.format(assign_dt)
    comfirm_json["claimsSubmission"]["hospitalizationDate"] = '{}'.format(assign_dt)
    comfirm_json["claimsSubmission"]["billDtFrom"] = '{}'.format(assign_dt)
    comfirm_json["claimsSubmission"]["billDtTo"] = '{}'.format(assign_dt)
    comfirm_json["claimsSubmission"]["treatmentDate"] = '{}'.format(assign_dt)
    comfirm_json["claimsSubmission"]["dischargeDate"] = '{}'.format(assign_dt)
    p_dat = json.dumps(comfirm_json, indent=4)
    #submit_dt ='2020-06-04T17:00:00.000Z'
    try:
        oFileName = '{}{}_{}_{}.json'.format(output_path,'HC-submitClaim','Resp',curDt)
        with io.open(oFileName,'a',encoding='utf8') as o:
            submit_claim(p_dat,o)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    #createNormalClaim()
    #createiClaim_CS()
    createiClaim_OL()
    #json_file = "sm_submit_claim_T140023374_treament_1.json"
    #json_file = "sm_submit_claim_T211224277_treament_4.json"
    #json_file = "sm_submit_claim_1000015461_treament_4.json"
   
    #json_file = "sm_submit_claim_1000015461_treament_4_edi.json" #Ok decline 
    #json_file = "sm_submit_claim_0000102511_treament_5.json" #Ok decline 
    #json_file = "sm_submit_claim_0000015551_treament_5.json"
    #json_file = "sm_submit_claim_0000015551_treament_5_edi.json"
    #json_file = "sm_submit_claim_P241002760_treament_4.json"
    #json_file = "sm_submit_claim_P241002618_treament_4.json"
    
    #json_file = "sm_submit_claim_P015652744_treament_4.json"
    #json_file = "sm_submit_claim_P252275719_treament_4.json"
    
    #json_file = "sm_submit_claim_T149940254_treament_1.json" #medical
    #json_file = "sm_submit_claim_P241002618_treament_4_edi.json"

    #json_file = "sm_submit_claim_P330003324_treament_2_preauth.json"
    #json_file = "sm_submit_claim_T149940254_treament_1_Phase03.json"
    
    #json_file = "sm_submit_claim_P330003641_Cash_treament_4_phase_02.json" # make claim as opd activity (go to opd simpilfy)
    #json_file = "sm_submit_claim_0000013332_treament_4.json"
    #json_file = "sm_submit_claim_T173958759_treament_1.json"
    #json_file = "sm_submit_claim_P330003641_Cashless_treament_4_phase_02_channel_05.json" # make claim iClaim
    #json_file = "sm_submit_claim_T149940254_treament_1_Channel05.json" 
    
    #assign_dt = ''
    #str_data = readJsonDataAsText(json_file) #P330003641 403209015
    # now = datetime.datetime.now()#- datetime.timedelta(days=1)
    # today = '{:%Y-%m-%d}'.format(now)
    # submit_dt = '{}{}'.format(today,'T00:00:00.000Z')#"2019-03-06T17:00:00.000Z"
    #comfirm_json = json.loads(str_data)
    # comfirm_json["claimsSubmission"]["requestOriginalInd"] = 'Y'
    # comfirm_json["claimsSubmission"]["treatmentType"] = '5'
    # comfirm_json["claimsSubmission"]["causeOfTreatment"] = 'I'
    # for iClaim
    # comfirm_json["claimsSubmission"]["treatmentType"] = '5'
    # comfirm_json["claimsSubmission"]["causeOfTreatment"] = 'I'
    # comfirm_json["claimsSubmission"]["submissionType"] = 'Cash'
    # comfirm_json["claimsSubmission"]["channel"] = '05'
    # comfirm_json["claimsSubmission"]["consultationDt"] = '{}'.format(assign_dt)
    # comfirm_json["claimsSubmission"]["accidentDt"] = '{}'.format(assign_dt)
    # comfirm_json["claimsSubmission"]["hospitalizationDate"] = '{}'.format(assign_dt)
    # comfirm_json["claimsSubmission"]["billDtFrom"] = '{}'.format(assign_dt)
    # comfirm_json["claimsSubmission"]["billDtTo"] = '{}'.format(assign_dt)
    # comfirm_json["claimsSubmission"]["treatmentDate"] = '{}'.format(assign_dt)
    # comfirm_json["claimsSubmission"]["dischargeDate"] = '{}'.format(assign_dt)
    # comfirm_json["claimsSubmission"]["providerCode"] = '{}'.format('2020250066')
    #comfirm_json["claimsSubmission"]["phase"] = '{}'.format('03')
    # p_dat = json.dumps(comfirm_json, indent=4)
    #submit_dt ='2020-06-04T17:00:00.000Z'
    # try:
    #     oFileName = '{}{}_{}_{}.json'.format(output_path,'HC-submitClaim','Resp',curDt)
    #     with io.open(oFileName,'a',encoding='utf8') as o:
    #         submit_claim(p_dat,o)
    # except Exception as e:
    #     print(e)