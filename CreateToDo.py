import json
import boto3
import uuid

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Todos')

    # Load the body of the request
    body = json.loads(event.get('body', '{}'))
    task = body.get('task')

    # Check if 'task' is provided
    if not task:
        return {
            'statusCode': 400,
            'headers': {
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Origin': 'http://todos-application-mini.s3-website-us-east-1.amazonaws.com',  # Replace with your domain
                'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
            },
            'body': json.dumps({'error': 'Missing required parameter: task'})
        }

    # Generate a unique ID for the task
    todo_id = str(uuid.uuid4())
    status = 'Pending'

    # Insert the new task into the DynamoDB table
    table.put_item(
        Item={
            'TodoID': todo_id,
            'Task': task,
            'Status': status
        }
    )

    # Return the response with CORS headers
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': 'http://todos-application-mini.s3-website-us-east-1.amazonaws.com',  # Replace with your domain
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        'body': json.dumps({'TodoID': todo_id, 'Task': task, 'Status': status})
    }
