class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # iterate over nums and map each unique int to its count
        # while i < k, add max value in hashmap to result
        count = {}
        result = []
        for n in nums:
            count[n] = count.get(n, 0) + 1
        for i in range(k):
            maxVal = max(count, key=count.get)
            result.append(maxVal)
            del count[maxVal]
        return result