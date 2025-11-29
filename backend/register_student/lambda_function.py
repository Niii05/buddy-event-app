import json

def lambda_handler(event, context):
    try:
        if event.get('httpMethod') != 'POST':
            return {'statusCode': 405, 'body': json.dumps({'error': 'Method not allowed'})}

        # Parse POST body
        body = json.loads(event.get('body', '{}'))
        student_name = body.get('name')
        student_email = body.get('email')
        student_roll = body.get('roll')

        # Placeholder: normally insert into RDS here
        response = {
            "message": "Student registered successfully",
            "name": student_name,
            "email": student_email,
            "roll": student_roll
        }

        return {'statusCode': 200, 'body': json.dumps(response)}

    except Exception as e:
        return {'statusCode': 500, 'body': json.dumps({'error': str(e)})}
