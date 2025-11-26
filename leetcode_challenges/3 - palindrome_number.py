from typing import List, Dict
number_1 = -111
number_2 = -121
number_3 = 10

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            left_side = x * -1
            right_side = int(str(left_side)[::-1]) * -1
        else:
            left_side = x
            right_side = int(str(x)[::-1])
        if left_side == right_side:
            return True
        else:
            return False

result_1 = Solution()
result_1.isPalindrome(number_1)
print(result_1.isPalindrome(number_1))

# x = 1234
# temp = x
# reversed_num = 0
#
# while temp > 0:
#     digit = temp % 10             # get last digit
#     reversed_num = reversed_num * 10 + digit
#     temp //= 10                   # remove last digit
#
# print(reversed_num)