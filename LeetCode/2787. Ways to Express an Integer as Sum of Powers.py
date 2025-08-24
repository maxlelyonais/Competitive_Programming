def numberOfWays(self, n: int, x: int) -> int:
    memo = {}
    return self.dp(n, 1, x, memo)

def dp(self, remaining: int, current: int, power: int, memo) -> int:
    if remaining == 0:
        return 1
    if pow(current, power) > remaining:
        return 0
    
    if (remaining, current) not in memo:
        memo[(remaining, current)] = (
            self.dp(remaining - pow(current, power), current + 1, power, memo)
            + self.dp(remaining, current + 1, power, memo)
        )
    return memo[(remaining, current)]