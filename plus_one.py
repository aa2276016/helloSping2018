
# 用list来表示一个数字, 比如123就是[1,2,3]
# 写一个函数把这个数字 +1, 答案也用列表来表示

def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    pass
    # your code:


if __name__ == '__main__':
    assert plusOne([0]) == [1]
    assert plusOne([1, 2, 3]) == [1, 2, 4]
    assert plusOne([4, 3, 2, 1]) == [4, 3, 2, 2]
    assert plusOne([1, 9, 9]) == [2, 0, 0]
    assert plusOne([9, 9, 9]) == [1, 0, 0, 0]
    print('all passed')
