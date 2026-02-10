class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        count = [0] * 121
        for age in ages:
            count[age] += 1

        res = 0
        for x in range(15, 121):
            if count[x] == 0:
                continue
            for y in range(int(x * 0.5 + 7) + 1, x + 1):
                if count[y] == 0:
                    continue
                res += count[x] * count[y]
                if x == y:
                    res -= count[x]  # remove self-requests

        return res