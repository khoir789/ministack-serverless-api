import json
import boto3
import time
from botocore.exceptions import ClientError

# Koneksi ke DynamoDB lokal MiniStack
dynamodb = boto3.resource('dynamodb', endpoint_url='http://localhost:4566')
table = dynamodb.Table('MyTable') # Pastikan nama tabel sama

def lambda_handler(event, context):
    # Ekstrak 'operation' dan 'payload' dari event yang masuk
    # Struktur event ini akan kita atur nanti di API Gateway
    operation = event.get('operation')
    payload = event.get('payload', {})

    if operation == 'create':
        # Buat ID unik menggunakan timestamp
        item_id = str(int(time.time() * 1000))
        item = {
            'ID': item_id,
            'data': payload.get('data', 'Tidak ada data')
        }
        table.put_item(Item=item)
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Item created', 'id': item_id})
        }

    elif operation == 'read':
        # Baca item berdasarkan ID dari payload
        item_id = payload.get('ID')
        if not item_id:
            return {'statusCode': 400, 'body': json.dumps({'error': 'ID diperlukan'})}
        
        response = table.get_item(Key={'ID': item_id})
        item = response.get('Item')
        if item:
            return {'statusCode': 200, 'body': json.dumps(item)}
        else:
            return {'statusCode': 404, 'body': json.dumps({'error': 'Item tidak ditemukan'})}

    # Tambahkan operasi update dan delete di sini jika diperlukan
    else:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': f'Operasi "{operation}" tidak dikenali'})
        }