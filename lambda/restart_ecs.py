import boto3

def handler(event, context):
    ecs = boto3.client('ecs')
    ecs.update_service(
        cluster='capstone7-cluster',
        service='capstone7-app-service',
        forceNewDeployment=True
    )
    return {'status': 'ECS service redeployed due to CPU alarm'}
