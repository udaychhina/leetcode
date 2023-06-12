from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # What are we doing here?

        # Add all the elements of the second array to the first array where
        # the 0's are located. Then sort the array. Very pythonic solution.
        for index in range(m, m+n):
            nums1[index] = nums2[index-m]
        nums1.sort()
