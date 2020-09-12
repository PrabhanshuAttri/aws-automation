import boto3
client = boto3.client('ec2')

id = ''
def reboot_ec2(ec2_instance_id):
    response = client.reboot_instances(
        InstanceIds=[ec2_instance_id]
    )
    return response

reboot_ec2(id)