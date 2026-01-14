#two pointers solution 56ms
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 1
        while j < len(nums):
            if nums[i] == nums[j]:
                nums.pop(j)
            else:
                i += 1
                j += 1
        return len(nums)


# another solutions with out algoritms 3ms

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        temp = set(nums)
        nums.clear()
        nums.extend(temp)
        nums.sort()
        return len(nums)
