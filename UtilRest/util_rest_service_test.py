import requests
import json
import time

my_auth = {
    'Authorization': 'Basic bWNsbTAyMjptY2xtMDIy'
}
def write_output_file(o, line, printoutput=False):
    try:
        if printoutput == True:
           text = '{}'.format(line)
           print(text)
        o.write(line)
        o.write("\n")
    except IOError:
        raise
#r = requests.post('http://localhost:8080/CMiC/api/rest/utility/findEligibleByPolPerYear/T201788956/1151/05/H17',  headers=my_auth)
#r = requests.post('http://localhost:8080/CMiC/api/rest/utility/findEligibleByPolPerYear/T201788956/191/03/A09',  headers=my_auth)
#r = requests.post('http://localhost:8080/CMiC/api/rest/utility/retrievePAME/1225505',  headers=my_auth)
#r = requests.post('http://localhost:8080/CMiC/api/rest/utility/retrieveNonSTPDeclineCode/93H',  headers=my_auth)
#r = requests.post('http://localhost:8080/CMiC/api/rest/utility/testSMStp/1225605',  headers=my_auth)
#r = requests.post('http://localhost:8080/CMiC/api/rest/utility/checkpending/386415444',  headers=my_auth)

#r = requests.post('http://localhost:8080/CMiC/api/rest/utility/checkstpcriteria/3559665/2500/0',  headers=my_auth)
#r = requests.post('http://localhost:8080/CMiC/api/rest/utility/checkstpcriteria/3559688/2500/0',  headers=my_auth)

#r = requests.post('http://localhost:8080/CMiC/api/rest/utility/checkcs21declinereasonexist/375690265',  headers=my_auth)
# stp = false
#r = requests.post('http://localhost:8080/CMiC/api/rest/utility/checkcs21declinereasonexist/391697002',  headers=my_auth)
# stp = true
#r = requests.post('http://localhost:8080/CMiC/api/rest/utility/checkcs21declinereasonexist/375690164',  headers=my_auth)
# stp = false
#r = requests.post('http://localhost:8080/CMiC/api/rest/utility/checkcs21declinereasonexist/0',  headers=my_auth)
# stp = true
#r = requests.post('http://localhost:8080/CMiC/api/rest/utility/retrieveClaimSettlementDetail/245535',  headers=my_auth)
#r = requests.post('http://localhost:8080/CMiC/api/rest/utility/openEligible/1226332',  headers=my_auth)
#r = requests.post('http://localhost:8080/CMiC/api/rest/utility/retrieveClaimFrom360/1136536',  headers=my_auth)
#print(r.status_code)
#print(r.json())
# print(json.dumps(r.json(), indent=4))
# output = r.json()
# data = output['data']
# claimCanonical = data['claimCanonical']
# claim= claimCanonical['claim']
# print('firstAdmitDt:{}',claim['firstAdmitDt'])
# print('ptCall:{}',claim['ptCall'])


# r = requests.post('http://localhost:8080/CMiC/api/rest/utility/upload360/3561013/RCAL/XXXX/CML',  headers=my_auth)

#3561316

# policy_no_set = set()
# count = 0
# claimidlst = ['3560849','3560919','3560922','3560931','3560937','3560938','3560940','3560946','3560947','3560958','3560959','3560960','3560963','3560972','3560965','3560968','3560969','3560977','3560978','3560981','3560982','3560983','3560984','3560988','3560991','3560992','3560985','3560986','3560987','3560989','3560990','3560995','3561002','3560996','3560998','3560999','3561000','3561001','3561003','3561021','3561023','3561069','3561114','3561166','3561214','3561167','3561168','3561393','3561394']
# for claimid in claimidlst:
#     time.sleep(5)
#     r = requests.post('http://localhost:8080/CMiC/api/rest/utility/pthistorycall/'+ claimid, headers=my_auth)
#     print(r.status_code)
#     print(json.dumps(r.json(), indent=4))
#     print('-----------------------------')
#     output = r.json()
#     datalst = output['data']
#     for data in datalst:
#         policy_no = data['policyNo']
#         policy_no_set.add(policy_no)

# print('policy no total {}'.format(len(policy_no_set)))
# for pol_no in policy_no_set:
#     print(pol_no)

# json_data = '''
#     {
#     "subject": "subject1",
#     "to": "virat.lerlapattana@aia.com",
#     "message": "text body message"
#     }
# '''
# headers={
# 'Authorization': 'Basic bWNsbTAyMjptY2xtMDIy',
# 'Content-type':'application/json', 
# 'Accept':'application/json'
# }
# r = requests.post('http://localhost:8080/CMiC/api/rest/utility/sendMail', data=json_data, headers=headers)
# print(r.status_code)
# print(json.dumps(r.json(), indent=4))

