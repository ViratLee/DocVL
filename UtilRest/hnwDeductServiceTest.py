import requests
import json
import time

my_auth = {
    'Authorization': 'Basic bWNsbTAyMjptY2xtMDIy',
    'Content-type':'application/json', 
    'Accept':'application/json'
}



def readJsonDataAsText(file_data):
    print('readJson')
    with open(file_data,encoding='utf-8') as f:
        content = f.read()
    return content   

def write_output_file(o, line, printoutput=False):
    try:
        if printoutput == True:
           text = '{}'.format(line)
           print(text)
        o.write(line)
        o.write("\n")
    except IOError:
        raise

json_file = "hnw_deduct.json"
p_dat = readJsonDataAsText(json_file)

r = requests.post('http://localhost:8080/CMiC/api/rest/claim/hnwcarededucts', data=p_dat,  headers=my_auth)
print(r.status_code)
print(json.dumps(r.json(), indent=4))