#!/usr/bin/env python
import boto3

dynamodb = boto3.resource('dynamodb', endpoint_url='http://localhost:8000')
table = dynamodb.Table('speeds')

table.put_item(
   Item={
        'year': '2018',
        'mo-day': '01-23',
        'sn': '34.5',
        'up': ['7.23', '6.89', '5.23', '8.09'],
        'dn': ['93.89', '130.09', '34.23', '56.6', '45.09', '99.99']
    }
)

print(table.item_count)
