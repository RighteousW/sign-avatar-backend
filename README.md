# Sign Avatar Backend

A production-style backend API for a sign language translation system, supporting text processing, video input, and simulated asynchronous workflows.

## Features

* REST API built with FastAPI
* Text-to-gloss translation endpoint
* Video upload handling for sign prediction
* Simulated async job processing
* Interactive API documentation

## Endpoints

* `GET /health` — service status
* `POST /translate/text-to-gloss` — convert text to gloss
* `POST /predict/video` — upload video for prediction
* `POST /predict/video-async` — submit async processing job
* `GET /jobs/{job_id}` — check job status

## Run Locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Visit: http://127.0.0.1:8000/docs

## Tech Stack

* Python
* FastAPI
* Uvicorn

## Project Structure

```
app/
├── api/
├── models/
├── services/
├── db/
└── main.py
```

## Purpose

This project allows headless transactions and provides endpoints to utilise the multimodal nature of the base project, while demonstrating backend engineering concepts including API design, modular architecture, file handling, and asynchronous processing in the context of a real-world ML system.
