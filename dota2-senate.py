from collections import Counter, deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        cur_round,cur_types = senate,set(senate)
        c = Counter() # this counter needs to accumulate!
        while len(cur_types) == 2:
            next_round,next_types = deque(),set()
            for e in cur_round:
                if e is 'R':
                    if c['D'] <= 0:
                        next_round.append('R')
                        next_types.add('R')
                        c['R'] += 1
                    else:
                        c['D'] -= 1
                if e is 'D':
                    if c['R'] <= 0:
                        next_round.append('D')
                        next_types.add('D')
                        c['D'] += 1
                    else:
                        c['R'] -= 1
            # update
            cur_round,cur_types = next_round,next_types

        map_dict = {'D':'Dire','R':'Radiant'}
        return map_dict[cur_types.pop()]



tests = [
    'RD', # R
    "DDRRR", # D
    'RDD', # D
    'DD', # D
    "DDDRDRRDRRDRDRRRDDRRDDDRDRDDDRRRRDDDDRDRRRRDRRRDRDRDDRDRRRRDRDRRRDRDDDRRDDDRDRDRDRRDRDDRDDRDDDDRDRRR", # R
    'RRDDD' # R
]

for test in tests:
    print(Solution().predictPartyVictory(test))