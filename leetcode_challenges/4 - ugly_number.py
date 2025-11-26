class Solution:
    def isUgly(self, n: int) -> bool:
        prime_num = [2, 3, 5]
        if n <= 0:
            return False
        while n > 1 :
            if n % 2 == 0:
                n /= 2
            elif n % 3 == 0:
                n /= 3
            elif n % 5 == 0:
                n /= 5
            else:
                return False
        return True
num = 121
test_1 = Solution()
print(test_1.isUgly(num))

# Alternatively 
# class Solution:
#     def isUgly(self, n: int) -> bool:
#         if n <= 0:
#             return False
#
#         for p in (2, 3, 5):
#             while n % p == 0:
#                 n //= p   # integer divide
#
#         return n == 1
