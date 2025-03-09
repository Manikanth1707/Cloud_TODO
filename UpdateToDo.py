import json
import boto3

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Todos')

    # CORS headers
    cors_headers = {
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Allow-Origin': 'http://todos-application-mini.s3-website-us-east-1.amazonaws.com',
        'Access-Control-Allow-Methods': 'OPTIONS,POST,GET,PUT'
    }
    
    # Parse the request body (expecting it to be passed as JSON)
    try:
        body = json.loads(event.get('body', '{}'))
    except json.JSONDecodeError:
        return {
            'statusCode': 400,
            'headers': cors_headers,
            'body': json.dumps({'error': 'Invalid JSON format'})
        }

    # Check if 'todo_id' and 'status' are in the request body
    todo_id = body.get('todo_id')
    status = body.get('status')

    if not todo_id or not status:
        return {
            'statusCode': 400,
            'headers': cors_headers,
            'body': json.dumps({'error': 'Missing required parameters: todo_id or status'})
        }

    # Update the status of the task in DynamoDB
    try:
        response = table.update_item(
            Key={'TodoID': todo_id},
            UpdateExpression='SET #s = :val',
            ExpressionAttributeNames={'#s': 'Status'},
            ExpressionAttributeValues={':val': status},
            ReturnValues="UPDATED_NEW"
        )
    except Exception as e:
        print(f"Error updating task: {e}")
        return {
            'statusCode': 500,
            'headers': cors_headers,
            'body': json.dumps({'error': 'Error updating task'})
        }
    
    # Return success response with updated attributes
    return {
        'statusCode': 200,
        'headers': cors_headers,
        'body': json.dumps({
            'message': 'Task updated successfully',
            'updatedAttributes': response.get('Attributes', {})
        })
    }
