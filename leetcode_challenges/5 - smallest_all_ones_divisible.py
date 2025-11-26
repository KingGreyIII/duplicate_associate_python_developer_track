from typing import List, Dict
class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        remainder = 0
        for i in range(k):
            remainder = ((remainder * 10) + 1 ) % k

            if remainder == 0 :
                return i + 1
        return -1

num = 6
riot = Solution()
print(riot.smallestRepunitDivByK(num))

"""Amongst all leetcode challenge i have done so far, this one humbled me since the integer limit had a constraint number couldn't buikd pass 64 integer yet so building the number n = 1, 11, 111, 1111, 1111, 1111, wasnt the issue but checking if the number was divisible by using the remainder, too AI a lot of time before it explained the concept of the remainder. If you ask me to explain, i can't but using the explanation and some hint i finally arrived at the solution after spending more than 4 - 6 hours, considering i started in the afternoon , suspended and took a break in between when it wasnt entering but the problem soliving it very thrilling. Just that for now, i can intepret the questions without AI breaking and simplifying it."""