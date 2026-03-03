# SHL Assessment Recommendation API

This API recommends SHL assessments based on job description queries.

## How to Run

1. Install dependencies:
pip install -r requirements.txt

2. Run server:
uvicorn app:app --reload

3. Open in browser:
http://127.0.0.1:8000/docs

## Endpoint

POST /recommend

Example Request:
{
  "query": "Looking for Java developer with teamwork skills"
}