import boto3

dynamodb = boto3.resource('dynamodb', endpoint_url='http://localhost:8000')
table = dynamodb.Table('speeds')

table.put_item(
   Item={
        'date': '2018-02-02',
        'hour': 0,
        'sn': '34.5',
        'up': 7,
        'dn': '93.89'
    }
)

print(table.item_count)