# r = requests.post('http://localhost:8080/CMiC/api/rest/utility/checkstpcriteria/3559688/5001/0',  headers=my_auth)
# print(r.status_code)
# print(json.dumps(r.json(), indent=4))


# r = requests.post('http://localhost:8080/CMiC/api/rest/utility/retrieveClaimDetail/10670598',  headers=my_auth)
# print(r.status_code)
# print(json.dumps(r.json(), indent=4))

# r = requests.post('http://localhost:8080/CMiC/api/rest/utility/edi/248448',  headers=my_auth)
# print(r.status_code)
# print(json.dumps(r.json(), indent=4))

#1227729,C900000730 800
#1227731, C900000732 100
# r = requests.post('http://localhost:8080/CMiC/api/rest/utility/settlementdetaildeducmamt/1227731',  headers=my_auth)
# print(r.status_code)
# print(json.dumps(r.json(), indent=4))


# r = requests.post('http://localhost:8080/CMiC/api/rest/utility/finddocumentbycaseid/18964',  headers=my_auth)
# print(r.status_code)
# print(json.dumps(r.json(), indent=4))
# input();

# r = requests.post('http://localhost:8080/CMiC/api/rest/utility/findclaimpaidbypartyid/395318157',  headers=my_auth)
# print(r.status_code)
# print(json.dumps(r.json(), indent=4))
# input();

# r = requests.post('http://localhost:8080/CMiC/api/rest/utility/retrievededucttransactionlog/1227782',  headers=my_auth)
# print(r.status_code)
# print(json.dumps(r.json(), indent=4))
# input();

# r = requests.post('http://localhost:8080/CMiC/api/rest/utility/retrievedeductclaimlist/00000A1275/0000000091/381020794',  headers=my_auth)
# print(r.status_code)
# print(json.dumps(r.json(), indent=4))
# output = r.json()
# data = output['data']
# data_len = len(data)
# print(f'len(data) is {data_len}')
# input();



# r = requests.post('http://localhost:8080/CMiC/api/rest/utility/findhnwpartybypolicy/T205949937',  headers=my_auth)
# print(r.status_code)
# print(json.dumps(r.json(), indent=4))
# output = r.json()
# data = output['data']
# data_len = len(data)
# print(f'len(data) is {data_len}')
# input();


# r = requests.post('http://localhost:8080/CMiC/api/rest/utility/hnwcarededucts/3565338',  headers=my_auth)
# print(r.status_code)
# print(json.dumps(r.json(), indent=4))
# output = r.json()
# data = output['data']
# data_len = len(data)
# print(f'len(data) is {data_len}')
# input();

# r = requests.post('http://localhost:8080/CMiC/api/rest/utility/listhnwplan/1227875',  headers=my_auth)
# print(r.status_code)
# print(json.dumps(r.json(), indent=4))
# output = r.json()
# data = output['data']
# data_len = len(data)
# print(f'len(data) is {data_len}')
# input();

# r = requests.post('http://localhost:8080/CMiC/api/rest/utility/openEligible/3565338',  headers=my_auth)
# print(r.status_code)
# print(json.dumps(r.json(), indent=4))
# output = r.json()
# data = output['data']
# data_len = len(data)
# print(f'len(data) is {data_len}')
# input();

# r = requests.post('http://localhost:8080/CMiC/api/rest/utility/defaultnhwbenefitcode/C900000815/1/',  headers=my_auth)
# print(r.status_code)
# print(json.dumps(r.json(), indent=4))
# output = r.json()
# data = output['data']
# data_len = len(data)
# print(f'len(data) is {data_len}')
# input();

#claimno = 'C000024246' uat
# claimno = 'C900000814' #sit
# r = requests.post(f'http://localhost:8080/CMiC/api/rest/utility/hnwpaidamount/{claimno}/1/CS',  headers=my_auth)
# print(r.status_code)
# print(json.dumps(r.json(), indent=4))
# output = r.json()
# data = output['data']
# input();

# r = requests.post('http://localhost:8080/CMiC/api/rest/utility/defaulthnwbenefitcode/C000024351/1/0000015551',  headers=my_auth)
# print(r.status_code)
# print(json.dumps(r.json(), indent=4))
# output = r.json()
# data = output['data']
# data_len = len(data)
# print(f'len(data) is {data_len}')
# input();

# r = requests.post('http://localhost:8080/CMiC/api/rest/utility/retrievecsdeduct/3565865/378637514',  headers=my_auth)
# print(r.status_code)
# print(json.dumps(r.json(), indent=4))
# output = r.json()
# data = output['data']
# data_len = len(data)
# print(f'len(data) is {data_len}')
# input();

