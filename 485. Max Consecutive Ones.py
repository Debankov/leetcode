class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        tmp = 0
        count = 0
        for i in range(0,len(nums)):
            if nums[i] == 1:
                count += 1
                if count > tmp:
                    tmp = count
            else:
                count = 0
        return tmp