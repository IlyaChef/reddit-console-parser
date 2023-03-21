from reddit_parse import get_subreddit_posts, get_posts_count_by_user, get_comments_count_by_user, get_top_users, \
    get_subreddit_name
from reddit_instance import create_reddit_instance

def reddit_console_parser() -> None:
    reddit = create_reddit_instance()
    subreddit_name = get_subreddit_name()
    days = 3
    posts = get_subreddit_posts(subreddit_name, days, reddit)
    comments_count_by_user = get_comments_count_by_user(posts, subreddit_name, reddit)
    top_commenters = get_top_users(comments_count_by_user)
    posts_count_by_user = get_posts_count_by_user(posts, subreddit_name, reddit)
    top_posters = get_top_users(posts_count_by_user)
    print("*****Top 10 post authors******:")
    for user, count in top_posters:
        print(f"{user}: {count}")
    print("******Top 10 commenters in this subreddit******:")
    for user, count in top_commenters:
        print(f"{user}: {count}")


if __name__ == '__main__':
    reddit_console_parser()
