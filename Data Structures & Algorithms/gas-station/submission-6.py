class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)

        gasChange = [0] * n

        for i in range(n):
            gasChange[i] = gas[i] - cost[i]

        possibleStart = 0
        currentTank = 0
        totalGasLeft = 0

        for i in range(n):
            currentTank += gasChange[i]
            totalGasLeft += gasChange[i]

            if currentTank < 0:
                possibleStart = i + 1
                currentTank = 0

        if totalGasLeft < 0:
            return -1

        return possibleStart
