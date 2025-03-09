import json
import boto3

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Todos')
    
    # Extract 'todo_id' from the query string parameters
    todo_id = event.get('queryStringParameters', {}).get('todo_id')

    # todo_id = 'ac85b878-6b95-481a-9b77-e6baf0a4d879'

    if not todo_id:
        return {
            'statusCode': 400,
            'headers': {
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Origin': 'http://todos-application-mini.s3-website-us-east-1.amazonaws.com',  # Replace with your domain
                'Access-Control-Allow-Methods': 'OPTIONS,DELETE'
            },
            'body': json.dumps({'error': 'Missing required parameter: todo_id'})
        }
    
    # Delete the task from DynamoDB
    try:
        response = table.delete_item(
            Key={'TodoID': todo_id}
        )
    except Exception as e:
        print(e)
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Origin': 'http://todos-application-mini.s3-website-us-east-1.amazonaws.com',  # Replace with your domain
                'Access-Control-Allow-Methods': 'OPTIONS,DELETE'
            },
            'body': json.dumps({'error': 'Error deleting task'})
        }
    
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': 'http://todos-application-mini.s3-website-us-east-1.amazonaws.com',  # Replace with your domain
            'Access-Control-Allow-Methods': 'OPTIONS,DELETE'
        },
        'body': json.dumps({'message': f'Task with TodoID {todo_id} deleted successfully'})
    }
