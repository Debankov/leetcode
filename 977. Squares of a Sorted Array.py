class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sqrNums = []
        nums = list(map(abs,nums))
        for i in sorted(nums):
            sqrNums.append(i ** 2)
        return sqrNums
        