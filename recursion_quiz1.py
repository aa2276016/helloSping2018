def has_sum(total, n, m):
    """
    判断total能否被 n * x + m * y组成:
    例如
    has_sum(7, 2, 3) == True, 因为  2 * 2 + 3 * 1 = 7

    不得使用for loop和while loop, 必须使用递归!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    """
    # 请作答:
    # 提示
    if total%m == 0: # condition 1_1
        return True
    elif total%n == 0: # condition 1_2
        return True
    elif total - n >= m: # condition 2
        return has_sum(total-n, n, m)
    else:
        return False
    
    # 标准答案
    if total < n and total < m:
        return False
    elif total == n or total == m:
        return True
    else:
        return has_sum(total - n, n, m) or has_sum(total - m, n, m)

    
    
if __name__ == '__main__':
    assert has_sum(1, 2, 3) == False, '太小'
    assert has_sum(2, 2, 3) == True, '2*1 + 3*0 = 2'
    assert has_sum(3, 2, 3) == True, '2*0 + 3*1 = 3'
    
    assert has_sum(10, 4, 5) == True, '4*0 + 5*2 = 10'
    assert has_sum(20, 2, 3) == True, '2*4 + 3*4 =  20'
    assert has_sum(31, 7, 9) == False, 'no way!'

    assert has_sum(21, 3, 10) == True, '21'
    assert has_sum(22, 3, 10) == True, '22' 
    assert has_sum(23, 3, 10) == True, '23'
    assert has_sum(24, 3, 10) == True, '24'
    assert has_sum(25, 3, 10) == True, '25'
    assert has_sum(26, 3, 10) == True, '26'
    assert has_sum(27, 3, 10) == True, '27'
    assert has_sum(28, 3, 10) == True, '28'
    assert has_sum(29, 3, 10) == True, '29'
    assert has_sum(30, 3, 10) == True, '30'
    print('all passed')
