#Finding nearest fruit

class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        lastSeen = -1
        consecCount = 0
        values = []
        ans = 0
        maxAns = 0
        for value in tree:
            if value not in values:
                if len(values) < 2:
                    values.append(value)
                    consecCount = 1
                    ans += 1
                else:
                    if values[1] == lastSeen:
                        values = [values[1]]
                    else:
                        values = [values[0]]
                    values.append(value)
                    ans = consecCount+1
                    consecCount = 1
            else:
                if lastSeen == value:
                    consecCount += 1
                else:
                    consecCount = 1
                ans += 1
            lastSeen = value
            maxAns = max(maxAns, ans)
            
        return maxAns