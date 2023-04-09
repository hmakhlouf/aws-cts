import boto3  # import Boto3


def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

    # Table defination
    table = dynamodb.create_table(
        TableName='users2',
        KeySchema=[
            {
                'AttributeName': 'userid',
                'KeyType': 'HASH'  # Partition key
            },
            {
                'AttributeName': 'gender',
                'KeyType': 'RANGE'  # Sort key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'userid',
                # AttributeType defines the data type. 'S' is string type and 'N' is number type
                'AttributeType': 'N'
            },
            {
                'AttributeName': 'gender',
                'AttributeType': 'S'
            },
        ],
        ProvisionedThroughput={
            # ReadCapacityUnits set to 10 strongly consistent reads per second
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5  # WriteCapacityUnits set to 10 writes per second
        }
    )
    print(table.item_count)
    return "Table created !!"
