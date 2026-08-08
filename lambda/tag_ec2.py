import boto3

def handler(event, context):
    ec2 = boto3.client('ec2')
    ec2.create_tags(
        Resources=['i-0eb3ab78e44edb40b'],
        Tags=[{'Key': 'Status', 'Value': 'investigate'}]
    )
    return {'status': 'EC2 instance tagged for investigation'}
