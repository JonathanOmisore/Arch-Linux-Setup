#! /usr/bin/env python3
import random
import praw
import time
import os
file = open("link","w")
def start():
    r = praw.Reddit(client_id=clientid,client_secret = clientsecret, user_agent="007")
   
    subreddits = ["worldnews","hacking","netsec","howtohack","bitcoin", "ethereum", "startups","news","politics","space"]
    todisplay = []
    for x in subreddits:
    
        for submission in r.subreddit(x).hot(limit=6):
            todisplay.append(submission)
    randsubmission = random.choice(todisplay)
    write(randsubmission.shortlink)
    return "/r/" + str(randsubmission.subreddit) + ": " + randsubmission.title[:70]
def write(link):
    file.write(link)
    file.close()
