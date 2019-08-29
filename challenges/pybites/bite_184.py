"""
Bite 184. Analyze some Bite stats data
"""

from csv import DictReader
from os import path
from urllib.request import urlretrieve
from collections import Counter

DATA = path.join('/tmp', 'bite_output_log.txt')
if not path.isfile(DATA):
    urlretrieve('https://bit.ly/2HoFZBd', DATA)


class BiteStats:

    def _load_data(self, data) -> list:
        rows = []
        with open(data) as csvfile:
            reader = DictReader(csvfile)
            for row in reader:
               rows.append(row)
        return rows
                

    def __init__(self, data=DATA):
        self.rows = self._load_data(data)


    @property
    def number_bites_accessed(self) -> int:
        """Get the number of unique Bites accessed"""
        return len(set([r["bite"] for r in self.rows]))

    @property
    def number_bites_resolved(self) -> int:
        """Get the number of unique Bites resolved (completed=True)"""
        return len(set([r["bite"] for r in self.rows if r["completed"] == "True"]))

    @property
    def number_users_active(self) -> int:
        """Get the number of unique users in the data set"""
        return len(set([r["user"] for r in self.rows]))

    @property
    def number_users_solving_bites(self) -> int:
        """Get the number of unique users that resolved
           one or more Bites"""
        return len(set([r["user"] for r in self.rows if r["completed"] == "True"]))

    @property
    def top_bite_by_number_of_clicks(self) -> str:
        """Get the Bite that got accessed the most
           (= in most rows)"""
        cnt = Counter()
        for r in self.rows:
            cnt[r["bite"]] += 1
        return cnt.most_common(1)[0][0]

# without Counter
#        bites = {}
#        for r in self.rows:
#            bite = r["bite"]
#            if bite in bites.keys(): # slow
#                bites[bite] += 1
#            else:
#                bites[bite] = 1
#        srt = sorted(bites.items(), key=lambda x: x[1])
#        return srt[-1][0]
        

    @property
    def top_user_by_bites_completed(self) -> str:
        """Get the user that completed the most Bites"""
        cnt = Counter()
        for r in self.rows:
            if r["completed"] == "True":
                cnt[r["user"]] += 1
        return cnt.most_common(1)[0][0]
                
# without Counter
#        users = {}
#        for r in self.rows:
#            user = r["user"]
#            if user in users.keys() and r["completed"] == "True":
#                users[user] +=1
#            else:
#                users[user] = 1
#        srt = sorted(users.items(), key=lambda x: x[1])
#        return srt[-1][0]
        
    