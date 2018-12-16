"""
 Bite 94. Parse PyCon talk data from YouTube 


https://codechalleng.es/bites/094
"""

from collections import namedtuple
import os
import pickle
import urllib.request

# prework
# download pickle file and store it in a tmp file
pkl_file = 'pycon_videos.pkl'
data = 'http://projects.bobbelderbos.com/pcc/{}'.format(pkl_file)
pycon_videos = os.path.join('/tmp', pkl_file)
urllib.request.urlretrieve(data, pycon_videos)

# the pkl contains a list of Video namedtuples
Video = namedtuple('Video', 'id title duration metrics')


def load_pycon_data(pycon_videos=pycon_videos):
    """Load the pickle file (pycon_videos) and return the data structure
       it holds"""
    with open(pycon_videos, "rb") as f:
        p = pickle.load(f)
    return p


def get_most_popular_talks_by_views(videos):
    """Return the pycon video list sorted by viewCount"""
    return sorted(videos , key= lambda x: int(x.metrics["viewCount"]), reverse = True)

def _like_to_view(video):
    return (int(video.metrics["likeCount"]) - int(video.metrics["dislikeCount"])) / int(video.metrics["viewCount"])

def get_most_popular_talks_by_like_ratio(videos):
    """Return the pycon video list sorted by most likes relative to
       number of views, so 10 likes on 175 views ranks higher than
       12 likes on 300 views. Discount the dislikeCount from the likeCount.
       Return the filtered list"""
    return sorted(videos, key=_like_to_view, reverse = True)


def get_talks_gt_one_hour(videos):
    """Filter the videos list down to videos of > 1 hour"""
    return [ v for v in videos if "H" in v.duration ]

def _get_mins(video):
    duration = video.duration
    m_pos = duration.index("M")
    minutes_str = duration[m_pos-2:m_pos]
    if minutes_str[0].isnumeric():
        minutes = int(minutes_str)
    else:
        minutes = int(minutes_str[-1])
    return minutes
    
    
def get_talks_lt_twentyfour_min(videos):
    """Filter videos list down to videos that have a duration of less than
       24 minutes"""
    return [ v for v in videos if _get_mins(v) < 24 and "H" not in v.duration ]
