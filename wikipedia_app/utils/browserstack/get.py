import requests
from dotenv import load_dotenv
import os

load_dotenv()


def video_url(*, session_id):
    session_details = requests.get(
        f'https://api.browserstack.com/app-automate/sessions/{session_id}.json',
        auth=(os.getenv('USER_NAME'), os.getenv('KEY')),
    ).json()
    return session_details['automation_session']['video_url']

