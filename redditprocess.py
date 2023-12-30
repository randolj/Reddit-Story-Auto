import praw

reddit = praw.Reddit(
    client_id="8Pb1OxdqelIkiHQVakLldg",
    client_secret="KfEzfdteMdclCiTqNfzLcyHa5FgAvQ",
    user_agent="Stories Creator by r/randolj",
)

subreddit = reddit.subreddit("redditstories")

test_post = reddit.submission(id="cq7li")

def getBody():
    test_post = reddit.submission(id="cq7li")

    temp = test_post.selftext
    return temp

#Section was used for testing
# top_posts = subreddit.top(limit=3)
# new_posts = subreddit.new(limit=10)
# for post in top_posts:
#     print("Title: ", post.title)

#     print("ID: ", post.id)
#     print("Author: ", post.author)
#     print("Title: ", post.title)

#     print("Score: ", post.score)
#     print("Comment count: ", post.num_comments)
#     print("Created: ", post.created_utc) 

#     print("Body: ", post.selftext)
#     print("\n")
