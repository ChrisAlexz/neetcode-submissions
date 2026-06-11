class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1

        for r in range(1, len(nums)):#both left and right value intialized at 1
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l += 1
        return l
            

