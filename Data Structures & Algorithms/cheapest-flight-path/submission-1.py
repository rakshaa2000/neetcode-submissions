class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n
        prices[src] = 0

        for stop in range(k+1):
            tmpPrices = prices.copy()
            for source, dest, price in flights:
                if prices[source] == float('inf'):
                    continue
                if prices[source] + price < tmpPrices[dest]:
                    tmpPrices[dest] = prices[source] + price
            prices = tmpPrices
        return -1 if prices[dst] == float('inf') else prices[dst]