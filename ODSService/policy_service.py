class policyService:
    """Policy Detail"""
    def __init__(self, policy ):
        """
        This is the constructor that lets us create
        objects from this class
        """
        self.policy = policy
 
    def write_output_file(self, o, line, printoutput=False):
	    try:
	        if printoutput == True:
	            text = '{}'.format(line)
	            print(text)
	        o.write(line)
	        o.write("\n")
	    except IOError:
	        raise

    def holding(self, o, policy_number):
        holdingList = self.policy['holdingList']
        holding = holdingList[0]
        holdingPartyRelationList = holding['holdingPartyRelationList']
        self.write_output_file(o,'/*------polno {}-------------'.format(policy_number),True)
        for holdingPartyRelation in holdingPartyRelationList:
            holdingPartyRelCd = holdingPartyRelation['holdingPartyRelCd']
            holding_party = holdingPartyRelation['partyId']
            businessKey = holdingPartyRelation['businessKey']
            if holdingPartyRelCd == '18':
                clientName_seq_num = holdingPartyRelation['clientNameSeqNum'] 
                clientName_type_cd = holdingPartyRelation['clientNameTypeCd']
                bu = businessKey.split(":")
                source = bu[0]
                th = bu[1]
                client_id = bu[4]
                self.write_output_file(o,'holdingPartyRelCd:{} - partyId:{} - businessKey:{} - '.format(holdingPartyRelCd, holding_party, businessKey),True)
                business_key1 = '{}:{}:{}:TH:{}:{}'.format(source,th,client_id,clientName_type_cd,clientName_seq_num)
                self.write_output_file(o,business_key1,True)
                business_key2 = '{}:{}:{}:AL:{}:{}'.format(source,th,client_id,clientName_type_cd,clientName_seq_num)
                self.write_output_file(o,business_key2,True)
            else:
                self.write_output_file(o,'holdingPartyRelCd:{} - partyId:{} - businessKey:{}'.format(holdingPartyRelCd, holding_party, businessKey),True)
        self.write_output_file(o,'---------------------------*/',True)

    def coverage(self, o, policy_number):
        count = 0
        console_print = True
        coverage_list = self.policy['coverageList']
        for coverage in coverage_list:
            covNum = coverage["covNum"]
            console_print = True if covNum == '01' else False
            self.write_output_file(o, '/* coverage[{}] - covNum:{} */'.format(count, covNum), console_print )
            coveragePartyRelation_list = coverage['coveragePartyRelationList']
            for coverage_party_relation in coveragePartyRelation_list:
                coveragePartyRelCd = coverage_party_relation['coveragePartyRelCd']
                coverage_party = coverage_party_relation['partyId']
                coveragePartyRelId = coverage_party_relation['coveragePartyRelId']
                businessKey = coverage_party_relation['businessKey']
                console_print = True if covNum == '01' and coveragePartyRelCd == '1' else False
                self.write_output_file(o, '/* coveragePartyRelCd {} - partyId {} - businessKey {} */'.format(coveragePartyRelCd, coverage_party, businessKey), console_print )
            count += 1
    # def unique_policy_number(self, o, policy_per_lifes):
    #     polNumSet = set()
    #     for policy in policy_per_lifes:
    #         polNum = policy['polNum']
    #         polNumSet.add(polNum)
    #     return polNumSet
    def unique_policy_number(self, o, policy_per_lifes):
        polNumSet = set()
        polNo = []
        for policy in policy_per_lifes:
            polNum = policy['polNum']
            if polNum in polNo:
                continue
            polNo.append(polNum)
            polNumSet.add(policy)
        return polNumSet

    def all_coverage(self):
        coverage_list = self.policy['coverageList']
        for coverage in coverage_list:
            message = (
                f"covNum:{coverage['covNum']},"
                f"productCd:{coverage['productCd']},"
                f"lifeCovStatus:{coverage['lifeCovStatus']}"
            )
            print(message)
    def policy_status(self):
        policyStatusList = self.policy['policyStatusList']
        for policy_status in policyStatusList:
            policy_status['policyStatus']
            print(f'policy status:{policy_status["policyStatus"]}')
    def findOwnerPartyId(self):
        print('-----find owner party-----')
        holdingList = self.policy['holdingList']
        holding = holdingList[0]
        holdingPartyRelationList = holding['holdingPartyRelationList']
        for holdingPartyRelation in holdingPartyRelationList:
            holdingPartyRelCd = holdingPartyRelation['holdingPartyRelCd']
            partyId = holdingPartyRelation['partyId']
            ownerPartyId = ''
            if holdingPartyRelCd == '18':
                ownerPartyId = ' this is ownere party id'
                print(f'    holdingPartyRelCd:{holdingPartyRelCd} - owner partyId:{partyId} ')
    def findInsureParty(self):
        print('-----find insure party-----')
        coverageList = self.policy['coverageList']
        partyId = ''
        for coverage in coverageList:
            if partyId:
                break
            covNum = coverage['covNum']
            if covNum == '01':
                coveragePartyRelationList = coverage['coveragePartyRelationList']
                for coveragePartyRelation in coveragePartyRelationList:
                    coveragePartyRelCd = coveragePartyRelation['coveragePartyRelCd']
                    if coveragePartyRelCd == '1' :
                        partyId = coveragePartyRelation['partyId']
                        print(f'    covNum:{covNum} coveragePartyRelCd:{coveragePartyRelCd} - insure partyId:{partyId} ')
                        break