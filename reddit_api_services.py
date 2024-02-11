from praw import Reddit
from praw.models import MoreComments
from random import randint

def get_comment_string(
    api_user_agent : str,
    client_id : str,
    client_secret : str,
    
    subreddits_list : list = ["AskReddit"], 
    max_chars_of_response_string : int = 4095,
    max_comments_in_string : int = 25,
    min_chars_per_comment : int = 100,
    max_posts_for_random_pool : int = 3
    
) -> list[str] | str:
    
    reddit_obj = Reddit(client_id=client_id, client_secret=client_secret, user_agent=api_user_agent)

    subreddit_obj = reddit_obj.subreddit(subreddits_list[randint(0, len(subreddits_list) - 1)])

    submission_obj = list(subreddit_obj.top(time_filter='day', limit=max_posts_for_random_pool))[randint(0, max_posts_for_random_pool - 1)]

    comment_list_obj = []

    for top_comment in submission_obj.comments:
        if isinstance(top_comment, MoreComments): continue
        comment_list_obj.append(top_comment)
        
    comment_list_obj = comment_list_obj[:max_comments_in_string]
        
    comment_list_obj = [comment.body for comment in comment_list_obj]

    comment_list_obj = [comment for comment in comment_list_obj if len(comment) > min_chars_per_comment]
    
    comment_list_obj = [f"{comment}.." for comment in comment_list_obj]

    comment_list_obj = sorted(comment_list_obj, key=len, reverse=True)

    comment_str_obj = ' '.join(comment_list_obj)

    comment_str_obj = comment_str_obj.replace('\n',' ')

    if len(comment_str_obj) >= max_chars_of_response_string:
        comment_str_obj = [comment_str_obj[i:i+max_chars_of_response_string] for i in range(0, len(comment_str_obj), max_chars_of_response_string)]

    comment_str_obj = f"{submission_obj.title}.. {comment_str_obj}"

    return comment_str_obj

if __name__ == "__main__":
    reddit_api_user_agent = "WINDOWS:redit_data_api_link:v1 (by /u/Easy_Consequence3087)"
    reddit_api_client_id = "_YfmYHjP37FG1V-2PWmmrQ"
    reddit_api_client_secret = "rDXqGn34mrgpWoJ98nmeHL5XQUkDXg"
    
    response = get_comment_string(reddit_api_user_agent, reddit_api_client_id, reddit_api_client_secret)
    
    print(response)

# CALCULATE TIME FOR EACH COMMENT TO SPEAK (e.g calculate how long it takes to say 1 letter, then times by letters ect)

# DOWNLOAD ENOIGH COMMENTS FOR DESIRED TIME

# ORDER IN NEAT STRING