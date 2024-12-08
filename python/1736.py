
# * https://leetcode.com/problems/latest-time-by-replacing-hidden-digits/


def maximum_time(time: str) -> str:
    time_as_list = list(time)
    for i, val in enumerate(time_as_list):
        if val == '?':
            if i == 0:
                time_as_list[i] = '2' if time_as_list[1] <= '3' or time_as_list[1] == '?' else '1'
            elif i == 1:
                time_as_list[i] = '3' if time_as_list[0] == '2' else '9'
            elif i == 3:
                time_as_list[i] = '5'
            elif i == 4:
                time_as_list[i] = '9'
    return ''.join(time_as_list) 


print(maximum_time(time="2?:?0"))
print(maximum_time(time="0?:3?"))
print(maximum_time(time="1?:22"))
print(maximum_time(time="?2:4?"))
print(maximum_time(time="?5:?6"))
print(maximum_time(time="??:??"))