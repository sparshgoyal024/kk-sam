import boto3
import json


def lambda_handler(event, context):
    count = 0
    cf = boto3.client('cloudformation')
    cf_resp = cf.list_stacks(StackStatusFilter=['CREATE_COMPLETE'])
    if any(cf_resp):
        count = count + 1

    ddb = boto3.resource('dynamodb')
    table = ddb.Table("rank")
    response = table.scan()
    if any(response['Items']):
        count = count + 1 

    
    if count >= 2:
        return True
    return False