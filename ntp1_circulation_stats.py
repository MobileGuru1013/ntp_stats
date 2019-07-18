import swagger_client
from swagger_client.rest import ApiException
import ast

# create an instance of the API class
ntp1_client = swagger_client.NTP1Api()


def getCircSupply(tokenid):
	try:
		api_response = str(ntp1_client.get_token_holders(tokenid))
		queryResult = ast.literal_eval(api_response)['holders']
		holders = len(queryResult)
		circSupply = sum(holder['amount'] for holder in queryResult)
	except ApiException as e:
		print("Exception when calling NTP1Api->get_token_holders: %s\n" % e)
	return {'supply':circSupply, 'holders':holders}

def runProgram():
	tokenid = 'La3QxvUgFwKz2jjQR2HSrwaKcRgotf4tGVkMJx' #La3QxvUgFwKz2jjQR2HSrwaKcRgotf4tGVkMJx = TRIF / Trifid
	result = getCircSupply(tokenid)
	print('Trifid Circulating Supply: ' + str(result['supply']))
	print('Number of unique addresses holding TRIF / Trifid: ' + str(result['holders']))

runProgram()