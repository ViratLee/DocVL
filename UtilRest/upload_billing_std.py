import requests
import json
import time

my_auth = {
    'Authorization': 'Basic bWNsbTAyMjptY2xtMDIy'
}
target_url = 'http://localhost:8080/CMiC/api/rest/utility/upload'
def write_output_file(o, line, printoutput=False):
    try:
        if printoutput == True:
           text = '{}'.format(line)
           print(text)
        o.write(line)
        o.write("\n")
    except IOError:
        raise
# r = requests.post(target_url,  headers=my_auth)
# print(r.status_code)
# print(json.dumps(r.json(), indent=4))
file_name = 'R00002_w.xlsx'
with open(file_name, 'rb') as f:
    print(f'load {file_name}')
    files = {'file': f}
    r = requests.post(target_url, headers=my_auth,  files=files)