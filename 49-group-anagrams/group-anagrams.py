class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}
        for s in strs:
            key = tuple(sorted(s))
            if key not in hm:
                hm[key] = [s]
            else:
                hm[key].append(s)
        return list(hm.values())