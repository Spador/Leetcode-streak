##spador
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        mid = total // 2

        if len(nums2) < len(nums1):
            A, B = B, A
        
        left, right = 0, len(A) - 1

        while True:
            i = (left + right) // 2  # partition for A
            j = mid - i - 2          # partition for B

            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i+1] if (i+1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j+1] if (j+1) < len(B) else float("infinity")

            # case 1: partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                # Total elements are odd
                if total % 2 == 1:
                    return min(Aright,Bright)
                # Total element is even
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            
            # case 2: partition is incorrect because Aleft > Bright
            elif Aleft > Bright:
                right = i - 1
            
            # case 3: partition is incorrect because Bleft > Aright
            else:
                left = i + 1
