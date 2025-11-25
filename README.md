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

