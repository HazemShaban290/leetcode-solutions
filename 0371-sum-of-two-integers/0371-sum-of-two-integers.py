class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff      # 32 bits
        max_int = 0x7fffffff   # max signed int

        while b != 0:
            carry = (a & b) & mask
            a = (a ^ b) & mask
            b = (carry << 1) & mask

        # convert to signed
        return a if a <= max_int else ~(a ^ mask)
