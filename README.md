# buddy-event-app
Event registration app with buddy pairing based on shared interests

# Buddy Event App

**Description:** Event registration app where students can be auto-paired ("buddies") for events based on shared interests.

## Tech stack
- Frontend: static site hosted on S3 + CloudFront (React optional later)
- Backend: AWS Lambda + API Gateway
- Database: Amazon RDS (MySQL / PostgreSQL)
- Monitoring: CloudWatch

## Day 1 progress
- App idea: Event + Buddy pairing
- API & DB design: (fill below)
GET  /events                     -> list events
POST /events                     -> create event (admin)
DELETE /events/{id}              -> delete event (admin)
POST /register                   -> student registration (attempt buddy match)
GET  /registrations/{event_id}   -> list registrations + buddy info

 -DB schema
- AWS resources: (to be added)
Table: events
- id (INT AUTO_INCREMENT PK)
- name (VARCHAR)
- description (TEXT)
- date (DATETIME)
- interests (VARCHAR) -- comma-separated tags

Table: students
- id (INT AUTO_INCREMENT PK)
- name (VARCHAR)
- email (VARCHAR UNIQUE)
- interests (VARCHAR)

Table: registrations
- id (INT AUTO_INCREMENT PK)
- student_id (FK -> students.id)
- event_id (FK -> events.id)
- buddy_id (FK -> students.id, nullable)
- registered_at (DATETIME)


## Architecture

Here’s a simple ASCII diagram of the system:
[S3 + CloudFront] -> [API Gateway] -> [Lambda functions] -> [RDS (MySQL)]
                     ^ IAM Roles     ^ Security Group
                     |
                   Frontend calls

# ARCHITECTURE DIAGRAM
![Architecture Diagram](docs/images/architecture.png)
 
 **Architecture(S3,rds,lambda)**
 ![Architecture Diagram](docs1/images/architecture.png)


---

## Screenshots

**Registration Page**  
![Registration Page](screenshots/registration.png)

**Dashboard**  
![Dashboard](screenshots/dashboard.png)

---

## How to Run

1. **Frontend:**  
   - Copy `frontend/dist` content to your S3 bucket.  
   - Set CloudFront distribution to serve the S3 bucket.  
   - Make sure your default root object is `index.html`.

2. **Backend:**  
   - Deploy Lambda functions using AWS Console or CLI.  
   - Set environment variables for DB connection: `DB_HOST`, `DB_USER`, `DB_PASSWORD`, `DB_NAME`.  
   - Connect API Gateway to the Lambda functions.

3. **Database:**  
   - Create RDS instance (MySQL/PostgreSQL).  
   - Apply schema above.  

---

## Features Implemented

- Student registration for events
- Buddy pairing based on shared interests
- Dashboard analytics: 
  - Number of students per event
  - Number of buddy pairs per event
  - Top shared interests

---

## Notes

- Email notifications (SES) not implemented yet.
- Frontend is currently static; can later be upgraded with React interactivity.

---

## License

[MIT](LICENSE)

