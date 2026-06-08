class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pt1 = 0
        pt2 = len(nums) -1
        nums2 = sorted([(nums[i],i) for i in range(len(nums))])
        while pt1 < pt2 :
            if nums2[pt1][0] + nums2[pt2][0] == target :
                return sorted([nums2[pt1][1] , nums2[pt2][1] ])
            elif nums2[pt1][0] + nums2[pt2][0] < target :
                pt1 += 1
            else :
                pt2 -=1
        