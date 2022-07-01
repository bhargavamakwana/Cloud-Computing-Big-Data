import boto3
from elasticsearch import Elasticsearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth
import requests
import pandas as pd

ELASTIC_SEARCH_URL = 'https://search-posts1-rm3jkuovm24lobotn7w4dob4mm.us-east-1.es.amazonaws.com'
region = 'us-east-1'
service = 'es'

cred = boto3.Session().get_credentials()
awsauth = AWS4Auth(cred.access_key, cred.secret_key, region, service, session_token=cred.token)



payload = {"director": "Burton Tim", "genre":["comedy", "sci-fi"]}

with open('ES.CSV', 'r')as infile:
    for line in infile:
        tags = []
        ids = line.split(',', 1)[0]
        url = ELASTIC_SEARCH_URL + '/posts1/_doc/' + str(ids)
        for word in line.split(',', 1)[1].replace("[", '').replace("]", '').split(','):
            tags.append(str(word).strip('\"').rstrip('"\n'))
        payload = {'tags': tags}
        r = requests.post(url, auth=("theroark", "Shreeji@7"), json=payload)
        print(r.text)
        print(payload)

