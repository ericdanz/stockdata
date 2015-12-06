import urllib.request as ur
import simplejson as json

###This is an example call to the api
###This example was written for Python 3


#first make a request to the API endpoint url
req = ur.Request('https://6rthd8ogcg.execute-api.us-east-1.amazonaws.com/prod/stockdata')

#then add the headers - the first is the key for the api
req.add_header('x-api-key','your-key-here')

#next is the content information for the json body
req.add_header('Content-Type','application/json')

#create some data for the request - this is a 'read' operation on the default table, 'stockdata'
#the ticker is the stock ticker, in format EXCHANGE/TICKER
#the date is in the format of YYYYMMDD
#other operations include 'update' and 'create'

data = { "operation":"read","tableRow" :{ "ticker" : "NASDAQ/MSFT", "date": 1, } }

#actually execute the request, and then do something with the response
response = ur.urlopen(req,json.dumps(data).encode('utf-8')).read().decode('utf-8')

#this is the response
print(response)
