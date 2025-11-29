import pymysql, os, json

def lambda_handler(event, context):
    try:
        event_id = event['pathParameters']['event_id']
        conn = pymysql.connect(host=os.environ['DB_HOST'], user=os.environ['DB_USER'],
            password=os.environ['DB_PASSWORD'], database=os.environ['DB_NAME'], connect_timeout=5)

        with conn.cursor(pymysql.cursors.DictCursor) as cur:
            cur.execute("""
                SELECT r.reg_id, r.student_id, s.name, s.interests, r.buddy_id, r.registered_at
                FROM registrations r
                JOIN students s ON r.student_id = s.student_id
                WHERE r.event_id = %s
            """, (event_id,))
            regs = cur.fetchall()

            # Optionally fetch buddy names for those with buddy_id
            student_ids_with_buddy = [r['buddy_id'] for r in regs if r['buddy_id']]
            buddy_names = {}
            if student_ids_with_buddy:
                cur.execute("SELECT student_id, name FROM students WHERE student_id IN (%s)" %
                            ",".join(["%s"] * len(student_ids_with_buddy)), tuple(student_ids_with_buddy))
                rows = cur.fetchall()
                for row in rows:
                    buddy_names[row['student_id']] = row['name']

            for r in regs:
                if r['buddy_id']:
                    r['buddy_name'] = buddy_names.get(r['buddy_id'])

        return {"statusCode": 200, "body": json.dumps({"registrations": regs}, default=str)}

    except Exception as e:
        return {"statusCode": 500, "body": json.dumps({"error": str(e)})}
