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

# another solution

#this solution is faster 
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result_count = []
        count = 0
        for n in nums:
            if n != 0:
                count+= 1
            else:
                result_count.append(count)
                count = 0
        
        if nums[-1] != 0:
            result_count.append(count)
            
        return max(result_count)
