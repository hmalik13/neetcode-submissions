class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # make dictionary with frequency
        # array as key and list of anagrams
        # as value
        anagrams = defaultdict(list)
        for word in strs:
            freq = [0] * 26
            for c in word:
                index = ord(c) - ord('a')
                freq[index] += 1
            # append this word to the list of 
            # anagrams with same frequency
            # the array must be converted to a tuple
            anagrams[tuple(freq)].append(word)
        return list(anagrams.values())