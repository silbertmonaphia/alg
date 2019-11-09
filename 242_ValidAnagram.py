class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

    def isAnagram1(self, s: str, t: str) -> bool:
        dict1, dict2 = dict(), dict()
        for item in s:
            dict1[item] = dict1.get(item, 0) + 1
        for item in t:
            dict2[item] = dict2.get(item, 0) + 1
        return dict1 == dict2

    def isAnagram2(self, s: str, t: str) -> bool:
        dict1, dict2 = [0]*26, [0]*26
        for item in s:
            dict1[ord[item]-ord('a')] += 1
        for item in t:
            dict2[ord[item]-ord('a')] += 1
        return dict1 == dict2