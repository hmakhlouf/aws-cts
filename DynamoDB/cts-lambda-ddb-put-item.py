import boto3  # import Boto3


def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    
    table = dynamodb.Table('users2')
    print(table.creation_date_time)
    
    table.put_item(
        Item = {
            'userid': 1,
            'gender': 'male',
            'name': 'kanakaraju'
        }
    )
    
    return 'Item added to the table.'
