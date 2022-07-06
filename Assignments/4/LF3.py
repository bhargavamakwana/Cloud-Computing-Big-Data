import json
import boto3
from botocore.vendored import requests
# import requests
from boto3.dynamodb.conditions import Key
# from requests_aws4auth import AWS4Auth
ELASTIC_SEARCH_URL = 'https://search-posts1-rm3jkuovm24lobotn7w4dob4mm.us-east-1.es.amazonaws.com/posts1/_search'
region = 'us-east-1'
service = 'es'

cred = boto3.Session().get_credentials()
# awsauth = AWS4Auth(cred.access_key, cred.secret_key, region, service, session_token=cred.token)
sns = boto3.client('sns', region_name='us-east-1')


def lambda_handler(event, context):


    # TODO implement
    print(event)
    dynamodb_res = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb_res.Table('posts')
    # client = boto3.client('dynamodb')
    curr_event = event['currentIntent']['slots'] 
    # return  {
    #     # "sessionAttributes": {},
    #     "dialogAction": {
    #     "type": "Close",
    #     "fulfillmentState": "Fulfilled",
    #     "message": {
    #         "contentType": "PlainText",
    #         "content": "something is wrong"
    #     },
    # }}
    posts = ""
    for keys in curr_event.keys():
        print(curr_event[keys])
        query = {
            "size": 3,
            "query": {
                "multi_match": {
                    "query": str(curr_event[keys])
                }
            }
        }

        # Elasticsearch 6.x requires an explicit Content-Type header
        headers = { "Content-Type": "application/json" }
        url = ELASTIC_SEARCH_URL
        # Make the signed HTTP request

        r = requests.get(url, auth=("theroark", "Shreeji@7"), headers=headers, data=json.dumps(query))

        # Create the response and add some extra content to support CORS


        resp = r.json()
        if resp['hits'] == []:
            return {
                'statusCode': 200,
                'headers': {
                    'Access-Control-Allow-Headers': 'Content-Type',
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
                },
                'body': "No posts found"

            }


        id_list = []
        for documents in resp['hits']["hits"]:
            id_list.append(documents["_id"])


        for ids in id_list:
            res = table.get_item(Key={'id': int(ids)})
            # posts['item'].append(response['Item']['posts'])
            tmp = res['Item']['posts'].replace("'", '"')
            posts += tmp + " "
    if posts is not '':
        sns.publish(TopicArn='arn:aws:sns:us-east-1:930942531032:sns-topic',
                    Message=posts)

        return  {
            "dialogAction": {
            "type": "Close",
            "fulfillmentState": "Fulfilled",
            "message": {
                "contentType": "PlainText",
                "content": posts
            },
        }}
    else:
        return  {
            "dialogAction": {
            "type": "Close",
            "fulfillmentState": "Fulfilled",
            "message": {
                "contentType": "PlainText",
                "content": "No posts found"
            },
        }}
