class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        arrival_cost = [0,0]
        cost.append(0)
        for i in range(2,len(cost)) :
            arrival_cost.append(min(arrival_cost[i-1]+cost[i-1], arrival_cost[i-2]+cost[i-2]))
        print(arrival_cost)
        return arrival_cost[-1]