from functools import lru_cache

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:

        @lru_cache(None)
        def solve(exp):
            ans = []

            for i, ch in enumerate(exp):
                if ch in "+-*":
                    left = solve(exp[:i])
                    right = solve(exp[i+1:])

                    for l in left:
                        for r in right:
                            if ch == "+":
                                ans.append(l + r)
                            elif ch == "-":
                                ans.append(l - r)
                            else:
                                ans.append(l * r)

            if not ans:
                ans.append(int(exp))

            return ans

        return solve(expression)
        