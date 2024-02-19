from praw import Reddit
from re import sub
from praw.models import MoreComments
from random import randint

rand_index = lambda i: randint(0, i - 1)

def get_comment_string(
    api_user_agent : str,
    client_id : str,
    client_secret : str,
    
    subreddits_list : list = ["AskReddit"], 
    max_posts_for_random_pool : int = 5,
    min_chars_per_post : int = 50
    
) -> str:
    
    reddit_obj = Reddit(client_id=client_id, client_secret=client_secret, user_agent=api_user_agent)

    subreddit_obj = reddit_obj.subreddit(subreddits_list[rand_index(len(subreddits_list))])

    submission_obj = list(subreddit_obj.top(time_filter='day', limit=max_posts_for_random_pool))[rand_index(max_posts_for_random_pool)]

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
    reddit_api_user_agent = "WINDOWS:redit_data_api_link:v1 (by /u/Easy_Consequence3087)"
    reddit_api_client_id = "_YfmYHjP37FG1V-2PWmmrQ"
    reddit_api_client_secret = "rDXqGn34mrgpWoJ98nmeHL5XQUkDXg"
    
    response = get_comment_string(reddit_api_user_agent, reddit_api_client_id, reddit_api_client_secret)
    
    print(response)

# CALCULATE TIME FOR EACH COMMENT TO SPEAK (e.g calculate how long it takes to say 1 letter, then times by letters ect)

# DOWNLOAD ENOIGH COMMENTS FOR DESIRED TIME

# ORDER IN NEAT STRING
