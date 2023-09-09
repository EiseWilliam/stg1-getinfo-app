from fastapi import FastAPI
from datetime import datetime

app = FastAPI()


@app.get("/api")
def get_info(slack_name: str, track: str):
    day = datetime.utcnow().strftime("%A")
    time = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    info = {
        "slack_name": slack_name,
        "track": track,
        "current_day": day,
        "utc_time": time,
        "github_file_url": "https://github.com/EiseWilliam/stg1-getinfo-app/blob/main/app.py",
        "github_repo_url": "https://github.com/EiseWilliam/stg1-getinfo-app",
        "status_code": 200,
    }
    return info
