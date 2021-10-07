import boto3
ec2 = boto3.resource('ec2')
ec2.Instance('i-0a103c316609ecf5f').stop()