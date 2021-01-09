import requests

my_auth = {
    'Authorization': 'Basic bWNsbTAyMjptY2xtMDIy'
}
claim_payment_data = {
  "companyId" : "051",
} 
r = requests.get('http://localhost:8080/CMiC/web/claimPaymentTest/allocatePayment?claimId=1224493&companyId=051', headers=my_auth)
print(r.status_code)
print(r.json())   