import boto3
from pprint import pprint

# Create an EC2 client
ec2 = boto3.client('ec2')

# Retrieve information for all instances
running_instances = ec2.describe_instances()


for instance in running_instances['Reservations']:
    for instance_id in instance['Instances']:
        print("=====================================")
        print(instance_id['InstanceId'])
        print(instance_id['InstanceType'])
        print(instance_id['Tags'][0]['Value'])
        print("=====================================\n")

