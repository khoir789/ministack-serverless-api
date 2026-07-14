import boto3

s3 = boto3.client(
    's3',
    endpoint_url='http://localhost:4566',
    aws_access_key_id='test',
    aws_secret_access_key='test',
    region_name='us-east-1'
)

bucket_name = 'my-data-bucket'

# Buat bucket
print(f"[INFO] Membuat bucket: {bucket_name}")
s3.create_bucket(Bucket=bucket_name)

# Upload file
print("[INFO] Upload file...")
s3.put_object(
    Bucket=bucket_name,
    Key='data/file1.txt',
    Body='Ini adalah isi file pertama'
)
s3.put_object(
    Bucket=bucket_name,
    Key='data/file2.txt',
    Body='Ini adalah isi file kedua'
)
print("[OK] File berhasil diupload!")

# List file
print("[INFO] Daftar file di bucket:")
response = s3.list_objects_v2(Bucket=bucket_name)
if 'Contents' in response:
    for obj in response['Contents']:
        print(f"  - {obj['Key']} ({obj['Size']} bytes)")

# Download file
print("[INFO] Mendownload file...")
response = s3.get_object(Bucket=bucket_name, Key='data/file1.txt')
content = response['Body'].read().decode('utf-8')
print(f"[OK] Isi file1.txt: {content}")