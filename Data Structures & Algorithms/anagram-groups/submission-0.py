class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for w in strs:
            sorted_word = ''.join(sorted(w))
            res[sorted_word].append(w)
        return list(res.values())