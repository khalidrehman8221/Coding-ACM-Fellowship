class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        def reverse(nums, start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        
        n = len(nums)
        i = n - 2

        # Find the longest non-increasing suffix
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            # Find the smallest number in the suffix that is greater than nums[i]
            j = n - 1
            
            while j > i and nums[j] <= nums[i]:
                j -= 1
            
            # Swap nums[i] and nums[j]
            nums[i], nums[j] = nums[j], nums[i]
        
        # Reverse the suffix to get the next permutation
        reverse(nums, i + 1, n - 1)

        if i < 0:
            # If the entire list was non-increasing, reverse it to get the smallest permutation
            reverse(nums, 0, n - 1)
