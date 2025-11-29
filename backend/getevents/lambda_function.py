import json

def lambda_handler(event, context):
    try:
        # Fetch data from RDS (placeholder)
        events = [{"name": "Sample Event", "date": "2025-11-25"}]
        return {"statusCode": 200, "body": json.dumps(events)}
    except Exception as e:
        return {"statusCode": 500, "body": json.dumps({"error": str(e)})}
