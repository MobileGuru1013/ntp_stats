import json
import requests

def getHolders(tokenid):
	while True:
		try:
			url = 'https://ntp1node.nebl.io/ntp1/stakeholders/' + str(tokenid)
			query_string = requests.get(url).text
			returnValue = json.loads(query_string)['holders']
			break
		except Exception as e:
			print(e)
			print('Error from API call, retrying...')
			time.sleep(1)
			continue
	return returnValue


def getCircSupply(li):
	circSupply = sum(holder['amount'] for holder in li)
	print('Number of holders: ' + str(len(li)))
	print('Circulating supply: ' + str(circSupply))

def getTop(li, num):
	sortedList = sorted(li,key=lambda x: x['amount'],reverse=True)[:num]
	print(sortedList)

def runProgram():
	tokenid = 'La3QxvUgFwKz2jjQR2HSrwaKcRgotf4tGVkMJx' #TRIF: La3QxvUgFwKz2jjQR2HSrwaKcRgotf4tGVkMJx
	holders = getHolders(tokenid)
	getCircSupply(holders)
	getTop(holders, 10)

runProgram()