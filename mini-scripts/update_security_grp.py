import boto3
ec2 = boto3.client('ec2')

r = ec2.describe_security_groups(GroupIds=[])

sg = r['SecurityGroups'][0]
print(sg['Description'])

security_group_id = sg['GroupId']

#       protocol, from, to, ip range(0.0.0.0/0 -> public)
rules = [['tcp', 80, 80, "0.0.0.0/0"]]
ip_permissions = []

for rule in rules:
    print(rule)
    a,b,c,d = rule
    ip_permissions.append(
        {
            'IpProtocol': a,
            'FromPort': int(b),
            'ToPort': int(c),
            'IpRanges': [{ 'CidrIp': d }]
        }
    )

print(ip_permissions)

data = ec2.authorize_security_group_ingress(
    GroupId=security_group_id,
    IpPermissions=ip_permissions
    )

print(data)