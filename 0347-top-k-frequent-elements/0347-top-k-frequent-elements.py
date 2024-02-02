class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashtable = {}
        for num in set(nums):
            hashtable[num] = nums.count(num)
            
        return list(dict(sorted(hashtable.items(), key=lambda item: item[1], reverse=True)).keys())[:k]