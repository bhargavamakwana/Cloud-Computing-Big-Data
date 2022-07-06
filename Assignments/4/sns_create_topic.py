import boto3
import json


sns = boto3.client("sns", region_name='us-east-1')

# create topic
topic_name = 'sns-topic'
create_res = sns.create_topic(Name=topic_name)
topic_arn = create_res.get("TopicArn")


email_sub = sns.subscribe(TopicArn=topic_arn,
                          Protocol='email',
                          Endpoint='bm3125@nyu.edu')





