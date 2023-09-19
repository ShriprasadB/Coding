class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = nums[0]
        
        # to get the meet point of tortoise and rabbit in the loop
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if fast == slow:
                break

        slow = nums[0]
        #they will meet when numbers are equal
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow           