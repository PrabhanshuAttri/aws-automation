import boto3
ec2 = boto3.client('ec2')

ids = ['']
def reboot_ec2(ec2_instance_id):
    response = client.reboot_instances(
        InstanceIds=ids,
        DryRun=True # change to fals to usd
    )
    return response

reboot_ec2(my_ec2_instance_id)