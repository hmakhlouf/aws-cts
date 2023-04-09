import boto3
import datetime
import base64
import json
import os

def lambda_handler(event, context):
	try: 
		my_region = os.environ['AWS_REGION']
		dynamoDBTableName = os.environ['DYNAMODB_TABLE_NAME']
		dynamo_db = boto3.resource('dynamodb', region_name=my_region)
		table = dynamo_db.Table(dynamoDBTableName)
		
		for record in event["Records"]:
			decoded_data = base64.b64decode(record["kinesis"]["data"]).decode("utf-8")            
			decoded_data_dic = json.loads(decoded_data)

			print(decoded_data_dic)

			with table.batch_writer() as batch_writer:
				batch_writer.put_item(Item=decoded_data_dic)
       
	except Exception as e: 
		print(str(e))
