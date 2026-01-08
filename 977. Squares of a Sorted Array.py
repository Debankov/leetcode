class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sqrNums = []
        nums = list(map(abs,nums))
        for i in sorted(nums):
            sqrNums.append(i ** 2)
        return sqrNums

# another solution

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(0,len(nums)):
            nums[i] = nums[i]**2
        return sorted(nums)
