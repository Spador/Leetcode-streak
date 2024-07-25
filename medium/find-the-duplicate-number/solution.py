##spador
# Learn this problem rather than solving it.
# it uses slow and fast pointer. The value at each index of the array points to the next index in the array. If the value is repeated then the slow pointer will catch fast becuase of the loop.
# Then create a new slow pointer at starting index and start moving both old slow and new slow pointers. They will meet at the start of the loop which will be the repeating element.

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow1 = nums[0]
        fast = nums[0]

        while True:
            slow1 = nums[slow1]
            fast = nums[nums[fast]]
            if slow1 == fast:
                break
        
        slow2 = nums[0]
        while slow1 != slow2:
            slow1 = nums[slow1]
            slow2 = nums[slow2]
        return slow1
