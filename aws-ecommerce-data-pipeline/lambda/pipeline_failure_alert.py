import boto3
import json
import os
from datetime import datetime

# Initialize SNS client
# boto3 is the AWS SDK for Python — it lets Lambda talk to other AWS services
sns = boto3.client('sns')

# SNS Topic ARN — we'll set this as an environment variable
# so we don't hardcode sensitive values in the code
TOPIC_ARN = os.environ['SNS_TOPIC_ARN']

def lambda_handler(event, context):
    """
    This function is triggered when Step Functions detects a failure.
    It sends an email alert via SNS with details about what failed.
    
    'event' contains the failure details passed from Step Functions
    'context' contains Lambda runtime information (not used here)
    """
    
    # Extract failure details from the event
    # Step Functions passes error information when it triggers Lambda
    error = event.get('error', 'Unknown error')
    cause = event.get('cause', 'Unknown cause')
    execution_id = event.get('execution_id', 'Unknown execution')
    failed_state = event.get('failed_state', 'Unknown state')
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')
    
    # Build the email message
    # This is what you'll receive in your inbox when the pipeline fails
    message = f"""
    OLIST PIPELINE FAILURE ALERT 
    
    Timestamp:      {timestamp}
    Execution ID:   {execution_id}
    Failed State:   {failed_state}
    Error:          {error}
    Cause:          {cause}
    
    Action Required:
    1. Go to AWS Step Functions console
    2. Find execution: {execution_id}
    3. Check CloudWatch logs for detailed error
    
    CloudWatch Logs:
    https://eu-north-1.console.aws.amazon.com/cloudwatch/home
    """
    
    # Send the email via SNS
    # SNS takes our message and delivers it to all subscribers
    # (in this case, your email address)
    response = sns.publish(
        TopicArn=TOPIC_ARN,
        Subject='⚠️ Olist Pipeline Failed',
        Message=message
    )
    
    print(f"Alert sent! Message ID: {response['MessageId']}")
    
    # Return the response for logging purposes
    return {
        'statusCode': 200,
        'message_id': response['MessageId'],
        'alert_sent_at': timestamp
    }
