import requests, json, io, datetime#, configparser
from MemberParty import MemberParty
import yaml
def load_yaml_config():
    with open('cmic_config.yaml', 'r') as f:
        yaml_file = yaml.safe_load(f)
        #pp.pprint(yaml_file)
        return yaml_file

config = load_yaml_config()
# config = configparser.ConfigParser()
# config.read('../notebooks/cmic_config.ini')
cmic_config = config['uat']
#print('{} {}'.format(cmic_config['user.auth'], cmic_config['user.password']))
url = cmic_config['webservices.rest.url']
req_headers = { 
    'Authorization': '{} {}'.format(cmic_config['user.auth'], cmic_config['user.password']),
    'User-Agent':'Mozilla/5.0'
}
#dedupe_mode = ', "dedupeMode":"partyDedupe"'
dedupe_mode = ''
url = '{}/{}'.format(url,'rest/AIAService/policy/searchPolicy/SearchPolicyPerlifeByPartyId') 
#party_list =['84746367']
#party_list =['386425486']
#party_list =['386187288'] #HNW
#party_list =['386188396'] #HNW
#party_list =['386436611'] #HNW
#party_list =['379947769']
#party_list = ['380232088','386433586','386179019','396915013','386436611']
#386433586
#386187288
#HNW T205949937/990E07
#party_list = ['393869115']
#party_list = ['386180240','386184429','386187263','386187288','386317473','386369349','386406564','386433306','397217004','398131007','398217002','398217025','398217108','398217128','398217145','403209024']
party_list = ['393869115']
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
def callService():
    count = 0
    now = datetime.datetime.now()
    curDt = '{:%Y-%m-%d_%H%M}'.format(now)
    for partyId in party_list:
        try:
            oFileName = '{}{}_{}_{}_{}.json'.format(output_path,'SearchPolicyPerlifeByPartyId',partyId,'Resp',curDt)
            with io.open(oFileName,'a',encoding='utf8') as o:
                count += 1
                print('###{}###'.format(count))
                json_data_str = '{"partyId":"'+partyId+'","companyId":"1"' + dedupe_mode + '}'
                url_data = {'url': url, 'data': json_data_str }
                get_url = '{url}?json={data}'.format(**url_data)
                request_data = 'request:{}'.format(get_url)
                write_output_file(o,'/*',True)
                write_output_file(o,request_data,True)
                r = requests.get(get_url, headers=req_headers)
                response_code = '-------------response:{}-------------'.format(r.status_code)
                write_output_file(o,response_code,True)
                output = r.json()
                policyPerlifeList = output['policyPerlifeList']
                write_output_file(o,'policy per life size {}'.format(len(policyPerlifeList)), True)
                write_output_file(o,'*/',True)
                parsed = json.dumps(r.json(), indent=4) 
                write_output_file(o,parsed)
                #print('policyPerlifeList len {}'.format(len(policyPerlifeList)))
                # member_party = MemberParty(policyPerlifeList)
                # member_party.find_party_id()
                # polNumSet = member_party.polNumSet
                #polNumSet = find_unique_policyno(policyPerlifeList);
                #print('policyPerLifeList unique len {}'.format(len(polNumSet)))
                #list_all_policy(policyPerlifeList)
                find_hnw_product(policyPerlifeList)
            # for pol in polNumSet:
            #     print(pol)
        except Exception as e:
            print(e)
            break
