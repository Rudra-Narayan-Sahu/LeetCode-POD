class Solution:
    def countDaysTogether(self, a: str, b: str, c: str, d: str) -> int:
        def f(s):
            """This function is used to break the MM-DD format to day in 365"""
            m, q = int(s[:2]), int(s[3:])
            return (275 * m) // 9 - 2 * ((m + 9) // 12) + q - 30# Meeus's Congruence
        return max(0, min(f(b), f(d)) - max(f(a), f(c)) + 1)
