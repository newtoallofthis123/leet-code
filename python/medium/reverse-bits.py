class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        n = bin(n)[2:]
        n = "0" * (32 - len(n)) + n
        print(n)
        n = n[::-1]
        return int(n, 2)


s = Solution()
print(s.reverseBits(43261596))
