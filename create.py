#!/usr/bin/env python
import boto3

# Get the service resource.
dynamodb = boto3.resource('dynamodb', endpoint_url='http://localhost:8000')

# Create the DynamoDB table.
table = dynamodb.create_table(
    TableName='speeds',
    KeySchema=[
        {
            'AttributeName': 'date',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'hour',
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'date',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'hour',
            'AttributeType': 'N'
        },

    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

# Wait until the table exists.
table.meta.client.get_waiter('table_exists').wait(TableName='speeds')

# Print out some data about the table.
print(table.item_count)
