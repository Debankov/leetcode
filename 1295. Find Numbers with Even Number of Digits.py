class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for i in nums:
            numLen = int(len(str(i)))
            if numLen % 2 == 0:
                count += 1
        return count
                
        