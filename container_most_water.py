from typing import List

# * https://leetcode.com/problems/container-with-most-water/
# ? Medium difficulty


def max_area(heights: List[int]) -> int:
    left_index = 0
    right_index = len(heights) - 1
    cur_max_area = 0

    while left_index < right_index:
        height = min(heights[left_index], heights[right_index])
        cur_max_area = max(cur_max_area, calc_area(height, right_index - left_index))
        while height >= heights[left_index] and left_index < right_index:
            left_index += 1
        while height >= heights[right_index] and left_index < right_index:
            right_index -= 1

    return cur_max_area


def calc_area(height, width):
    return height * width


print(max_area(heights=[1, 1]))  # 1
print(max_area(heights=[4, 3, 2, 1, 4]))  # 16
print(max_area(heights=[1, 2, 1]))  # 2
print(max_area(heights=[1, 8, 6, 2, 5, 4, 8, 3, 7]))  # 49
print(max_area(heights=[2, 3, 10, 5, 7, 8, 9]))  # 36
