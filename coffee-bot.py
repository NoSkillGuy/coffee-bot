import apiai
import json

CLIENT_ACCESS_TOKEN = '074308fedb6e4967b4271470c334aab8'
DEVELOPER_ACCESS_TOKEN = 'dd1ece53f723419495e421554671081d'

def main():
	# setup agent
	ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)
	request = ai.text_request()
	request.lang = 'en'

	#loop the queries to API.AI so we can have a conversation client-side
	while True:
		user_message = raw_input(" Me   : ")
        	if (user_message == u"exit" or user_message == u"Thanks"):
            		break

		#parse the user input
		request = ai.text_request()
		request.query = user_message

		#query the console with the user input, retrieve the response
		response = json.loads(request.getresponse().read())
		result = response['result']
		fulfillment = result['fulfillment']

		# print the result
		print ' Alex : ' + fulfillment['speech']

	print " Alex : It was nice talking to you, have a nice day!"

main()
