import requests

my_auth = {
    'Authorization': 'Basic bWNsbTAyMjptY2xtMDIy'
}
#r = requests.post('http://localhost:8080/CMiC/api/rest/utility/allocateClaimPayment/1227559',  headers=my_auth)
#r = requests.post('http://localhost:8080/CMiC/api/rest/utility/allocateClaimPayment/1227559/H12/210/02/T212446517',  headers=my_auth)
r = requests.post('http://localhost:8080/CMiC/api/rest/utility/allocateClaimPayment/1227559/H25/999/08/T212446517',  headers=my_auth)
print(r.status_code)
print(r.json())   