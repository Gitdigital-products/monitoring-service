# Handles webhook/Slack/email notifications for alerts
import httpx

def send_webhook(url: str, payload: dict):
    response = httpx.post(url, json=payload)
    return response.status_code
