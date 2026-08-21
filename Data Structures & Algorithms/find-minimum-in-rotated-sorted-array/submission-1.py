class Solution:
    def findMin(self, nums: List[int]) -> int:
        tar = nums[0]
        lower = 0
        upper = len(nums)-1
        while upper - lower > 1:
            mid = (lower + upper)//2
            if nums[mid] > tar and nums[mid] > nums[upper]:
                lower = mid
            elif nums[mid] < tar and nums[mid] < nums[upper]:
                upper = mid
            else:
                return tar
        return min(nums[lower], nums[upper])

        