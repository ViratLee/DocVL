import requests, json, io, datetime, configparser, base64, codecs
import yaml
import pandas as pd
import datetime

def load_yaml_config():
    with open('cmic_config.yaml', 'r') as f:
        yaml_file = yaml.safe_load(f)
        #pp.pprint(yaml_file)
        return yaml_file

# config = configparser.ConfigParser()
# config.read('cmic_config.ini')
config = load_yaml_config()
cmic_config = config['uat']

# config = configparser.ConfigParser()
# config.read('cmic_config.ini')
# cmic_config = config['uat']
#print('{} {}'.format(cmic_config['user.auth'], cmic_config['user.password']))
url = cmic_config['webservices.360.url']
#user_name = 'bclm022'
#password = 'bclm022'
#auth = user_name + ":" + password
#print('auth:{}'.format(auth))
#encode_auth = auth.encode('utf-8')
#print('encode_auth:{}'.format(encode_auth))
#base64_auth = base64.b64encode(encode_auth)
#print('base64_auth:{}'.format(base64_auth))
req_headers = { 
    'Authorization': '{} {}'.format(cmic_config['webservices.360.user.auth'], cmic_config['webservices.360.user.password']),
    #'Authorization': '{} {}'.format(cmic_config['webservices.360.user.auth'], base64_auth),
    'Content-Type':'application/json',
    'User-Agent':'Mozilla/5.0'
}
url = '{}/{}'.format(url,'sonora/cmicrest/workflow/getMyQueue') 
#case_id_list = ['1128080'] #uat
#case_id_list = ['2710180'] #prod

def write_output_file(o, line, printoutput=False):
    try:
        if printoutput == True:
           text = '{}'.format(line)
           print(text)
        o.write(line)
        o.write("\n")
    except IOError:
        raise


post_data = """
[
{
    "policyNo": "",
    "channel": "",
    "providerCode": "",
    "location": "",
    "rowPerPages": 2147483647,
    "startPage": 1,
    "activityList": ["OPD"],
    "userProfile": {
        "userId": "bclm279",
        "companyCode": "051",
        "userName": "SIWAPORN  SIWAPON-NGAM",
        "userType": "NonWF_User",
        "email": "SIWAPORN.SIWAPON-NGAM@aia.com",
        "dept": "NPC",
        "subDept": "",
        "branch": "",
        "region": "HO",
        "group": "CMC_JUNIOR",
        "userAuthForm": [{
                "funcId": "CMIC_DOCTOR_PRC",
                "secLev": "00",
                "secLimit": "0.0000000000"
            }, {
                "funcId": "CMIC_DATAENTRY_MEDICAL_PRC",
                "secLev": "90",
                "secLimit": "0.0000000000"
            }, {
                "funcId": "CMIC_LMT_WI_DAY_GP",
                "secLev": "84",
                "secLimit": "0.0000000000"
            }, {
                "funcId": "CMIC_LMT_HB_AMT_GP",
                "secLev": "THB",
                "secLimit": "50000.0000000000"
            }, {
                "funcId": "CMIC_LMT_AI_AMT_GP",
                "secLev": "THB",
                "secLimit": "30000.0000000000"
            }, {
                "funcId": "CMIC_REPORT_HSM_INQ",
                "secLev": "90",
                "secLimit": "30000.0000000000"
            }, {
                "funcId": "CMIC_OUTSTANDINGWORK_PRC",
                "secLev": "90",
                "secLimit": "30000.0000000000"
            }]
        }
}
]
"""
count = 0
now = datetime.datetime.now()
curDt = '{:%Y-%m-%d_%H%M}'.format(now)
output_path = cmic_config['output.path']
def readJsonDataAsText(jsonkey):
    #with open(data_sumit['case_validate_json'],encoding='utf-8') as f:
    with open(jsonkey,encoding='utf-8') as f:
        content = f.read()
    #print(type(content))
    #print(content)
    return content
def get_my_queue_v1(post_data, activityList):
    try:
        oFileName = '{}{}_{}_{}.json'.format(output_path,'getMyQueue','Resp',curDt)
        with io.open(oFileName,'a',encoding='utf8') as o:
            write_output_file(o,'/*',True)
            print(url)
            print(f'activity:{activityList}')
            write_output_file(o,url,True)
            r = requests.post(url, data=post_data, headers=req_headers, verify=False)
            response_code = '-------------response:{}-------------'.format(r.status_code)
            write_output_file(o,response_code,True)
            write_output_file(o,'*/',True)
            print(r)
            parsed = json.dumps(r.json(), indent=4) 
            write_output_file(o,parsed,True)
            output = r.json()
            code = output['code']
            print(f'{code}')
            data = output['data']
    except Exception as e:
        print(e)
