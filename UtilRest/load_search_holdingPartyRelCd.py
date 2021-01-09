import json
import glob, os
import re
pattern = '[^\/*.+\*\/]'
replace = ''

#'C:\\Users\\asnpatd\\JaspersoftWorkspace\\eFrmWS\\jasper\\jrxml'
dir_path = 'D:\\rest_response\\prod\\RetrievePolicyDetail_2019-10-22'
files = glob.iglob(os.path.join(dir_path,"*.json"))
for file in files:
    print(file)
    with open(file, 'r', encoding='utf8') as f:
        json_text = f.read()
        #this_line = f.readline()
        #print('json_text is {} type'.format(type(json_text)))
        #new_text = re.sub(pattern,replace,json_text)
        #json_text=re.sub("//.*?\n","",json_text)
        json_text=re.sub("/\\*.*?\\*/","",json_text)
        #print('json_text:{}'.format(json_text))
        #break;
        detail_dict = json.loads(json_text)
        policyList = detail_dict['policyList']
        policy = policyList[0]
        holdingList = policy['holdingList']
        for holding in holdingList:
            holdingPartyRelationList = holding['holdingPartyRelationList']
            for hodingPartyRelation in holdingPartyRelationList:
                holdingPartyRelCd = hodingPartyRelation['holdingPartyRelCd']
                partyId = hodingPartyRelation['partyId']
                if holdingPartyRelCd == '18':
                    print('holdingPartyRelCd:{}, partyId:{}'.format(holdingPartyRelCd, partyId))
# # Decode the JSON string into a Python dictionary.
# print('json_text is {} type'.format(type(json_text)))#json_text is <class 'str'> type
# apod_dict = json.loads(json_text)
# print('apod_dict is {} type'.format(type(apod_dict)))#apod_dict is <class 'dict'> type
# print(apod_dict['explanation'])#Meteors have been shooting out from the constellation of Orion...

# # Encode the Python dictionary into a JSON string.
# new_json_string = json.dumps(apod_dict, indent=4)
# print('new_json_string is {} type'.format(type(new_json_string)))#new_json_string is <class 'str'> type
# print(new_json_string)