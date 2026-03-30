
# GitHub API FastAPI Project

## 📌 Overview

This project is a FastAPI-based backend application that interacts with the GitHub API.
It allows users to fetch and display data such as repositories and issues using REST endpoints.

---

## 🚀 Features

* Fetch GitHub repositories of a user
* Fetch issues from a repository
* Simple and clean API endpoints
* Built using FastAPI

---

## 🛠️ Tech Stack

* Python
* FastAPI
* Uvicorn
* Requests

---

## ⚙️ Setup & Run Locally

### 1. Clone the repository

git clone https://github.com/Prajakta17-bod/github-api-fastapi.git

### 2. Navigate to project folder

cd github-api-fastapi

### 3. Create virtual environment

python -m venv venv

### 4. Activate virtual environment (Windows PowerShell)

.\venv\Scripts\Activate.ps1

### 5. Install dependencies

pip install -r requirements.txt

### 6. Run the server

uvicorn main:app --reload

---

## 🔐 Environment Variables

Create a `.env` file in the root directory and add:

GITHUB_TOKEN=your_github_token_here

---

## 📍 API Endpoints (Example)

* /repos/{username}
* /issues/{owner}/{repo}

---

## 📬 Notes

* Make sure your GitHub token is valid
* Do not share your `.env` file publicly

---

## 👩‍💻 Author

Prajakta



.\venv\Scripts\Activate.ps1
