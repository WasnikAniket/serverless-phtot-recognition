import boto3
import json

rekognition = boto3.client('rekognition')

def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    response = rekognition.detect_labels(
        Image={'S3Object': {'Bucket': bucket, 'Name': key}},
        MaxLabels=10
    )
    
    labels = [label['Name'] for label in response['Labels']]
    print(f"Image: {key}, Labels: {labels}")
    
    return {
        'statusCode': 200,
        'body': json.dumps({'image': key, 'labels': labels})
    }
