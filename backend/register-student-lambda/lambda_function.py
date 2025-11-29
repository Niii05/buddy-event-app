import json
import pymysql
import os

def lambda_handler(event, context):
    try:
        # Parse body safely
        body = json.loads(event.get("body", "{}"))
        print("Received payload:", body)

        name = body.get("name")
        email = body.get("email")
        interests = body.get("interests")
        event_id = body.get("event_id")

        # Validate required fields
        if not name or not email or not event_id:
            print("Validation failed: missing fields")
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Missing name, email, or event_id"})
            }

        # Connect to DB
        conn = pymysql.connect(
            host=os.environ['DB_HOST'],
            user=os.environ['DB_USER'],
            password=os.environ['DB_PASSWORD'],
            database=os.environ['DB_NAME'],
            connect_timeout=5
        )
        print("Connected to database")

        paired_with = None
        pair_score = 0

        with conn.cursor() as cur:
            # Insert student
            print(f"Inserting student: {name}, {email}")
            cur.execute(
                "INSERT INTO students (name, email, interests) VALUES (%s, %s, %s)",
                (name, email, interests)
            )
            student_id = cur.lastrowid
            print("Inserted student with ID:", student_id)

            # Fetch other students registered for the same event
            cur.execute(
                """
                SELECT s.student_id, s.interests
                FROM students s
                JOIN registrations r ON s.student_id = r.student_id
                WHERE r.event_id = %s AND s.student_id != %s
                """,
                (event_id, student_id)
            )
            others = cur.fetchall()
            print("Other registered students fetched:", others)

            # Find best buddy
            new_set = set(map(str.strip, interests.split(",")))
            best_score = 0
            best_student_id = None

            for other_id, other_interests in others:
                other_set = set(map(str.strip, other_interests.split(",")))
                score = len(new_set & other_set)
                print(f"Comparing with student {other_id}, score {score}")
                if score > best_score:
                    best_score = score
                    best_student_id = other_id

            if best_student_id:
                paired_with = best_student_id
                pair_score = best_score
                print(f"Best buddy found: {paired_with} with score {pair_score}")

            # Insert registration
            print(f"Inserting registration for student {student_id} to event {event_id} with buddy {paired_with}")
            cur.execute(
                "INSERT INTO registrations (student_id, event_id, buddy_id) VALUES (%s, %s, %s)",
                (student_id, event_id, paired_with)
            )
            reg_id = cur.lastrowid
            print("Inserted registration ID:", reg_id)

            conn.commit()
            print("Database commit successful")

        # Return response
        response_body = {
            "reg_id": reg_id,
            "student_id": student_id,
            "message": "Student registered successfully"
        }
        if paired_with:
            response_body["paired_with"] = paired_with
            response_body["pair_score"] = pair_score

        print("Returning response:", response_body)

        return {
            "statusCode": 200,
            "body": json.dumps(response_body),
            "headers": {
                "Access-Control-Allow-Origin": "*",  # CORS header
                "Access-Control-Allow-Headers": "*",
            }
        }

    except pymysql.MySQLError as e:
        print("Database error:", str(e))
        return {
            "statusCode": 500,
            "body": json.dumps({"error": "DB error", "detail": str(e)})
        }

    except Exception as e:
        print("Other error:", str(e))
        return {
            "statusCode": 500,
            "body": json.dumps({"error": "Other error", "detail": str(e)})
        }
