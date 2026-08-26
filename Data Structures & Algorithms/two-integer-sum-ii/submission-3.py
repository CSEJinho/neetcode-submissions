class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic = defaultdict(int)
        for i in range(len(numbers)):
            dic[numbers[i]] = i + 1
        for i in range(len(numbers)):
            temp = target - numbers[i]
            if dic[temp]:
                return [min(i + 1, dic[temp]), max(i + 1, dic[temp])]
        return []