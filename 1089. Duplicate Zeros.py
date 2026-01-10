class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        
        i = 0
        while(i<len(arr)):
            if arr[i] == 0:
                arr.insert(i,0)
                arr.pop()
                i += 2
            else:
                i += 1

# another way to solution 

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        tempArray = list()
        for i,val in enumerate(arr):
            tempArray.append(val)
            if val == 0:
                tempArray.append(0)
                arr.pop()
                if i == len(arr):
                    tempArray.pop()
        arr.clear()
        arr.extend(tempArray)
