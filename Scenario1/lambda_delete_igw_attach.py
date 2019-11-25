import json
import boto3

def lambda_handler(event, context):
    vpc_id = event['detail']['requestParameters']['vpcId']
    igw_id = event['detail']['requestParameters']['internetGatewayId']
    ec2 = boto3.client('ec2')
    ret = ec2.detach_internet_gateway(
        DryRun = True,
        InternetGatewayId = igw_id,
        VpcId = vpc_id
    )
    return {
        'statusCode': 200,
        'body': ret
    }

