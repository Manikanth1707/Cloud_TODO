import json
import boto3

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Todos')

    # Fetch all items from the DynamoDB table
    response = table.scan()  # Scan the entire table
    items = response.get('Items', [])  # Get the items from the response

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': 'http://todos-application-mini.s3-website-us-east-1.amazonaws.com',  # Replace with your domain
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        'body': json.dumps(items)  # Return the list of tasks as JSON
    }
