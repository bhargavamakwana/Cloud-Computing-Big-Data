import boto3
import json


sns = boto3.client('sns', region_name='us-east-1')

sns.publish(TopicArn='arn:aws:sns:us-east-1:930942531032:sns-topic',
            Message=json.dumps("This is bhargav from SNS"))
