class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_sequence = 0
        counter = 1
        nums = sorted(set(nums))
        
        if len(nums) == 1:
            return counter
        for i, num in enumerate(nums[1:]):
            if num - nums[i] == 1:
                counter += 1
            else:
                counter = 1
            longest_sequence = max(longest_sequence, counter)

        return longest_sequence