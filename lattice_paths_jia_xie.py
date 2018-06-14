def count_grid_path(n):
    """return number of paths from top left to bottom right

    only allow to move right and down
    n: size of the grid
    """

    count = 0
    current = [(0,0)]  # 从原点出发

    while len(current) != 0:

        # 分裂坐标
        temp = []
        for coor in current:
            temp += [(coor[0] + 1, coor[1]), (coor[0], coor[1] + 1)]  # 得到分叉一层后的坐标

        # 这里检查坐标
        open_path, end_path = [], []
        for coor in temp:
            if coor[0] == n or coor[1] == n:  # 如果遇到x值或者y值等于n,相当于不再可能分叉
                end_path.append(coor)  # 不能分叉的坐标,为路线的终点
            else:
                open_path.append(coor) # 可以继续分叉的坐标

        current = open_path  # 可以继续分叉的坐标,进入下轮循环
        count += len(end_path) # 不能分叉的坐标的数目记入结果

        # 最终current中所有的坐标都会遇到x值=n或者y值=n,所以open_path最终为空list
        # 导致current也就为空,终结while循环

    return count


if __name__ == '__main__':
    assert count_grid_path(1) == 2, 'simple'
    assert count_grid_path(2) == 6, 'regular'
    print(count_grid_path(10))
    # >>> 184756

    # print(count_grid_path(20))
    # >>> 计算量太大.算不出来



# 第二版,把上一版中的逻辑抽象化成纯数学
def count_grid_path_math(n):
    count = 0
    start = 2**n
    while start != 0:
        level_from_corner = 1
        end = 2**level_from_corner
        start -= end
        count += end
        level_from_corner += 1
    return count


if __name__ == '__main__':
    assert count_grid_path(1) == 2, 'simple'
    assert count_grid_path(2) == 6, 'regular'
    print(count_grid_path(10))
    # >>> 184756

    # print(count_grid_path(20))
    # >>> 计算量太大.还是算不出来....
