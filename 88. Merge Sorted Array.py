class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in range(0,n):
            nums1.pop()
        nums1.extend(nums2)
        nums1.sort()
        
