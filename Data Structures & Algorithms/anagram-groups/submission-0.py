class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # declare dictionary of lists
        anagrams = defaultdict(list)
        for s in strs:
            # initialize array of 0's for each string
            count = [0] * 26
            for c in s:
                # populate array with frequency of each 
                # character
                count[ord(c) - ord("a")] += 1
            # convert each array to tuple
            key = tuple(count)
            # append the string to the list of anagrams
            # within the value in the dict
            anagrams[key].append(s)
        return list(anagrams.values())

                