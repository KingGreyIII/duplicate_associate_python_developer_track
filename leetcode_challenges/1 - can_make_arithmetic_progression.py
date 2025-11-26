from typing import List

# 1. Define the input list
test_arr = [2, 4, 6]


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        n = len(arr)

        if n <= 2:
            return True

        diff = arr[1] - arr[0]

        for i in range(2, n):
            if arr[i] - arr[i - 1] != diff:
                return False

        return True

# 2. Create an instance of the class
solver = Solution()

# 3. Call the method, passing the input list 'test_arr'
result = solver.canMakeArithmeticProgression(test_arr)

# 4. Print the result
print(result)  # Output: True