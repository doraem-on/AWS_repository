# core/alchemist.py
import boto3
import json
import os
import time
from dotenv import load_dotenv

# Load environment variables (AWS Keys)
load_dotenv()

# Initialize the AWS Step Functions Client
# This is our remote control for the cloud workflow
sfn_client = boto3.client(
    'stepfunctions',
    region_name=os.getenv("AWS_REGION"),
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY")
)

STATE_MACHINE_ARN = os.getenv("ALCHEMIST_STATE_MACHINE_ARN")

def start_transcreation_pipeline(s3_video_key, source_lang, target_lang, context_tone="casual"):
    """
    Triggers the AWS Cloud Pipeline to localize the video.
    
    Args:
        s3_video_key (str): The path to the video in your S3 bucket (e.g., 'raw/video1.mp4')
        source_lang (str): Original language (e.g., 'en-US')
        target_lang (str): Desired output (e.g., 'hi-IN')
        context_tone (str): The 'vibe' for the Alchemist (e.g., 'formal', 'funny')
    
    Returns:
        str: The Execution ARN (Tracking ID)
    """
    
    # 1. Prepare the Payload
    # This is the "Job Ticket" we hand to the Project Manager
    payload = {
        "Input": {
            "s3_key": s3_video_key,
            "source_language": source_lang,
            "target_language": target_lang,
            "transcreation_tone": context_tone
        }
    }

    try:
        # 2. Fire and Forget
        response = sfn_client.start_execution(
            stateMachineArn=STATE_MACHINE_ARN,
            name=f"AlchemistJob-{int(time.time())}", # Unique ID for this run
            input=json.dumps(payload)
        )
        
        print(f"✅ Pipeline Triggered! Tracking ID: {response['executionArn']}")
        return response['executionArn']

    except Exception as e:
        print(f"❌ Failed to trigger cloud pipeline: {e}")
        return None

def check_pipeline_status(execution_arn):
    """
    Optional: call this every few seconds to see if the job is done.
    """
    response = sfn_client.describe_execution(executionArn=execution_arn)
    return response['status'] # Returns: RUNNING, SUCCEEDED, or FAILED