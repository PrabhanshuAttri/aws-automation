import boto3
ec2 = boto3.resource('ec2')
ids = []

if ids:
    print('Deleting: ', ids)
    ec2.instances.filter(InstanceIds=ids).stop()
    ec2.instances.filter(InstanceIds=ids).terminate()