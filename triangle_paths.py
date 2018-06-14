# This is code snippet developed from ProjectEuler P015
# https://projecteuler.net/problem=18
# See details in ProjectEuler/p015_lattice_paths.py

# A typical triangluler grid
#    1
#   1 2
#  1 2 3
# 1 2 3 4

# in the data structure:
# grid = [
#     [1],
#     [1,2]
#     [1,2,3]
#     [1,2,3,4]
# ]


# Brutal force
def coor_value(coor, grid):
    """coor is coordinate of the grid in the form of (x, y)

    grid: a nested list with list of numbers
    """
    return grid[coor[0]][coor[1]]

def find_triangle_paths(T):
    """calculate the max sum of a route in triangle

    T as triangle: a nested list as triangle grid
    return: the max sum of the numbers in one route of the triangle grid
    """
    row, depth = 1, len(T)
    current = [(0,0)]
    possible_path = [current]

    while row < depth:
        # 对上一行进行分裂
        possible_routes_temp = []
        for i in possible_path:
            possible_routes_temp += [i[:], i[:]]
        possible_path = possible_routes_temp[:]

        # 准备下一行的新数据,以便添加
        temp = []
        for coor in current:
            temp += [(coor[0] + 1, coor[1]), (coor[0] + 1, coor[1] + 1)]
        current = temp[:]

        # 按位置对应添加
        for idx in range(len(temp)):
            possible_path[idx].append(temp[idx])

        row += 1

    # 对坐标进行翻译,变成数值
    path_in_value = []
    for i in possible_path:
        values = [coor_value(j, T) for j in i]
        path_in_value.append(values)
    
    # 打印数值路径和路径总数
    for i in path_in_value:
        print(i)
    print('total path number', len(path_in_value))
    
    # 对每条路径求和然后找出最大值
    return sum(max(path_in_value, key=sum))




if __name__ == '__main__':
    grid_1 = [
    [1],
    [1,2],
    [1,2,3],
    [1,2,3,4]
    ]

    print(find_triangle_paths(grid_1))
    # >>> 20 (from 1,2,3,4)

