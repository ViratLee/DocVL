class MemberParty:
    """A member party"""
    def __init__(self, policyPerlifes):
        """
        This is the constructor that lets us create
        objects from this class
        """
        self.policyPerlifes = policyPerlifes
        self.polNumSet = set()

    def find_party_id(self):
        print('policy per life size {}'.format(len(self.policyPerlifes)))
        for policy in self.policyPerlifes:
            covNum = policy['covNum']
            partyId = policy['partyId']
            polNum = policy['polNum']
            dash = '------------'
            if covNum == 'MEM':
                dash = ''
            #print('{}covNum {}, partyId {} policy {}'.format(dash, covNum, partyId, polNum))
            self.polNumSet.add(polNum)