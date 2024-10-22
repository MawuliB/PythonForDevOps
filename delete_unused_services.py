import boto3
from pprint import pprint

# Create an EC2 client
ec2 = boto3.client('ec2')


# Fetch all the ec2 instances
running_instances = ec2.describe_instances()

# pprint(running_instances)

# Fetch all security groups
security_groups = ec2.describe_security_groups()

# get security group id
sec_ids = []

for reservation in running_instances['Reservations']:
    for instance in reservation['Instances']:
        for sg in instance['SecurityGroups']:
            sec_ids.append(sg['GroupId'])

# delete security groups
for sg in security_groups['SecurityGroups']:
    if sg['GroupName'] != 'default':
        if sg['GroupId'] not in sec_ids:
            print(f"Deleting security group {sg['GroupId']}")
            ec2.delete_security_group(GroupId=sg['GroupId'])
        else:
            print(f"Security group {sg['GroupId']} is being used by an instance")
    else:
        print(f"Skipping default security group {sg['GroupId']}")