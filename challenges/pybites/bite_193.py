"""
Bite 193. Most upvoted StackOverflow Python questions
"""

import requests
from bs4 import BeautifulSoup

cached_so_url = 'https://bit.ly/2IMrXdp'


def top_python_questions(url=cached_so_url):
    """Use requests to retrieve the url / html,
       parse the questions out of the html with BeautifulSoup,
       filter them by >= 1m views ("..m views").
       Return a list of (question, num_votes) tuples ordered
       by num_votes descending (see tests for expected output).
    """
    r = requests.get(cached_so_url)
    if r.status_code != 200:
        raise Exception("Problem with response - status_code != 200")
    soup = BeautifulSoup(r.text)
    q_summaries = soup.body.find_all("div", class_="question-summary")
    
    questions = []
    
    for q_summary in q_summaries:
        text = q_summary.find(class_ = "question-hyperlink").text
        vote_count = q_summary.find(class_ = "vote-count-post").text
        views_raw = q_summary.find(class_ = "views").text.strip()
        if "m" in views_raw:
            questions.append((text, int(vote_count)))
    questions.sort(key=lambda x:x[1], reverse=True)
    
    return questions
            