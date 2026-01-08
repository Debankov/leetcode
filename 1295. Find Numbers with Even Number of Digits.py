class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for i in nums:
            numLen = int(len(str(i)))
            if numLen % 2 == 0:
                count += 1
        return count
                

# another solution

#this solution just look pretty than first
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            if len(str(n)) % 2 == 0:
                res+= 1
        return res
