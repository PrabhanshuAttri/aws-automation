import os
import boto3
import botocore
import paramiko
from pathlib import Path

HOME = str(Path.home())
PEM_FILEPATH = os.path.join(HOME, '.ssh/aws_id_rsa')

user_name = 'ubuntu'
ip = ''

key = paramiko.RSAKey.from_private_key_file(PEM_FILEPATH)
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

commands = [
    'sudo apt-get install curl -y',
    'curl -o- https://raw.githubusercontent.com/PrabhanshuAttri/aws-automation/master/setup/generic.sh | bash'
]

try:
    client.connect(hostname=ip, username=user_name, pkey=key)
    for c in commands:
        stdin, stdout, stderr = client.exec_command(c)
        print(str(stdout.read()))
    client.close()
except (Exception, e):
    print(e)