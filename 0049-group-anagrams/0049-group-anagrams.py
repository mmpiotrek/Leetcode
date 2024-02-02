class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashtable = {}
        for word in strs:
            key = ''.join(sorted(word))
            if key in hashtable:
                hashtable[key].append(word)
            else:
                hashtable[key] = [word]
        return [x for _, x in hashtable.items()]
