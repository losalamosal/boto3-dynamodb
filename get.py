import boto3

dynamodb = boto3.resource('dynamodb', endpoint_url='http://localhost:8000')
table = dynamodb.Table('speeds')

response = table.get_item(
    Key={
        'date': '2018-02-02',
        'hour': 0
    }
)
item = response['Item']
print(item)

print(table.item_count)
