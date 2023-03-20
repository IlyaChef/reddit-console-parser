import datetime
from typing import List, Dict, Any, Tuple
from operator import itemgetter
from reddit_instance import create_reddit_instance


def get_subreddit_name():
    subreddit_name = input("Please enter subreddit name: ")
    return subreddit_name


def get_subreddit_posts(subreddit_name: str, days: int) -> List[Dict[str, Any]]:
    reddit = create_reddit_instance()
    subreddit = reddit.subreddit(subreddit_name)
    date_from = datetime.datetime.utcnow() - datetime.timedelta(days=days)
    posts = []
    for post in subreddit.top(limit=40):
        if datetime.datetime.utcfromtimestamp(post.created_utc) >= date_from:
            posts.append({
                'id': post.id,
                'title': post.title,
                'author': post.author.name if post.author else "Unknown",
                'post_url': post.url,
                'num_comments': post.num_comments,
                'comments': post.comments,
                'comment_authors': extract_comment_authors(post.comments)
            })
        print(
            '***', post.title, '***',
            'by', post.author.name,
            '*** comments:', post.num_comments,
            # post.comments.list(),
            # extract_comment_authors(post.comments)
            # post.url
        )
    return posts


def extract_comment_authors(comments) -> List[str]:
    authors = []
    for comment in comments:
        author = comment.author
        if author:
            authors.append(author.name)
    return authors


def get_posts_count_by_user(posts: List[Dict[str, Any]], subreddit_name: str) -> Dict[str, int]:
    reddit = create_reddit_instance()
    subreddit = reddit.subreddit(subreddit_name)
    user_post_count: Dict[str, int] = {}
    for post in subreddit.top(limit=50):
        author = post.author.name
        if author in user_post_count:
            user_post_count[author] += 1
        else:
            user_post_count[author] = 1
    return user_post_count


def get_comments_count_by_user(posts: List[Dict[str, Any]], subreddit_name: str) -> Dict[str, int]:
    reddit = create_reddit_instance()
    subreddit = reddit.subreddit(subreddit_name)
    comments_count: Dict[str, int] = {}
    for comment in subreddit.comments(limit=500):
        author = comment.author
        if author in comments_count:
            comments_count[author] += 1
        else:
            comments_count[author] = 1
    return comments_count


def get_top_users(user_data: Dict[str, int]) -> List[Tuple[str, int]]:
    sorted_user_data = sorted(user_data.items(), key=itemgetter(1), reverse=True)
    return sorted_user_data[0:10]