#party_list = ['375560630','375560644','375571746','375572942','375574655','375694980','375804348','375804370','375804448','375804463','376401989']
#party_list = ['376449901','376785203','376785270','376785274','376785339','376789950','377126654','377274197','377306847','377400628','377726634']
#party_list = ['377728917','377728921','377729012','377729025','378335578','378335666','378357098','378359524','378383118','378392725','378404360']
#party_list = ['378635203','378637514','378637564','378639935','378640064','378640066','378642454','378644617','378644862','378663517']
#party_list = ['378665898','378665960','378670764','378670794','379004378','379143269','379146102','379150397','379152647','379157726']
#party_list = ['379159759','379568649','379947769','379947770','379947771','379947774','380509666','380511532','380756076','380764652']
#party_list = ['380787722','380850951','380919599','380925056','380936279','380936282','380999983','381097097','381101389','381107919']
def callService3():
    count = 0
    with open('party_list5.txt', 'r') as fp:
        line = fp.readline()
        count = 1
        while line:
            print("Line {}: {}".format(count, line.strip()))
    #for partyId in party_list:
            try:
                import time
                time.sleep(5) # Delay for 18 seconds.
                partyId = line.strip()
                oFileName = '{}_{}'.format('SearchPolicyPerlifeByPartyId',partyId)
                #count = count + 1
                json_data_str = '{"partyId":"'+partyId+'","companyId":"1"' + dedupe_mode + '}'
                url_data = {'url': url, 'data': json_data_str }
                get_url = '{url}?json={data}'.format(**url_data)
                request_data = 'request:{}'.format(get_url)
                print(f'###{count}###')
                print(f'{request_data}')
                r = requests.get(get_url, headers=req_headers)
                print(f'-------------response:{r.status_code}-------------')
                output = r.json()
                policyPerlifeList = output['policyPerlifeList']
                found = find_hnw_product(policyPerlifeList)
                if found:
                    write_file(partyId)
            except Exception as e:
                print(e)
                break
            line = fp.readline()
            count += 1
def callService2():
    count = 0
    for partyId in party_list:
        try:
            oFileName = '{}_{}'.format('SearchPolicyPerlifeByPartyId',partyId)
            json_data_str = '{"partyId":"'+partyId+'","companyId":"1"' + dedupe_mode + '}'
            url_data = {'url': url, 'data': json_data_str }
            get_url = '{url}?json={data}'.format(**url_data)
            request_data = 'request:{}'.format(get_url)
            print(f'###{count}###')
            print(f'{request_data}')
            r = requests.get(get_url, headers=req_headers)
            print(f'-------------response:{r.status_code}-------------')
            output = r.json()
            policyPerlifeList = output['policyPerlifeList']
            found = find_hnw_product(policyPerlifeList)
        except Exception as e:
            print(e)
            break

def list_all_policy(policyPerlifeList):
     for policy in policyPerlifeList:
        print(f'partyId: {policy["partyId"]}, covNum: {policy["covNum"]} , polNum: {policy["polNum"]}, productCd: {policy["productCd"]})')

def find_unique_policyno(policyPerlifeList):
    polNumSet = set()
    for policy in policyPerlifeList:
        covNum = policy['covNum']
        partyId = policy['partyId']
        polNum = policy['polNum']
        if polNum not in polNumSet:
          print('covNum {}, partyId {} policy {}'.format(covNum, partyId, polNum))
        polNumSet.add(polNum)
    return polNumSet

def find_hnw_product(policyPerlifeList):
    found = False
    hnw_product = ['990E07','990D07','990F07']
    policy_list=[]
    for policy in policyPerlifeList:
        covNum = policy['covNum']
        productCd = policy['productCd']
        polNum = policy['polNum']
        policyStatus = policy['policyStatus']
        if productCd in hnw_product:
            print(f'HNW {covNum}/{polNum}/{productCd}/{policyStatus}')
            found = True
    return found

def write_file(line):
    oFileName = 'temp.txt'
    with io.open(oFileName,'a+',encoding='utf8') as o:
        o.write(line)
        o.write("\n")

def main():
    #callService2()
    callService2()
if __name__ == '__main__':
    main()        
#parsed = json.loads(r.json())
#print(json.dumps(parsed, indent=4, sort_keys=True)
#output = r.json()
#print(output['code'])
#print(output['message'])
#print(output['data'])
#print(r.headers['content-type'])