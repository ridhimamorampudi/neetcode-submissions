class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        diff = [0]*n

        for i in range(n):
            diff[i] = gas[i] - cost[i]
        
        start = 0
        res = 0
        total = 0

        for i in range(n):
            res += diff[i]
            total += diff[i]

            if res < 0:
                start = i + 1
                res = 0

        if total < 0:
            return -1
        return start

