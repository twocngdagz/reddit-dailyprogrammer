#! /usr/bin/env python3

# Schematic: evaluate from command line
# ./get-post.py -c [challengeNumber] -d [difficultyNumber]
# Will create a directory ./posts/challenge[challengeNumber]/[difficulty]
# Within the directory, create post.md with content from Reddit post
# From there, you can try to solve the problem within its own directory

# Hard-code these in for quick eval. Add in argparse when functional
challengeNumber = 255
difficultyNumber = 3

import praw
import re
#import argparse

user_agent = "Edridge D'Souza get-post script for /r/dailyprogrammer"
r = praw.Reddit(user_agent=user_agent)
sub = 'dailyprogrammer'

def BuildQuery(ch, diff):
    challenge = u'Challenge #' + str(ch)
    difficulty = {
        1: u'easy',
        2: u'(med OR intermediate)',
        3: u'(hard OR difficult)'    
    }[diff]
    return challenge + ' ' + difficulty   
query = BuildQuery(challengeNumber, difficultyNumber)

# Return most relevant submissions to search, then double-check titles
subsearch = [i for i in r.search(query, subreddit = sub, sort = u'relevance')]

def VerifyPost(redditobject):
    