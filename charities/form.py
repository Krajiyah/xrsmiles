def sendBTC(userinfo): 
	charity_address=address
	receiving= "1KBGCThhCs1ohCaxCkwasgVMHDNFbrd3RU"
	amt=userinfo.amount
	date= userinfo.date
	charityName= charity_name

	validation=userinfo.validateaddress(charity_address)
	if validation.isvalid:
		print "address is not valid."
		userinfo.isvalid=False
	else if amt<0:
		print "amount is negative."
		userinfo.isvalid=False
	else
		print "address is valid."
		userinfo.sendfrom(getaccount(charity_address), receiving, amt, 0, "sent from " +charityName, amt+ " sent to" + receiving)
		payment=userinfo.getreceivedbyaddress(receiving)
		if(payment==amt):
			print "payment received."
			userinfo.is_transaction_complete= True
			userinfo.isvalid=True
		else
			print "payment not received."
