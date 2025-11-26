from typing import List, Dict
number = [*range(1, 9)]
print(number)
# right_sum = total_sum - left_sum
def pivotnumber(pivot:List[int]) -> int:
    total_sum = sum(number)
    left_sum = 0

    for pivot in number:
        left_sum += pivot
        right_sum = total_sum - (left_sum - pivot)

        if left_sum == right_sum:
            return pivot

    return -1

riot = pivotnumber(number)
print(riot)
