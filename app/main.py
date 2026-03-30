from fastapi import FastAPI
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

@app.get("/")
def home():
   return {"message": "API is working"}

@app.get("/repos")
def get_repos():
    url = "https://api.github.com/user/repos"

    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}"
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    clean_data = []

    for repo in data:
        clean_data.append({
            "name": repo["name"],
            "full_name": repo["full_name"],
            "private": repo["private"],
            "url": repo["html_url"]
        })

    return clean_data
    
@app.get("/issues")
def get_issues(owner: str, repo: str):
    url = f"https://api.github.com/repos/{owner}/{repo}/issues"

    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}"
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    clean_issues = []

    for issue in data:
        clean_issues.append({
            "title": issue["title"],
            "url": issue["html_url"],
            "state": issue["state"]
        })

    return clean_issues

@app.post("/create-issue")
def create_issue(owner: str, repo: str, title: str, body: str):
    url = f"https://api.github.com/repos/{owner}/{repo}/issues"

    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json"
    }

    data = {
        "title": title,
        "body": body
    }

    response = requests.post(url, headers=headers, json=data)

    return {
        "status_code": response.status_code,
        "response": response.json()
    }