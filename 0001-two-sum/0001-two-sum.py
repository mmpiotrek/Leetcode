class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for num in nums:
            diff = target - num
            if diff == num and nums.count(diff) > 1:
                start_index = nums.index(num) + 1
                return nums.index(num), nums.index(diff, start_index)
            elif diff in nums and nums.index(num) != nums.index(diff):
                return nums.index(num), nums.index(diff)