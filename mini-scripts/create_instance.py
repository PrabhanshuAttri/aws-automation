import boto3
ec2 = boto3.resource('ec2')

image_id = "ami-06b263d6ceff0b3dd"
instance_type = "t2.micro"
key_name = "clone@cloud_computing"

instances = ec2.create_instances(
     ImageId=image_id,
     MinCount=1,
     MaxCount=1,
     InstanceType=instance_type,
     Monitoring={
        'Enabled': False
    },
    KeyName=key_name
 )

print(instances)