class Solution:
    def romanToInt(self, s: str) -> int:
        numeric = 0
        sym_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        s_length = len(s) - 1
        last_num = 0
        while s_length >= 0:
            current_sym = s[s_length]

            # if s_length == 0:
            #     numeric += sym_dict[current_sym]
            #     return numeric

            # numeric += sym_dict[current_sym]

            if sym_dict[current_sym] >= last_num:
                numeric += sym_dict[current_sym]
            else:
                numeric -= sym_dict[current_sym]

            last_num = sym_dict[current_sym]
            s_length -= 1

            if s_length <= -1:
                return numeric

s = "MCMXCIV"
riot = Solution()
print(riot.romanToInt(s))


# AI improvement on my code
# class Solution:
#     def romanToInt(self, s: str) -> int:
#         numeric = 0
#         sym_dict = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
#
#         last_num = 0
#         index = len(s) - 1
#
#         while index >= 0:
#             current_val = sym_dict[s[index]]
#
#             if current_val >= last_num:
#                 numeric += current_val
#             else:
#                 numeric -= current_val
#
#             last_num = current_val
#             index -= 1
#
#         return numeric


# AI soltion
# class Solution:
#     def romanToInt(self, s: str) -> int:
#         values = {
#             "I": 1, "V": 5, "X": 10, "L": 50,
#             "C": 100, "D": 500, "M": 1000
#         }
#
#         total = 0
#         prev = 0
#
#         for ch in reversed(s):
#             current = values[ch]
#
#             if current >= prev:
#                 total += current
#             else:
#                 total -= current
#
#             prev = current
#
#         return total


# class Solution:
#     def romanToInt(self, s: str) -> int:
#         numeric = 0
#         sym_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
#
#         for i, j in enumerate(s):
#             if i == (len(s) - 1):
#                 numeric += sym_dict[j]
#                 return numeric
#
#             current_sym = s[i]
#             next_sym = s[i + 1]
#
#             if sym_dict[next_sym] > sym_dict[current_sym]:
#                 numeric -= sym_dict[current_sym]
#                 numeric += sym_dict[next_sym] - sym_dict[current_sym]
#             else:
#                 numeric += sym_dict[current_sym]
# my first initial attempt lol 🤣