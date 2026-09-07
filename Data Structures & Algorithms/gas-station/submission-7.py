class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        diff = [0]*n

        if sum(gas) < sum(cost):
            return -1

        total = 0
        index = 0

        for i in range(n):
            diff[i] = gas[i] - cost[i]
        
        for i in range(n):
            total += diff[i]
            
            if total < 0:
                total = 0
                index = i+1
        
        return index
            


