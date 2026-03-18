import uuid

jobs = {}

def create_job():
    job_id = str(uuid.uuid4())
    jobs[job_id] = {"status": "processing"}
    return job_id

def get_job(job_id: str):
    return jobs.get(job_id, {"status": "not found"})

def complete_job(job_id: str):
    jobs[job_id] = {"status": "completed"}