class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not s and not t: return True
        if not s or not t: return False
        s_dict,t_dict = {},{}
        for i in s:
            if i in s_dict:
                s_dict[i] += 1
            else:
                s_dict[i] = 0
        for i in t:
            if i in t_dict:
                t_dict[i] += 1
            else:
                t_dict[i] = 0
        for k,v in s_dict.items():
            try:
                if t_dict[k] != v:
                    return False
            except:
                return False
        for k,v in t_dict.items():
            try:
                if s_dict[k] != v:
                    return False
            except:
                return False
        return True