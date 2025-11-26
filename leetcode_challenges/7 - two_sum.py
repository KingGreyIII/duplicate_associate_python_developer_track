from typing import List
# AI learned method
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        difference ={}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in difference:
                return  [difference[diff], i]
            difference[num] = i

# my original method
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)

        for index in range(length):
            step = 1
            while index + step < length:
                if nums[index] + nums[index + step] == target:
                    return [index, index + step]
                step += 1

# AI recommended version of my solution above
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        for i in range(length):
            for j in range(i + 1, length):
                if nums[i] + nums[j] == target:
                    return [i, j]
