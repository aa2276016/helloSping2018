# This is code snippet developed from ProjectEuler P015
# https://projecteuler.net/problem=15
# See details in ProjectEuler/p015_lattice_paths.py


from itertools import permutations
from math import factorial


# 核心算法,生成路径,以移动方式表达
def generate_path_move(coor_1, coor_2):
    """generate all the shortest possible paths, reprented by a string composed by 'R', 'U', 'D'

    coor_1: a tuple to represent coordination (x, y)
    coor_2: a tuple to represent coordination (x, y)

    print: number of paths in total
    return: a list of strings, each string represents a sequence of movement from start to end
    """
    
    # determine the direction:
    ordered_coor_list = [coor_1, coor_2]
    start, end = sorted(ordered_coor_list)[0], sorted(ordered_coor_list)[1]
    
    if start[0] == end[0]:
        move_h = ''  # 若x值相同,则处于同一条y轴,不必左右移动
    else:
        move_h = 'R'  # 由于start,end是排序所得,所以start一定在end的左侧,只能向右移.
    
    # determine the movement direction up or down
    if start[1] > end[1]:
        move_v = 'D'  # 从start开始必须向下移动才能到end
    elif start[1] < end[1]:
        move_v = 'U'  # 从start开始必须向上移动才能到end
    else:
        move_v = ''  # 若y值相同,则处于同一条x轴,不必上下移动
    
    move_h_num, move_v_num = (end[0] - start[0]), abs(end[1] - start[1])
    path_length = move_h_num + move_v_num
    total_paths_num = factorial(path_length) // (factorial(move_h_num) * factorial(move_v_num))  # 利用组合计算总路径数目

    combination_candidate = move_h * move_h_num + move_v * move_v_num
    
    # 通过排列来输出所有的路径移动方式
    raw = list(permutations(combination_candidate, path_length))
    # 通过set()来过滤到重复的路径移动方式,利用sorted()来维持顺序
    filtered_raw = sorted(set(raw), key=raw.index)
    
    print('Total path number:', total_paths_num)
    return filtered_raw


# 定义一个翻译函数,将移动方式翻译成坐标点序列
def move_translate(coor_1, coor_2, moves):
    """translate moves into a route list of coordinates

    coor_1: a tuple to represent coordination (x, y)
    coor_2: a tuple to represent coordination (x, y)
    moves: a tuple represents the movement, example: ('R', 'U', 'R', 'U')

    return: a list of tuples, each tuple represent a cooridnate, as start follows the direction of moves
    """
    
    # determine the direction:
    ordered_coor_list = [coor_1, coor_2]
    start, end = sorted(ordered_coor_list)[0], sorted(ordered_coor_list)[1]
    
    path = [start]
    current = start
    for move in moves:
        if move == 'R':
            current = (current[0] + 1, current[1])
        elif move == 'U':
            current = (current[0], current[1] + 1)
        elif move == 'D':
            current = (current[0], current[1] - 1)
        path.append(current)
    return path


# 一个管理函数,将前两个函数结合起来,返回全部坐标点序列形式的最短路径
def find_coor_paths(coor_1, coor_2):
    
    """search all the possible shortest paths between coor_1 and coor_2

    coor_1: a tuple to represent coordination (x, y)
    coor_2: a tuple to represent coordination (x, y)

    print: number of paths in total
    return: all the paths in a list of coordinates
    """
    if coor_1 == coor_2:
        print('The two point is overlapped')
    
    result = []
    moves = generate_path_move(coor_1, coor_2)

    for move in moves:
        path = move_translate(coor_1, coor_2, move)
        result.append(path)
    
    # for printing the paths
    for path in result:
        print(path)
    
    # return the result for further use
    return result



if __name__ == '__main__':
    find_coor_paths((1,1), (1,1))      # 如果两个坐标完全重合
    find_coor_paths((-1,1), (5,1))     # 如果坐标在一条x轴上
    find_coor_paths((-1,-1), (-1,4))   # 如果坐标在一条x轴上
    find_coor_paths((1,1), (3,3))      # 如果坐标在一个正方形的两个端点 (相当于2*的grid)
    find_coor_paths((-1,1), (1,-2))    # 如果坐标随意离散 (相当于2*3的grid)
