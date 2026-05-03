class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # search range is 1 to max(piles)
        l = 1
        r = max(piles)
        res = r

        # do binary search to find possible k value
        while l <= r:
            k = (l + r) // 2
            hours = 0
            # check if all bananas can be eaten in h hours
            # with rate of k bananas per hour
            for p in piles:
                hours += math.ceil(p / k)
            # if it's a valid k, compare it to 
            # the current result
            if hours <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        return res