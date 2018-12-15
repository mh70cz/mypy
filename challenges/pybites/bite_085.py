"""
Bite 85. Write an advanced property 


https://codechalleng.es/bites/085
"""

scores = [10, 50, 100, 175, 250, 400, 600, 800, 1000]
ranks = 'white yellow orange green blue brown black paneled red'.split()
BELTS = dict(zip(scores, ranks))


class NinjaBelt:

    def __init__(self, score=0):
        self._score = score
        self._last_earned_belt = None

    def _get_belt(self, new_score):
        belt = None
        for s in scores:
            if s <= new_score:
                belt = BELTS[s]
            else:
                break
        return belt

    def _get_score(self):
        return self._score

    def _set_score(self, new_score):
        if not isinstance(new_score, int):
            raise ValueError
        if new_score < self._score :
            raise ValueError
        self._score = new_score
        rank = self._get_belt(self._score)
        if self._last_earned_belt == rank:
            print (f"Set new score to {new_score}")        
        else:
            self._last_earned_belt = rank
            print(f"Congrats, you earned {new_score} points obtaining the PyBites Ninja {rank.title()} Belt")
        
    score = property(_get_score, _set_score)
            
            
            


    