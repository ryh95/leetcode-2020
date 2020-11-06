from collections import defaultdict
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in set(wordList): return 0
        if beginWord == endWord: return 1
        transition_dict = self.get_transition_dict(wordList)
        q,visited_words,res = [[beginWord]],set([beginWord]),1
        has_find_end = False
        while q:
            cur_frontier = q.pop(0)
            next_frontier = set()
            for e in cur_frontier:
                # visited_words.add(e)
                next_frontier.update([e_n for e_n in self.obtain_neighbors(e, wordList, transition_dict)
                              if e_n not in visited_words])
            if next_frontier: q.append(list(next_frontier))
            visited_words |= next_frontier
            res += 1
            if endWord in visited_words:
                has_find_end = True
                break

        if has_find_end: return res
        return 0

    def get_transition_dict(self,wordlist):
        transition_dict = defaultdict(list)
        for i in range(len(wordlist[0])):
            for j,w in enumerate(wordlist):
                transition_dict[str(i)+'_'+w[:i]+w[i+1:]].append(j)
        return transition_dict

    def obtain_neighbors(self,w,wordlist,transition_dict):
        neighbor_words = set()
        for i in range(len(w)):
            neighbor_words.update([wordlist[id] for id in transition_dict[str(i)+'_'+w[:i]+w[i+1:]]])
        return neighbor_words

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

# trans_dict = Solution().get_transition_dict(wordList)
# print(Solution().obtain_neighbors('hot',wordList,trans_dict))
print(Solution().ladderLength(beginWord,endWord,wordList))

# print(trans_dict)