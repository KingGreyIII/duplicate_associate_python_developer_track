from typing import List
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        acc_range = [int(j) for j in range(left, right + 1) if '0' not in str(j)]
        acceptable = list()
        for i in acc_range:
            series = 0
            for j in str(i):

                if i % int(j) != 0:

                    break
                else:
                    series += 1

                if series == (len(str(i))):
                    acceptable.append(i)

        return acceptable

riot = Solution()
print(riot.selfDividingNumbers( 47, 85))


# AI improved version of my code
# class Solution:
#     def selfDividingNumbers(self, left: int, right: int) -> List[int]:
#         acceptable = []
#
#         for num in range(left, right + 1):
#             s = str(num)
#
#             # Skip numbers containing zero early
#             if "0" in s:
#                 continue
#
#             # Check self-dividing property
#             valid = True
#             for digit in s:
#                 if num % int(digit) != 0:
#                     valid = False
#                     break
#
#             if valid:
#                 acceptable.append(num)
#
#         return acceptable

# ai own solution
# class Solution:
#     def selfDividingNumbers(self, left: int, right: int) -> List[int]:
#         return [
#             num
#             for num in range(left, right + 1)
#             if "0" not in str(num)
#             and all(num % int(digit) == 0 for digit in str(num))
#         ]