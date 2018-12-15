
# 给出一串数字,必须从第一个出发,必须走到最后一个数字作为终点.
# 走法可以走一步,也可以走两步
# 若有一种走法能让所踩数字之和最大, 请问最大值是多少?

def stair(lst):
    """
    Args:
        lst: a list of integers

    Returns: a integer

    """
    def find_max(n):
        if n == -1:
            return 0  # 假设开头必须为0
        elif n == 0:
            return lst[n]
        elif 0 < n < len(lst):
            return max(find_max(n-1), find_max(n-2)) + lst[n]
        elif n == len(lst):
            return max(find_max(n - 1), find_max(n - 2)) + 0  # 假设结尾也必须是0

    return find_max(len(lst))

if __name__ == '__main__':
    assert stair([5, -3, -1, 2]) == 6, '1st test, (5-1+2=6)'
    assert stair([5, 6, -10, -7, 4]) == 8, '2nd test, (5+6-7+4=8)'
    assert stair([-11, 69, 77, -51, 23, 67, 35, 27, -25, 95]) == 393, '3rd test, (69+77+23+67+35+27+95=393)'
    assert stair([1,-1,-10,-100,-50,-5000,-100,9999]) == 9840, '4th test, (1-10-50-100+9999=9840)'
    assert stair([1, -1, -10, -100, -5000, -5, -100, 9999]) == 9894, '5th test, (1-1-100-5+9999=9894)'
    assert stair([1, -1, -10, -100, -101, -101, -10, 9999]) == 9879, '6th test, (1-10-101-10+9999)'
    assert stair([1, -1, -10, -500, -500, -500, -10, 9999]) == 9480, '6th test, (1-10-500-10+9999)'
    print('All ok')
    
