#!/usr/bin/env python
import boto3

dynamodb = boto3.resource('dynamodb', endpoint_url='http://localhost:8000')
table = dynamodb.Table('speeds')

response = table.get_item(
    Key={
        'year': '2018',
        'mo-day': '01-23'
    }
)
item = response['Item']
print(item)

print(table.item_count)
