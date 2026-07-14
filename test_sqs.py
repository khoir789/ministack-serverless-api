import boto3

sqs = boto3.client(
    'sqs',
    endpoint_url='http://localhost:4566',
    aws_access_key_id='test',
    aws_secret_access_key='test',
    region_name='us-east-1'
)

# Buat queue
print("[INFO] Membuat queue...")
response = sqs.create_queue(
    QueueName='my-test-queue',
    Attributes={'DelaySeconds': '5'}
)
queue_url = response['QueueUrl']
print(f"[OK] Queue berhasil dibuat: {queue_url}")

# Kirim pesan
print("[INFO] Mengirim pesan...")
sqs.send_message(
    QueueUrl=queue_url,
    MessageBody='Hello from MiniStack!'
)
print("[OK] Pesan terkirim!")

# Terima pesan
print("[INFO] Menerima pesan...")
messages = sqs.receive_message(
    QueueUrl=queue_url,
    MaxNumberOfMessages=1,
    WaitTimeSeconds=5
)
if 'Messages' in messages:
    for msg in messages['Messages']:
        print(f"[OK] Pesan diterima: {msg['Body']}")
        # Hapus pesan setelah diproses
        sqs.delete_message(
            QueueUrl=queue_url,
            ReceiptHandle=msg['ReceiptHandle']
        )
        print("[OK] Pesan dihapus dari queue")
else:
    print("[INFO] Tidak ada pesan")