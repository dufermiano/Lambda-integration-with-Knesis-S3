from __future__ import print_function
import hashlib
import json
import boto3

def lambda_handler(event, context):
    data = json.dumps(event)

    id = hashlib.sha1(str(event)).hexdigest()

    s3 = boto3.client('s3')
    s3.put_object(Bucket= bucket-name, Body=data, Key= id+'.json')

    client = boto3.client('firehose')
    response = client.put_record(
        DeliveryStreamName= firehose-name,
        Record={
            'Data': data
            }
    )
    return { 'response' : response }
    
