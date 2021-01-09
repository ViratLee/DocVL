import requests, json, io

class retrieveClaimDetial:
	
	def __init__(self, cmic_config):
		self.url = cmic_config['webservices.rest.url']
		self.req_headers = { 
			'Authorization': '{} {}'.format(cmic_config['user.auth'], cmic_config['user.password']),#;'Basic QkFQUEVTQjpLbjR5SWFnQEtx', # UAT
			'User-Agent':'Mozilla/5.0'
		}
		self.url = '{}/{}'.format(self.url,'rest/AIAService/claim/retrieveClaim/RetrieveClaimDetail')
		self.output_path = cmic_config['output.path']

	def write_output_file(self, o, line, printoutput=False):
		try:
			if printoutput == True:
				text = '{}'.format(line)
				print(text)
			o.write(line)
			o.write("\n")
		except IOError:
			raise

	def callService(self, claim_id_list, now):
		try:
			curDt = '{:%Y-%m-%d_%H%M}'.format(now)
			oFileName = '{}{}_claimid_{}_{}.json'.format(self.output_path,'RetrieveClaimDetail','Resp',curDt)
			with io.open(oFileName,'a',encoding='utf-8') as o:     
				claimlstStr = ''       
				for clm_id in claim_id_list:
					if claimlstStr : claimlstStr = claimlstStr + "," 
					claimlstStr = claimlstStr + '{"claimId":"'+ clm_id + '","companyId":"1"}'
				claim_id_filter = '[' +claimlstStr+ ']'
				#payload =  '{"resultFilter":"claimBenefitList,claimLossEventInfoList,claimParticipantList,claimPolicyList,policyObj,policyProductObj,caseObj,claimStatusList,finActivityClaimRltnList,paymentList,paymentFormDetailList,claimNotesList,medicalTreatmentObj","claimList":'+claim_id_filter+'}'
				payload = '{"resultFilter":"claimBenefitList,claimLossEventInfoList,claimMedicalTreatmentRelationList,medicalTreatmentList,claimParticipantList,claimPolicyList,claimPolicyCoverageList,claimBenefitCoverageList,policyObj,policyProductObj,caseObj,requirementInfoList,claimNotesList,paymentList,claimStatusList,finActivityClaimRltnList,paymentFormDetailList,medicalTreatmentObj,policyBenefitMasterObj","claimList":'+claim_id_filter+'}'
				url_data = {'url': self.url, 'data': payload }
				get_url = '{url}?json={data}'.format(**url_data)
				request_data = 'get request:{}'.format(get_url)
				self.write_output_file(o,'/*',True)
				self.write_output_file(o,request_data,True)
				r = requests.get(get_url,  headers=self.req_headers,verify=False)
				response_code = '-------------response:{}-------------'.format(r.status_code)
				self.write_output_file(o,response_code,True)
				self.write_output_file(o,'*/',True)
				if r.status_code != 200:
					print('exit')
					return
				parsed = json.dumps(r.json(), indent=4) 
				self.write_output_file(o,parsed,False)
				self.claimDetail(r.json())
		except Exception as e:
			print(e)
			
	def claimDetail(self, output):
		claimList = output['claimList']
		for claim in claimList:
			businessKey = claim['businessKey']
			claimNo = claim['claimNo']
			occurrence = claim['occurrence']
			claimId = claim['claimId']
			print('businessKey:{}'.format(businessKey))
			print('claimNo:{}/{} claimId:{}'.format(claimNo,occurrence,claimId))
			claimLossEventInfoList = claim['claimLossEventInfoList']
			for claimLossEvnInfo in claimLossEventInfoList:
				lossEventType = claimLossEvnInfo['lossEventType']
				lossEventDt   = claimLossEvnInfo['lossEventDt']
				print('         lossEventType:{}, lossEventDt:{}'.format(lossEventType, lossEventDt))
