class Solution(object):
    def findDisappearedNumbers(self, nums):
        n = len(nums)

        # Mark the numbers that have appeared
        for num in nums:
            index = abs(num) - 1
            if nums[index] > 0:
                nums[index] = -nums[index]

        # Find the numbers that have not appeared
        disappeared_numbers = []
        for i in range(n):
            if nums[i] > 0:
                disappeared_numbers.append(i + 1)

        return disappeared_numbers
