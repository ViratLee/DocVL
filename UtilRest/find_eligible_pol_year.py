import requests

my_auth = {
    'Authorization': 'Basic bWNsbTAyMjptY2xtMDIy'
}
#r = requests.post('http://localhost:8080/CMiC/api/rest/utility/findEligibleByPolPerYear/T201788956/1151/05/H17',  headers=my_auth)
#r = requests.post('http://localhost:8080/CMiC/api/rest/utility/findEligibleByPolPerYear/T201788956/191/03/A09',  headers=my_auth)
#r = requests.post('http://localhost:8080/CMiC/api/rest/utility/eligibleAmtA09_ME/1224465/P250917260',  headers=my_auth)
print(r.status_code)
print(r.json())   