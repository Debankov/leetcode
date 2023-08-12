class Solution:
    def numberOfSteps(self, num: int) -> int:
        isNoneZero = True
        count = 0 
        while isNoneZero:
            if num % 2 == 0 and num != 0:
                num = num / 2
                count += 1

            if num % 2 != 0:
                num = num - 1
                count += 1
            
            if num == 0:
                isNoneZero = False
                return count
