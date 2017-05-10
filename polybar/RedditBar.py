#! /usr/bin/env python3
import random
import praw
import time
import os
def start():

    r = praw.Reddit(client_id=clientid, client_secret = clientsecret, user_agent="007")

    subreddits = ["worldnews","hacking","netsec","howtohack","android", "startups","news","politics","space"]
    todisplay = []
    #Retuns random hot submission from subreddit
    for x in subreddits:
    
        for submission in r.subreddit(x).hot(limit=6):
            todisplay.append("/r/" + x + ": " + submission.title[:70])
    return random.choice(todisplay)
        
    
