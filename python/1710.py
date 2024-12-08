from typing import List

# * https://leetcode.com/problems/maximum-units-on-a-truck/


def maximum_units(boxTypes: List[List[int]], truckSize: int) -> int:
    cur_box = 0
    max_units = 0
    boxTypes.sort(key=lambda x: x[1], reverse=True)
        
    for box in boxTypes:
        for _ in range(box[0]):
            if cur_box >= truckSize:
                break
            cur_box += 1
            max_units += box[1]

    return max_units


# ? boxTypes[i] = [numberOfBoxes[i], numberOfUnitsPerBox[i]]
print(maximum_units(boxTypes=[[1, 3], [2, 2], [3, 1]], truckSize=4))
print(maximum_units(boxTypes=[[5, 10], [2, 5], [4, 7], [3, 9]], truckSize=10))
