class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        hashtable = {}
        for num in set(nums):
            hashtable[num] = nums.count(num)
        if 0 in hashtable.keys() and hashtable[0] > 1:
            return [0] * len(nums)
        
        answer = []
        for num in nums:
            hashtable[num] -= 1
            ans = 1
            for key, value in hashtable.items():
                ans = ans * key ** value
            answer.append(ans)
            hashtable[num] += 1
        return answer