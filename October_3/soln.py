class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        ans = 0
        i = 0
        j = 1
        n = len(colors)
        while i < n and j < n:
            if colors[i] == colors[j]:
                if neededTime[i] > neededTime[j]:
                    ans += neededTime[j]
                    j += 1
                else:
                    ans += neededTime[i]
                    i = j
                    j += 1
                
            else:
                i = j
                j += 1

        return ans
