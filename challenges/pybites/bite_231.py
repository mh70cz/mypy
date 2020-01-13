# -*- coding: utf-8 -*-
"""
Bite 231. Where are the emojis? 
"""

import re
from typing import List

# https://stackoverflow.com/a/43147265
# just for exercise sake, real life use emoji lib
IS_EMOJI = re.compile(r'[^\w\s,]')


def get_emoji_indices(text: str) -> List[int]:
    """Given a text return indices of emoji characters"""
    return [x.start() for x in IS_EMOJI.finditer(text)]