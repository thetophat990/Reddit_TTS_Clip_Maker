from praw import Reddit                    # Used To access Reddits API
from re import sub                         # Used to filter string to be ASCII-Only
from praw.models import MoreComments       # Requierd to handle more comments error
from random import randint                 # For random post selection

rand_index = lambda i: randint(0, i - 1)   # Random Function

def get_comment_string(
    api_user_agent : str,
    client_id : str,
    client_secret : str,
    
    subreddits_list : list = ["AskReddit"], 
    max_posts_for_random_pool : int = 5,
    min_chars_per_post : int = 50
    
) -> str:
    
    reddit_obj = Reddit(client_id=client_id, client_secret=client_secret, user_agent=api_user_agent)    # Create reddit object

    subreddit_obj = reddit_obj.subreddit(subreddits_list[rand_index(len(subreddits_list))])    # Get subreddit object by random selection

    submission_obj = list(subreddit_obj.top(time_filter='day', limit=max_posts_for_random_pool))[rand_index(max_posts_for_random_pool)]     # Get post object by random selection

    comment_list_obj = []

    for top_comment in submission_obj.comments:
        if isinstance(top_comment, MoreComments): continue
        if len(top_comment.body) >= min_chars_per_post:
            comment_list_obj.append(top_comment.body + "..")  
     
    comment_list_obj = sorted(comment_list_obj, key=len, reverse=True)
    comment_list_obj.insert(0, submission_obj.title + "..")
        
    comment_str = ' '.join(comment_list_obj)
    comment_str = comment_str.replace('\n', '')
    comment_str = sub(r'[^\x00-\x7F]', '', comment_str)

    return comment_str

if __name__ == "__main__":
    pass
