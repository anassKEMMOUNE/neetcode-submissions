class Solution:
    def maxArea(self, heights: List[int]) -> int:
        pt1 = 0
        pt2 = len(heights)-1
        max_amount =  0
        while pt1 < pt2 :
            curr_amount = (pt2 - pt1 )* min(heights[pt2],heights[pt1])
            max_amount = max(curr_amount,max_amount)
            if heights[pt1] < heights[pt2] :
                pt1 += 1
            else :
                pt2 -= 1
        return max_amount


        