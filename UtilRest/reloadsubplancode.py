import requests

my_auth = {
    'Authorization': 'Basic bWNsbTAyMjptY2xtMDIy'
}
# claim_payment_data = {
#   "companyId" : "051",
# } 
# r = requests.get('https://thadcplwcm11:9043/ibm/console',verify=False)#, headers=my_auth)
# print(type(r))
# print('---------------------------------------------------------')
# print(r)   
# s = requests.session()
# print(type(s))
# print('session:{}:'.format(s))

prd1 = 'thadcplwcm11'
prd2 = 'thadcplwcm12'
prd3 = 'thadcplwcm13'

uat1 = 'thadculwcm01'
uat2 = 'thadculwcm02'

sit = 'thadcdlwcm01'
url = 'http://{}:9080/CMiC/api/rest/utility/subplancode/R2'.format(prd2)
r1 = requests.get( url,verify=False, headers=my_auth)
print(' ####### {} ########'.format(url))
print(r1.content)

# url = 'http://{}:9080/CMiC/api/rest/utility/subplancode/R2'.format(prd2)
# r2 = s.get(url,verify=False, headers=my_auth)
# print(' ####### {} ########'.format(url))
# print(r2.content)


# url = 'http://{}:9080/CMiC/api/rest/utility/subplancode/R2'.format(prd3)
# r3 = s.get(url,verify=False, headers=my_auth)
# print(' ####### {} ########'.format(url))
# print(r3.content)

# from http.client import HTTPSConnection
# from base64 import b64encode
# #This sets up the https connection
# c = HTTPSConnection("http://thadcplwcm11/CMiC/api/rest/utility/subplancode/R2",port=9080)
# #we need to base 64 encode it 
# #and then decode it to acsii as python 3 stores it as a byte string
# userAndPass = b64encode(b"bclm022:bclm022").decode("ascii")
# headers = { 'Authorization' : 'Basic %s' %  userAndPass }
# #then connect
# c.request('GET', '/', headers=headers)
# #get the response back
# res = c.getresponse()
# # at this point you could check the status etc
# # this gets the page text
# data = res.read()  
# print(data)