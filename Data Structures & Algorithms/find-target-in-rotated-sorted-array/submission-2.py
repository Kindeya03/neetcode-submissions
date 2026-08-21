class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # l = 0
        # r = len(nums) - 1

        # while l < r:
        #     m = (l + r) // 2

        #     if nums[m] > nums[r]:
        #         l = m + 1
        #     else:
        #         r = m
        # # return min(nums[lower], nums[upper])
        # if target >= nums[0]:
        #     low = 0
        #     up = l - 1
        # else:
        #     low = l
        #     up = len(nums) - 1

        # normal binary search
        up = len(nums)-1
        low = 0
        
        while low <= up:
            ch = (up + low)//2
            if nums[ch] == target:
                return ch 
            if nums[ch] >= nums[0]: # left half is sorted
                if nums[ch] > target and target >= nums[0]:
                     up = ch-1
                else:  
                    low = ch +1
            elif nums[ch] <= nums[0]: # left half is sorted
                if nums[ch] < target and target <= nums[-1]:
                     low = ch+1
                else:  
                    up = ch -1
            # ch = (up + low)//2
        return 0 if nums[0] == target else -1

        