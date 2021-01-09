import requests
# my_data = {
# 	"username": "asnpahu",
# 	"password": "Password201905",
# 	"newPassword": "",
# 	"type": "ldap",
# 	"secureMode": True,
# 	"additionalInfo": ""
# }
# r = requests.post('https://pvwa-th.aia.biz/PasswordVault/api/auth/ldap/logon',verify=False,  json=my_data)
# print('res code:{}'.format(r.status_code))
# s = requests.session()
# print(type(s))
# print('session:{}:'.format(s))

#import base64
from http.client import HTTPSConnection
from base64 import b64encode

username = 'asnpahu'
password = 'Password201905'
#base64string = base64.encodestring('%s:%s' % (username, password))[:-1]
#req.add_header("Authorization", "Basic %s" % base64string)
userAndPass = b64encode(b"asnpahu:Password201905").decode("ascii")
headers = { 'Authorization' : 'Basic %s' %  userAndPass }

# my_auth = {
#     'Authorization': 'Basic {}'.format(base64string)
# }
#r = requests.post('http://localhost:8080/CMiC/api/rest/utility/findEligibleByPolPerYear/T201788956/1151/05/H17',  headers=my_auth)
#r = requests.post('http://localhost:8080/CMiC/api/rest/utility/findEligibleByPolPerYear/T201788956/191/03/A09',  headers=my_auth)
retrieve_date = {
	"actionType": "Show",
	"reason": "Troubleshoot Production issues"
}
r2 = requests.post('https://pvwa-th.aia.biz/PasswordVault/api/Accounts/2451_5/password/retrieve',verify=False, headers=headers,  json=retrieve_date)
print('retrieve res code:{}'.format(r2.status_code))
