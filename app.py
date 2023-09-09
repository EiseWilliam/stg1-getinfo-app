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
        "github_file_url": "Your GitHub File URL",
        "github_repo_url": "Your GitHub Repo URL",
        "status_code": 200,
    }
    return info