# r = requests.post('http://localhost:8080/CMiC/api/rest/utility/subamt1/C900000622/1/P703902308/T205950243/243/H25',  headers=my_auth)
# print(r.status_code)
# print(json.dumps(r.json(), indent=4))

# r = requests.post('http://localhost:8080/CMiC/api/rest/utility/subamt2/1227540/P703902308/C900000811/1/T440008002/243/H02',  headers=my_auth)
# print(r.status_code)
# print(json.dumps(r.json(), indent=4))

# r = requests.post('http://localhost:8080/CMiC/api/rest/utility/findpolicyyear/3565865/T205950269',  headers=my_auth)
# print(r.status_code)
# print(json.dumps(r.json(), indent=4))

# r = requests.post('http://localhost:8080/CMiC/api/rest/utility/findamth01/1228125/T205949937/C000024631/1/T205949937/40', headers=my_auth)
# print(r.status_code)
# print(json.dumps(r.json(), indent=4))

# r = requests.post('http://localhost:8080/CMiC/api/rest/utility/totaldeductamt2/0000000446/T205950243', headers=my_auth)
# print(r.status_code)
# print(json.dumps(r.json(), indent=4))

# r = requests.post('http://localhost:8080/CMiC/api/rest/utility/totaldeductamt1/C000023949/1/0000000161/T205950243', headers=my_auth)
# print(r.status_code)
# print(json.dumps(r.json(), indent=4))

# r = requests.post('http://localhost:8080/CMiC/api/rest/utility/retrievepolicy/T205950243', headers=my_auth)
# print(r.status_code)
# print(json.dumps(r.json(), indent=4))

# r = requests.post('http://localhost:8080/CMiC/api/rest/utility/retrieveicd10stp/3567803/false', headers=my_auth)#C000026182 ,|W54.11|
# print(r.status_code) # true
# print(json.dumps(r.json(), indent=4))
# r = requests.post('http://localhost:8080/CMiC/api/rest/utility/retrieveicd10stp/3567518/true', headers=my_auth)#C000025916, V99.5
# print(r.status_code) #false
# print(json.dumps(r.json(), indent=4))
# r = requests.post('http://localhost:8080/CMiC/api/rest/utility/retrieveicd10stp/3567530/false', headers=my_auth)#C000025928, V99.
# print(r.status_code) #false
# print(json.dumps(r.json(), indent=4))


# r = requests.post('http://localhost:8080/CMiC/api/rest/utility/checkstp/12539415/1001010003', headers=my_auth)#C000026182 ,|W54.11|
# print(json.dumps(r.json(), indent=4))

# r = requests.post('http://localhost:8080/CMiC/api/rest/utility/checkpamestp/1229594/', headers=my_auth)#C000026182 ,|W54.11|
# print(json.dumps(r.json(), indent=4))

# r = requests.post('http://localhost:8080/CMiC/api/rest/utility/retrieveclaimdetail/19993', headers=my_auth)
# print(json.dumps(r.json(), indent=4))

# r = requests.post('http://localhost:8080/CMiC/api/rest/utility/hshp/386406564/20118', headers=my_auth) # C900001275
# print(json.dumps(r.json(), indent=4))

#r = requests.post('http://localhost:8080/CMiC/api/rest/utility/previouspaid/1231277/T456193066', headers=my_auth) # C900001507
#print(json.dumps(r.json(), indent=4))



# r = requests.post('http://localhost:8080/CMiC/api/rest/utility/hshp/403070005/20301', headers=my_auth) # C900001507
# print(json.dumps(r.json(), indent=4))

server = 'localhost'
port = 8080
server = 'thadculwcm01'
port = 9080

# r = requests.post('http://localhost:8080/CMiC/api/rest/utility/hshp/403070005/20301', headers=my_auth) # C900001507
# print(json.dumps(r.json(), indent=4))

# r = requests.post('http://localhost:8080/CMiC/api/rest/utility/testprocess/20301', headers=my_auth) # C900001507
# print(json.dumps(r.json(), indent=4))


# r = requests.post('http://localhost:8080/CMiC/api/rest/utility/hshpmaxbenefit/3576860', headers=my_auth) # 
# print(json.dumps(r.json(), indent=4))

# r = requests.post('http://localhost:8080/CMiC/api/rest/utility/hshp/403070090/1151200', headers=my_auth) # C900001507
# print(json.dumps(r.json(), indent=4))

# r = requests.post('http://localhost:8080/CMiC/api/rest/utility/testrequest/T410230949', headers=my_auth) # C900001507
# print(json.dumps(r.json(), indent=4))

r = requests.post('http://localhost:8080/CMiC/api/rest/utility/updatework/20479', headers=my_auth) # C900001507
print(json.dumps(r.json(), indent=4))