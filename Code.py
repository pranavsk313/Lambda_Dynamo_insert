import json 
import boto3

def lambda_handler(event, context):
    try:
        print(event["message"])
        
        client = boto3.resource("dynamodb")
        table = client.Table("learners")
        
        items_to_insert = {
            'Learner_id': '2',
            'Learner_name': 'adttya',
            'learner_location': 'Chh sanbhajinagar'
        }
        
        response = table.put_item(Item=items_to_insert)
        return {
            'statusCode': 200,
            'body': json.dumps('Items inserted successfully')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps('Error: {}'.format(str(e)))
        }
