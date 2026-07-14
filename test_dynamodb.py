import boto3

dynamodb = boto3.client(
    'dynamodb',
    endpoint_url='http://localhost:4566',
    aws_access_key_id='test',
    aws_secret_access_key='test',
    region_name='us-east-1'
)

# Buat tabel
print("[INFO] Membuat tabel Users...")
dynamodb.create_table(
    TableName='Users',
    KeySchema=[
        {'AttributeName': 'userId', 'KeyType': 'HASH'}
    ],
    AttributeDefinitions=[
        {'AttributeName': 'userId', 'AttributeType': 'S'}
    ],
    BillingMode='PAY_PER_REQUEST'
)
print("[OK] Tabel Users berhasil dibuat!")

# Tambahkan data
print("[INFO] Menambahkan data...")
dynamodb.put_item(
    TableName='Users',
    Item={
        'userId': {'S': 'user001'},
        'name': {'S': 'John Doe'},
        'email': {'S': 'john@example.com'}
    }
)
print("[OK] Data berhasil ditambahkan!")

# Baca data
print("[INFO] Membaca data...")
response = dynamodb.get_item(
    TableName='Users',
    Key={'userId': {'S': 'user001'}}
)
print(f"[OK] Data ditemukan: {response['Item']}")

# List semua tabel
tables = dynamodb.list_tables()
print(f"[INFO] Daftar tabel: {tables['TableNames']}")