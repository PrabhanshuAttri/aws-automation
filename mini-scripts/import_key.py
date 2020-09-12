import os
import base64
import struct
import boto3
import paramiko
from paramiko.util import deflate_long
from pathlib import Path
from subprocess import Popen

HOME = str(Path.home())
PEM_FILEPATH = os.path.join(HOME, '.ssh/aws_id_rsa')

def get_key_pair(filepath, email = "user@domain"):
    key_pair_file = Path(filepath)
    if key_pair_file.is_file():
        print('Found ssh key')
    else:
        print('Key Pair Not Found: ', filepath)
        print('Generating Key Pair...')
        key_pair_gen_command = 'ssh-keygen -m pem -t rsa -f {} -q -P "" -C "{}"'.format(str(filepath), email)
        p = Popen(key_pair_gen_command, shell=True)
        p.communicate()
    
    key = paramiko.RSAKey.from_private_key_file(filepath)
    output = b''
    parts = [b'ssh-rsa', deflate_long(key.public_numbers.e), deflate_long(key.public_numbers.n)]

    for part in parts:
        output += struct.pack('>I', len(part)) + part

    public_key = b'ssh-rsa ' + base64.b64encode(output) + b'\n'

    file = open("{}.pub".format(PEM_FILEPATH), "r")
    key_name = file.read().strip().split(' ')[-1]

    return key_name, public_key

ec2 = boto3.resource('ec2')
email = "clone@cloud_computing"
key_pair = ec2.KeyPair(email)
key_pair.delete()

name, key = get_key_pair(PEM_FILEPATH, email)
key_pair_response = ec2.import_key_pair(KeyName=name, PublicKeyMaterial=key)
print('Uploaded to AWS', key_pair_response)

key_pair = ec2.KeyPair(email)
print("Key Id: ", key_pair.key_pair_id)