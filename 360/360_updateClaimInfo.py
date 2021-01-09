import requests, json, io, datetime, configparser, base64, codecs, sys
config = configparser.ConfigParser()
config.read('cmic_config.ini')
cmic_config = config['sit']
url = cmic_config['webservices.360.url']

my_data = {
        "caseId": 17566,
        "businessType": "",
        "category": "RCLA",
        "certNo": "",
        "channel": "Email",
        "claimAmount": 800,
        "claimNum": "C900000555/1",
        "claimType": "Cash",
        "comment": "",
        "completionDate": "",
        "creationDatetime": "08/02/2019 15:08:46",
        "dataentryUser": "mclm022",
        "dateReceived": "08/02/2019 15:08:46",
        "dependentCode": "",
        "dob": "08/10/1963",
        "fyi": "",
        "policyNo": "T149159252",
        "indexingUser": "",
        "insuredFirstname": "พรพXXXX",
        "insuredLastname": "โกศล",
        "medicalUser": "",
        "memberId": "",
        "nationalId": "3101501447886",
        "partyId": 68138442,
        "phase": "Discharge",
        "providerCode": "1001280005",
        "receivingCentre": "",
        "scanBatchId": "",
        "scanDate": "",
        "scanType": "",
        "slaDatetime": "08/09/2019 15:08:00",
        "submissionDate": "08/02/2019 15:08:46",
        "submissionPoint": "",
        "typeOfService": "1",
        "lockType": 0,
        "jsonData": "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",
        "deleteUser": "",
        "assignGroup": "",
        "activity": "ManualReview",
        "owner": "",
        "submissionAgentCode": "",
        "risk": "3",
        "assessResult": "Pending",
        "accidentDate": "",
        "hospitalDate": "",
        "dischargeDate": "08/02/2019",
        "claimStatus": "25",
        "location": "",
        "injuryArea": "",
        "lossCode": "J10.8",
        "docTypeCode": "",
        "urgentReason": "",
        "totalPages": 0,
        "ingeniumClientId": "B001645814",
        "documentIntime": "",
        "addDocumentIntime": "",
        "claimStatusDate": "08/02/2019 15:09:56",
        "businessSource": "",
        "causeOfTreatment": "",
        "insureType": "IND",
        "ipdOpd": "IPD",
        "lastDocumentDate": "",
        "billingItem": "",
        "mdrt": "",
        "edi": "Y",
        "vip": "false",
        "complete": "false",
        "delete": "false",
        "contractProvider": "false",
        "returnOriginal": "false",
        "caseValidated": "true",
        "unidentified": "false",
        "stp": "false",
        "nonClean": "false",
        "bbl": "false"
    }

req_headers = { 
    'Authorization': '{} {}'.format(cmic_config['webservices.360.user.auth'], cmic_config['webservices.360.user.password']),
    #'Authorization': '{} {}'.format(cmic_config['webservices.360.user.auth'], base64_auth),
    'User-Agent':'Mozilla/5.0'
}
#url = '{}/{}'.format(url,'sonora/cmicrest/workflow/updateWork') 
case_id_list = ['17565']

def write_output_file(o, line, printoutput=False):
    try:
        if printoutput == True:
           text = '{}'.format(line)
           print(text)
        o.write(line)
        o.write("\n")
    except IOError:
        raise

def updateWork(post_data):
    url = cmic_config['webservices.360.url']
    url = '{}/{}'.format(url,'sonora/cmicrest/workflow/updateWork') 
    now = datetime.datetime.now()
    curDt = '{:%Y-%m-%d_%H%M}'.format(now)
    output_path = cmic_config['output.path']
    print(url)
    print('sending...')
    r = requests.post(url, data=post_data, headers=req_headers)
    print(r)
    # response_code = '-------------response:{}-------------'.format(r.status_code)
    # print(response_code)
    # parsed = json.dumps(r.json(), indent=4) 
    # print(parsed)    

def readJsonDataAsText(data_file):
    with open(data_file,encoding='utf-8') as f:
        content = f.read()
    return content

if __name__ == '__main__':
    #submit_data = readJsonDataAsText('update_work.json')    
    updateWork(my_data)