class Solution:
    def search(self, nums: List[int], target: int) -> int:
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
        return -1

        