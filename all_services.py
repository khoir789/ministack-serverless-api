import boto3

# Konfigurasi MiniStack
config = {
    'endpoint_url': 'http://localhost:4566',
    'aws_access_key_id': 'test',
    'aws_secret_access_key': 'test',
    'region_name': 'us-east-1'
}

print("=== TESTING AWS SERVICES WITH MINISTACK ===\n")

# 1. S3
print("1. Testing S3...")
s3 = boto3.client('s3', **config)
s3.create_bucket(Bucket='test-bucket')
s3.put_object(Bucket='test-bucket', Key='hello.txt', Body='Hello MiniStack!')
print("   OK - S3 berfungsi\n")

# 2. DynamoDB
print("2. Testing DynamoDB...")
dynamodb = boto3.client('dynamodb', **config)
dynamodb.create_table(
    TableName='TestTable',
    KeySchema=[{'AttributeName': 'id', 'KeyType': 'HASH'}],
    AttributeDefinitions=[{'AttributeName': 'id', 'AttributeType': 'S'}],
    BillingMode='PAY_PER_REQUEST'
)
dynamodb.put_item(
    TableName='TestTable',
    Item={'id': {'S': '1'}, 'data': {'S': 'test data'}}
)
print("   OK - DynamoDB berfungsi\n")

# 3. SQS
print("3. Testing SQS...")
sqs = boto3.client('sqs', **config)
response = sqs.create_queue(QueueName='test-queue')
queue_url = response['QueueUrl']
sqs.send_message(QueueUrl=queue_url, MessageBody='Hello SQS')
print("   OK - SQS berfungsi\n")

print("=== SEMUA LAYANAN BERJALAN DENGAN BAIK ===")