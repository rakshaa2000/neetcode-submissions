class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        totalGas = sum(gas)
        totalCost = sum(cost)
        if totalCost > totalGas:
            return -1
        currentGas = 0
        newStart = 0
        for i in range(0, len(gas)-1):
            currentGas += gas[i] - cost[i]
            if currentGas < 0:
                newStart = i+1
                currentGas = 0
        return newStart