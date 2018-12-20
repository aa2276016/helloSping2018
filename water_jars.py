# Each action is described as a string of two symbols: from and to. The jars are marked as 1 and 2, the lake is marked 0. If you want to take water from the lake and fill first jar, then it's "01". To pour water from second jar into the first would be "21". Dump water out of the first jar and back into the lake would be "10". When you fill a jar from the lake, that jars volume will be full. When you pour water out a jar and into the lake, that jars volume will be empty. If you pour water from one jar to another, you can only pour as much as will fill the full volume of the receiving jar.


# The function has three arguments: The volume of first jar, the volume of second jar and the goal. All arguments are positive integers (number > 0). You should return a list with action's sequence.

# The solution must contain the minimum possible number of steps
# Input: The volume of first jar, the volume of second jar and the goal as integers.

# 新思路:
# 一个pair代表两个瓶子的水量,只要target in pair即可终止
# 灌水倒水一共只有六种动作
# 终结条件,重复出现两瓶子的水量




from copy import deepcopy

def checkio(first, second, goal):

    current = [[0, 0]]  # water in [first, second]

    methods = ['01', '02', '12', '21', '10', '20'] # '0' is the lake
    # The string '01' reprenst from lake to first jar, same applies to the other strings '

    temp_method_list = [current]
    result = []

    def pour(status, first, second):
        """
        return the level of water in first and second
        after pour from first to second
        """
        available = second - status[1]
        if available == 0:
            return status
        elif available > status[0]:
            return [0, status[0]+status[1]]
        else:
            return [status[0]-available, second]

    def process(lst, method):

        now = lst[-1][:]

        if method == '01':
            now[0] = first
        elif method == '02':
            now[1] = second
        elif method == '12':
            now = pour(now, first, second)
        elif method == '21':
            now = pour(now[::-1], second, first)[::-1]
        elif method == '10':
            now[0] = 0
        elif method == '20':
            now[1] = 0

        return now

    def move(lst):
        new_method_list = []
        for i in lst:
            for method in methods:
                new_status = process(i, method)
                if new_status not in i:
                    new_i = deepcopy(i) + [new_status]
                    new_method_list.append(new_i)
                    if goal in new_status:
                        result.append(new_i)
        return new_method_list

    while result == []:
        temp_method_list = move(temp_method_list)

    print(result)



checkio(5, 7, 6)
# ['02', '21', '10', '21', '02', '21', '10', '21', '02', '21']   # 这是要求的结果
#这是目前我的输出
# [[[0, 0], [0, 7], [5, 2], [0, 2], [2, 0], [2, 7], [5, 4], [0, 4], [4, 0], [4, 7], [5, 6]]]
