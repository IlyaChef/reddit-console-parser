import praw
import os
from dotenv import load_dotenv


load_dotenv()


def create_reddit_instance() -> praw.Reddit:
    reddit = praw.Reddit(
        client_id=os.getenv('CLIENT_ID'),
        client_secret=os.getenv('CLIENT_SECRET'),
        username=os.getenv('USERNAME'),
        user_agent=os.getenv('USER_AGENT'),
    )
    return reddit
