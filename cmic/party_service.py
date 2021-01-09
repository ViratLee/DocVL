class partyService:
    """Policy Detail"""
    def __init__(self, partys):
        """
        This is the constructor that lets us create
        objects from this class
        """
        self.partys = partys
 
    def write_output_file(self, o, line, printoutput=False):
	    try:
	        if printoutput == True:
	            text = '{}'.format(line)
	            print(text)
	        o.write(line)
	        o.write("\n")
	    except IOError:
	        raise

    def priorNamelist(self, o):
        party_detail = self.partys[0]
        prior_name_list = party_detail['priorNameList']
        for prior_name in prior_name_list:
            partyId = prior_name['partyId']
            businessKey = prior_name['businessKey']
            self.write_output_file(o,'/*------partyId {}-------------'.format(partyId),True)
            self.write_output_file(o,'------businessKey {}-----------*/'.format(businessKey),True)
