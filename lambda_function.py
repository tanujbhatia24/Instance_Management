import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')

    # Find instances with tag Action=Auto-Stop
    stop_response = ec2.describe_instances(
        Filters=[
            {'Name': 'tag:Action', 'Values': ['tanuj-Auto-Stop']},
            {'Name': 'instance-state-name', 'Values': ['running']}
        ]
    )

    stop_instances = [
        instance['InstanceId']
        for reservation in stop_response['Reservations']
        for instance in reservation['Instances']
    ]

    if stop_instances:
        print(f"Stopping instances: {stop_instances}")
        ec2.stop_instances(InstanceIds=stop_instances)
    else:
        print("No instances found to stop.")

    # Find instances with tag Action=Auto-Start
    start_response = ec2.describe_instances(
        Filters=[
            {'Name': 'tag:Action', 'Values': ['tanuj-Auto-Start']},
            {'Name': 'instance-state-name', 'Values': ['stopped']}
        ]
    )

    start_instances = [
        instance['InstanceId']
        for reservation in start_response['Reservations']
        for instance in reservation['Instances']
    ]

    if start_instances:
        print(f"Starting instances: {start_instances}")
        ec2.start_instances(InstanceIds=start_instances)
    else:
        print("No instances found to start.")

    return {
        'statusCode': 200,
        'body': 'Instance actions completed.'
    }
