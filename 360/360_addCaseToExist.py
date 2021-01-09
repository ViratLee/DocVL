import requests, json, io, datetime, configparser, base64, codecs
config = configparser.ConfigParser()
config.read('cmic_config.ini')
cmic_config = config['uat']
url = cmic_config['webservices.360.url']
req_headers = { 
    'Authorization': '{} {}'.format(cmic_config['webservices.360.user.auth'], cmic_config['webservices.360.user.password']),
    #'Authorization': '{} {}'.format(cmic_config['webservices.360.user.auth'], base64_auth),
    'User-Agent':'Mozilla/5.0'
}
url = '{}/{}'.format(url,'sonora/cmicrest/workflow/addCaseToExisting')
now = datetime.datetime.now()
curDt = '{:%Y-%m-%d_%H%M}'.format(now)
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
def buildPostData():
    my_data = {
        "newCase": {
        "caseId": 1125572,
        "businessType": "CLM",
        "category": "RCLA",
        "certNo": "",
        "channel": "Scan",
        "claimAmount": "",
        "claimNum": "",
        "claimType": "Cash",
        "comment": "renewal PBWP=>3rd PBWP due 05-09-18/ดึงวันsubmitผิด=>createใหม่แล้ว",
        "completionDate": "",
        "creationDatetime": 1525422921000,
        "dataentryUser": "mclm022",
        "dateReceived": 1503371338000,
        "dependentCode": "",
        "dob": "07/03/2015",
        "fyi": "",
        "policyNo": "T197307878",
        "indexingUser": "mclm022",
        "insuredFirstname": "รัชXXXXX",
        "insuredLastname": "สุขXXXXX",
        "medicalUser": "",
        "memberId": "",
        "nationalId": "1129902476128",
        "partyId": 83965603,
        "phase": "Discharge",
        "providerCode": "1001360004",
        "receivingCentre": "AIT",
        "scanBatchId": "C275CMAC180504N153503",
        "scanDate": "",
        "scanType": "N",
        "slaDatetime": 1503976080000,
        "submissionDate": 1503371338000,
        "submissionPoint": "AIT",
        "typeOfService": "",
        "lockType": 0,
        "jsonData": "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",
        "deleteUser": "",
        "assignGroup": "",
        "activity": "DataEntry",
        "owner": "mclm022",
        "submissionAgentCode": "0000538141",
        "risk": "",
        "assessResult": "",
        "accidentDate": "",
        "hospitalDate": "",
        "dischargeDate": "",
        "claimStatus": "",
        "location": "AIT",
        "injuryArea": "",
        "lossCode": "",
        "docTypeCode": "",
        "urgentReason": "",
        "totalPages": 0,
        "ingeniumClientId": "B017181114",
        "documentIntime": "",
        "addDocumentIntime": "",
        "claimStatusDate": "",
        "businessSource": "",
        "causeOfTreatment": "",
        "insureType": "IND",
        "ipdOpd": "IPD",
        "lastDocumentDate": "",
        "billingItem": "",
        "vip": "false",
        "complete": "false",
        "delete": "false",
        "contractProvider": "true",
        "returnOriginal": "false",
        "caseValidated": "true",
        "unidentified": "false",
        "stp": "false",
        "nonClean": "false"
    },
    "existingCaseId": 1129623
    }

    return my_data
def callService(payload):
    try:
        oFileName = '{}{}_{}_{}.json'.format(output_path,'360_add_to_exit','Resp',curDt)
        with io.open(oFileName,'a',encoding='utf-8') as o:            
            #payload = buildPostData()
            url_data = {'url': url, 'data': payload }
            post_url = '{url}:payload={data}'.format(**url_data)
            request_data = 'post request:{}'.format(post_url)
            write_output_file(o,'/*',True)
            write_output_file(o,request_data,True)
            r = requests.post(url, verify=False, headers=req_headers, json=payload)
            response_code = '-------------response:{}-------------'.format(r.status_code)
            write_output_file(o,response_code,True)
            write_output_file(o,'*/',True)
            if response_code == '200':
	            parsed = json.dumps(r.json(),ensure_ascii=False, indent=4) 
	            write_output_file(o,parsed,True)
    except Exception as e:
        print(e)

def readJsonDataAsTextbyjsonFile(json_file):
    with open(json_file,encoding='utf-8') as f:
        content = f.read()
    return content

def main():
    post_data = readJsonDataAsTextbyjsonFile('xxx.json')
    callService(post_data)

if __name__ == '__main__':
    main()        