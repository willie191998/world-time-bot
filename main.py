event = {'version': '2.0', 'routeKey': '$default', 'rawPath': '/', 'rawQueryString': '', 'headers': {'content-length': '1275', 'x-amzn-tls-version': 'TLSv1.2', 'x-forwarded-proto': 'https', 'x-forwarded-port': '443', 'x-forwarded-for': '74.125.209.2', 'accept': '*/*', 'authorization': 'Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjVkZjFmOTQ1ZmY5MDZhZWFlZmE5M2MyNzY5OGRiNDA2ZDYwNmIwZTgiLCJ0eXAiOiJKV1QifQ.eyJhdWQiOiJodHRwczovL3I3ZndndWhramUyNWJzeDdtcGN2cGZpeXBlMHJzbWJoLmxhbWJkYS11cmwudXMtZWFzdC0yLm9uLmF3cy8iLCJhenAiOiIxMTM0ODU1Mjg2NDA4OTA0MTY2MDAiLCJlbWFpbCI6InNlcnZpY2UtNzg1ODQ5MTIyNjQ2QGdjcC1zYS1kaWFsb2dmbG93LmlhbS5nc2VydmljZWFjY291bnQuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImV4cCI6MTY3ODc3MjA2NywiaWF0IjoxNjc4NzY4NDY3LCJpc3MiOiJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20iLCJzdWIiOiIxMTM0ODU1Mjg2NDA4OTA0MTY2MDAifQ.YFSWMgdIoU8ZXDkdyhKpmj5MOw-O4zrUQyNAT20QDxTOIDzJ9n3ph2Dg7otB7_DB0TgSn11IwW4WZW_ZIhAC7XDsBvdZoQcDr1l8BeNZnRwWXZiBJDuoPW2pLMB-GcZhrTClWRbdrwL7ADHsEiXHnUVoTc6D5rEEDRauCZCskxOT5R-FLIIrinItnLHOyMxgdRYFV8IuEU9N1unFkQwTzXVKX9M1OFwk4-Kmy6Ylacz3UplCfl6MP18qGPVEyP5pLNfoR30j0_gz8WuU8ZOpZK62p40yMNe1UKVjR_sjXBOcC7ZOgUOCxK1DH0XtK9CKfgUJSLI0F7BwT0T-HkMQeA', 'x-amzn-tls-cipher-suite': 'ECDHE-RSA-AES128-GCM-SHA256', 'x-amzn-trace-id': 'Root=1-640ff953-14a39b6644f96de56acf0550', 'host': 'r7fwguhkje25bsx7mpcvpfiype0rsmbh.lambda-url.us-east-2.on.aws', 'content-type': 'application/json', 'accept-encoding': 'gzip, deflate, br', 'user-agent': 'Google-Dialogflow'}, 'requestContext': {'accountId': 'anonymous', 'apiId': 'r7fwguhkje25bsx7mpcvpfiype0rsmbh', 'domainName': 'r7fwguhkje25bsx7mpcvpfiype0rsmbh.lambda-url.us-east-2.on.aws', 'domainPrefix': 'r7fwguhkje25bsx7mpcvpfiype0rsmbh', 'http': {'method': 'POST', 'path': '/', 'protocol': 'HTTP/1.1', 'sourceIp': '74.125.209.2', 'userAgent': 'Google-Dialogflow'}, 'requestId': 'cfe024bd-ffaf-468a-b77b-3405600497de', 'routeKey': '$default', 'stage': '$default', 'time': '14/Mar/2023:04:34:27 +0000', 'timeEpoch': 1678768467532}, 'body': '{\n  "responseId": "10dd32ef-23eb-452e-9880-2ad043936a6e-0504e25d",\n  "queryResult": {\n    "queryText": "get the timezones",\n    "action": "get_list_of_timezones",\n    "parameters": {\n    },\n    "allRequiredParamsPresent": true,\n    "fulfillmentText": "sorry, the system is not responding now.",\n    "fulfillmentMessages": [{\n      "text": {\n        "text": ["sorry, the system is not responding now."]\n      }\n    }],\n    "outputContexts": [{\n      "name": "projects/world-time-bot-kblm/locations/global/agent/sessions/b8551e71-cefd-fa22-50d8-5baded2d60b5/contexts/__system_counters__",\n      "parameters": {\n        "no-input": 0.0,\n        "no-match": 0.0\n      }\n    }],\n    "intent": {\n      "name": "projects/world-time-bot-kblm/locations/global/agent/intents/165bb132-65b9-4686-91c6-8b251df5b614",\n      "displayName": "get list of timezones in the world"\n    },\n    "intentDetectionConfidence": 1.0,\n    "languageCode": "en",\n    "sentimentAnalysisResult": {\n      "queryTextSentiment": {\n        "score": 0.2,\n        "magnitude": 0.2\n      }\n    }\n  },\n  "originalDetectIntentRequest": {\n    "source": "DIALOGFLOW_CONSOLE",\n    "payload": {\n    }\n  },\n  "session": "projects/world-time-bot-kblm/locations/global/agent/sessions/b8551e71-cefd-fa22-50d8-5baded2d60b5"\n}', 'isBase64Encoded': False}
context = {'yes': '3.0'}

import json

def lambda_handler(event, context):
  query_body_str = event["body"]
  query_body_dict = json.loads(query_body_str)
  query_action = (query_body_dict["queryResult"])["action"]
  
    
  if query_action == "get_list_of_timezones" :
    user_intent = "these are the list of timezones"
        
  else :
    user_intent = "none"
        
  return {
        "statusCode": 200,
        "body": {
            "fulfillmentMessages": [
                              {
                                "text": {
                                   "text": [
                                      user_intent
                                         ]
      }
    }
   ]
  }
}
    

print(lambda_handler(event, context))