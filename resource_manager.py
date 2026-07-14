import boto3
import datetime

ec2 = boto3.client(
    'ec2',
    endpoint_url='http://localhost:4566',
    aws_access_key_id='test',
    aws_secret_access_key='test',
    region_name='us-east-1'
)

# Buat VPC dan Subnet
print("[INFO] Membuat VPC...")
vpc = ec2.create_vpc(CidrBlock='10.0.0.0/16')
vpc_id = vpc['Vpc']['VpcId']
print(f"[OK] VPC dibuat: {vpc_id}")

print("[INFO] Membuat Subnet...")
subnet = ec2.create_subnet(
    VpcId=vpc_id,
    CidrBlock='10.0.1.0/24'
)
subnet_id = subnet['Subnet']['SubnetId']
print(f"[OK] Subnet dibuat: {subnet_id}")

# Buat Security Group
print("[INFO] Membuat Security Group...")
sg = ec2.create_security_group(
    GroupName='my-sg',
    Description='Test Security Group'
)
sg_id = sg['GroupId']
print(f"[OK] Security Group dibuat: {sg_id}")

# Jalankan instance
print("[INFO] Menjalankan instance EC2...")
instances = ec2.run_instances(
    ImageId='ami-00000001',
    MinCount=1,
    MaxCount=2,
    InstanceType='t3.micro',
    SubnetId=subnet_id,
    SecurityGroupIds=[sg_id],
    TagSpecifications=[{
        'ResourceType': 'instance',
        'Tags': [{'Key': 'AutoStop', 'Value': 'Yes'}]
    }]
)

instance_ids = [inst['InstanceId'] for inst in instances['Instances']]
print(f"[OK] Instance berjalan: {instance_ids}")

# Lihat semua instance
print("[INFO] Daftar semua instance:")
instances = ec2.describe_instances()
for reservation in instances['Reservations']:
    for instance in reservation['Instances']:
        state = instance['State']['Name']
        print(f"  - {instance['InstanceId']}: {state}")

# Hentikan instance
print("[INFO] Menghentikan instance...")
ec2.stop_instances(InstanceIds=instance_ids)
print(f"[OK] Instance dihentikan: {instance_ids}")