def get_my_queue_v2(post_data, activityList):
    try:
        print(f'{url}')
        print(f'activity:{activityList}')
        r = requests.post(url, data=post_data, headers=req_headers, verify=False)
        response_code = '-------------response:{}-------------'.format(r.status_code)
        print(f'{response_code}')
        output = r.json()
        code = output['code']
        print(f'{code}')
        data = output['data']
        totalRows = data['totalRows']
        print(f'total my queue:{totalRows}')
        resultSets = data['resultSets']
        df = pd.DataFrame(resultSets)
        print(df.columns)
        print(df.shape)
        # print(df.head())
        # print(df.tail())
        if 'activity' in df.columns:
            print('activity exists')
        else: print(' activity not exists ')
        #date1 = datetime.date(2020, 5, 20)#// yyyy, mm, dd
        #df_date_less = df[df['submissionDate']<date1]
        #df['submissionDate'].dt.date
       
        #print(df)
        #df1 = df[['caseId', 'activity','policyNo','partyId']]
        #fillter_by_column_value(df)
        #submission_filter_df = pd.DataFrame({'submissionDate':pd.date_range(start = datetime.datetime(2020,5,20), end = datetime.now())})
        #df1 = df[['caseId', 'activity','policyNo','submissionDate','aging']]
        #print(df1)
        #print(df['activity'].value_counts())
        fillter_partyId_by_column_value(df)
        fillter_by_column_case_id(df)
        #print(df['PreAuthMedical'].value_counts())
        #print(df['policyNo'].value_counts())
        # phase_set = set()
        # activity_dict = gen_activity_dict(activityList)
        # for case_item in resultSets:
        #     phase = case_item['phase']
        #     if phase in activityList:
        #         values = activity_dict.get(phase)
        #     else print('found unwant phase {phase}')
        
    except Exception as e:
        print(e)
def fillter_by_column_case_id(df):
    submission_filter_df = df[['caseId', 'activity','policyNo','submissionDate','aging']]
    print(submission_filter_df)

def fillter_by_column_value(df):
    #dataframe3 = dataframe.loc[:,(dataframe>50).all()]
    #df['aging'] = pd.to_numeric(df['aging']) #convert str to int 
    # raw_data.loc[:,'Mycol'] = pd.to_datetime(raw_data['Mycol'], format='%d%b%Y:%H:%M:%S.%f')
    df.loc[:,'submissionDate'] = pd.to_datetime(df['submissionDate'], format='%m/%d/%Y %H:%M:%S')#convert str to datetime (05/14/2020 15:47:24)
    #df['submissionDate'] = pd.to_datetime(df['submissionDate'], format='%m/%d/%Y %H:%M:%S')#convert str to datetime (05/14/2020 15:47:24)
    submission_filter_df = df[(df['submissionDate'] > '2020-05-10') & (df['submissionDate'] < '2020-05-20')]#filter date between 
    submission_filter_df = submission_filter_df[['caseId', 'activity','policyNo','submissionDate','aging']]
    print(submission_filter_df)

def fillter_partyId_by_column_value(df):
    #df1 = df[['caseId', 'activity','policyNo','partyId']]
    print(df['activity'].value_counts())
    #print(df['phase'].value_counts())
    #print(df1['partyId'].value_counts())


if __name__ == '__main__':
    str_data = readJsonDataAsText('get_my_queue.json')
    my_queue_json = json.loads(str_data)
    #activityList = ["Medical"]
    #activityList = ["Medical","DataEntry"]
    #activityList = ["PreAuthMedical"]
    #activityList = ["PreAuthMedical","PreAuthAdjudication","PreAuthReview"]
    #activityList = ["PreAuthReview"]
    #activityList = ["PreAuthMedical","PreAuthAdjudication"]
    #activityList = ["ManualReview"]
    #activityList = ["Deduct"]
    activityList = ["OPD"]
    my_queue_json["activityList"] = activityList
    p_dat = json.dumps(my_queue_json, indent=4)
    get_my_queue_v1(p_dat, activityList)