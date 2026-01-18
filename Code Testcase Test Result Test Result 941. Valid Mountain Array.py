class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) <= 1:
            return False
        if arr[0] > arr[1]:
            return False
        if arr[-2] < arr[-1]:
            return False
        i = 0
        j = 1
        peakReached = False
        while j < len(arr):
            if arr[i] == arr[j]:
                return False
    
            if arr[i] > arr[j] and peakReached != True:
                peakReached = True
            elif arr[i] < arr[j] and peakReached == True:
                return False
            i +=1
            j +=1
        return True
        
