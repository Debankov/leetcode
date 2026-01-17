class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in range(0,len(arr)):
            for j in range(0, len(arr)):
                if i == j:
                    continue
                if 2 * arr[j] == arr[i]:
                    return True
        return False 
        
