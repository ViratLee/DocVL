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
config = load_yaml_config()
cmic_config = config['uat']
now = datetime.datetime.now()
curDt = '{:%Y-%m-%d_%H%M}'.format(now)
output_path = cmic_config['output.path']
#call_retrieve_lookupIgn_tedit_list.py
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
    oFileName = '{}{}_{}_{}.json'.format(output_path,'retrieve_lookup','Resp',curDt)
    with io.open(oFileName,'a',encoding='utf8') as o:
        retrieve_lookup = retrieveLookupTEditList('uat')
        r = retrieve_lookup.callService()
        output = r.json()
        parsed = json.dumps(r.json(), indent=4) 
        write_output_file(o,parsed,True)
        IngTeditList = output['IngTeditList']
        for ingTedit in IngTeditList:
            tableValue = ingTedit['tableValue']
            print('tableValue:{}'.format(tableValue))
            tableValueDesc = ingTedit['tableValueDesc']
            valueDesc = tableValueDesc.split()
            print('valueDesc {}'.format(valueDesc))
            subCode = valueDesc[-1]
            print('subCode {}'.format(subCode))

def main():
    callService()
if __name__ == '__main__':
    main() 