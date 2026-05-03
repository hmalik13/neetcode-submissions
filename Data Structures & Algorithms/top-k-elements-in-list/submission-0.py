from heapq import nlargest
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        # key = frequency, value = list of values 
        # with that frequency
        freq = [[] for i in range(len(nums) + 1)]

        # get count of each value
        for n in nums:
            if n not in count:
                count[n] = 1
            else:
                count[n] += 1

        # add num to list of values that have that frequency
        for num, count in count.items():
            freq[count].append(num)
        
        result = []
        # iterate over freq in descending order to get
        # top k elements
        for i in range(len(freq)-1, 0, -1):
            # iterate over each sublist
            # and add that value to result
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result
