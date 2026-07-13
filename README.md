# Automated UI/UX Review Agent

## Overview

AI UI/UX Review Agent is an AI-powered application that analyzes web and mobile application screenshots to identify UI/UX issues and generate structured usability reports.

The system leverages a Vision Language Model (Llama Vision) to inspect uploaded screenshots and provide actionable recommendations based on established UI/UX principles.

---

## Features

- Upload application screenshots
- Detect whether the uploaded image is a valid UI screenshot
- Analyze UI/UX using AI
- Identify usability and accessibility issues
- Generate structured JSON reports
- Provide actionable recommendations for developers

---

## Tech Stack

### Backend

- FastAPI
- Python
- Hugging Face Inference API
- Llama 4 Scout Vision Model
- Pydantic
- Pillow
- python-dotenv

---

## Project Structure

```
AI-UI-UX-Review-Agent/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── schemas/
│   │   ├── services/
│   │   └── main.py
│   │
│   └── requirements.txt
│
├── .gitignore
└── README.md
```

---

## Backend Setup

### 1. Clone the Repository

```bash
git clone <repository-url>
```

---

### 2. Navigate to the Backend

```bash
cd backend
```

---

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

---

### 4. Activate the Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

---

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 6. Create a `.env` File

Inside the `backend` folder create a file named:

```
.env
```

Add your Hugging Face API token:

```
HF_TOKEN=your_huggingface_token
```

---

### 7. Run the Backend

```bash
uvicorn app.main:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

---

## Current Functionality

The backend currently supports:

- Image upload
- Image validation
- UI screenshot detection
- AI-powered UI/UX analysis
- JSON response generation
- REST API using FastAPI

---

## Roadmap

### Sprint 1 ✅

- Backend architecture
- FastAPI setup
- Llama Vision integration
- Prompt engineering
- JSON response generation

### Sprint 2 🚧

- React frontend
- Multiple image upload
- Professional dashboard
- UX report interface

### Sprint 3

- PDF report generation
- Multi-screen project analysis
- Report history

### Sprint 4

- Automated screenshot capture
- Playwright integration
- Appium integration

---

## Team

Internship Project

AI-Powered UI/UX Review Agent

---

## Project Status

🚧 Under Development
