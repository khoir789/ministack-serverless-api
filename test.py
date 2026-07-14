import boto3

# Koneksi ke MiniStack
s3 = boto3.client(
    's3',
    endpoint_url='http://localhost:4566',
    aws_access_key_id='test',
    aws_secret_access_key='test',
    region_name='us-east-1'
)

print("[INFO] Membuat bucket S3...")
s3.create_bucket(Bucket='my-test-bucket')
print("[OK] Bucket berhasil dibuat!")

print("[INFO] Daftar semua bucket:")
buckets = s3.list_buckets()
for bucket in buckets['Buckets']:
    print(f"  - {bucket['Name']}")
