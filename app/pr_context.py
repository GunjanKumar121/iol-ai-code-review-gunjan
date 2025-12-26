import json
import os
import requests


def get_pr_context():
    # Repo info like: GunjanKumar121/iol-ai-code-review-gunjan
    repo = os.environ["GITHUB_REPOSITORY"]

    # GitHub event payload file path
    event_path = os.environ["GITHUB_EVENT_PATH"]

    with open(event_path, "r") as f:
        event = json.load(f)

    pr = event["pull_request"]
    pr_number = pr["number"]
    title = pr["title"]
    body = pr["body"]
    diff_url = pr["diff_url"]

    headers = {
        "Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}",
        "Accept": "application/vnd.github.v3.diff"
    }

    diff = requests.get(diff_url, headers=headers).text

    return {
        "repo": repo,
        "pr_number": pr_number,
        "title": title,
        "body": body,
        "diff": diff
    }

