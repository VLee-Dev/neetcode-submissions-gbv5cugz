class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len (s): return False
        dict1 = {}
        for i in s:
            dict1[i] = dict1.get(i,0)+1
        dict2 = {}
        for i in t:
            dict2[i] = dict2.get(i,0)+1
        if dict1 == dict2: return True
        return False