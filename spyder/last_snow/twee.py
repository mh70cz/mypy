"""
https://apps.twitter.com
Owner	mh70cz
Owner ID	18578903
"""

import tweepy
from pathlib import Path

# Store OAuth authentication credentials in relevant variables

access_token = "18578903-jqIt6bjBzhD46p8GDkYSuE5KChvRwSOWtolWNQjHL"
access_token_secret = ""
consumer_key = "dLbcVhiqDUOi9ZYmcYqa2UcqI"
consumer_secret = ""

def get_secrets():
    home = str(Path.home())
    secrets_file = home + '/Documents/pymh70.txt'
    access_token_secret = ""
    consumer_secret = ""
    try:
        with open(secrets_file, "r", encoding="utf8") as f:
            for line in f:
                print(line)
                if line[0] == "#":
                    continue
                if "access_token_secret" in line:
                    first_qm_pos = line.find('"')
                    tmp_str = line[first_qm_pos + 1 : ]
                    second_qm_pos = tmp_str.find('"')
                    access_token_secret = tmp_str[:second_qm_pos]
                if "consumer_secret" in line:
                    first_qm_pos = line.find('"')
                    tmp_str = line[first_qm_pos + 1 : ]
                    second_qm_pos = tmp_str.find('"')
                    consumer_secret = tmp_str[:second_qm_pos]                

    except Exception as e:
            print("Poblem getting secrets")
            raise e
    return (access_token_secret,  consumer_secret)

print(get_secrets())
