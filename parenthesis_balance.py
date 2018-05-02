# 请试写一个函数p_balance(str),检测字符串算式的内括号是否平衡
# 一共有三种括号形式: (), [], {}, 不分优先级,只管包容逻辑!

# 例:
# p_balance('([{}])') == True
# p_balance('([()}') == False
# 注意,算式本身不必合理,只需理会括号之间的逻辑是否合理


def p_balance(tem_str):
    open_bracket = '([{'
    close_bracket = ')]}'
    tem_list = []
    
    for each in tem_str:
        if each in open_bracket:
            tem_list.append(open_bracket.index(each))
        if each in close_bracket:
            if len(tem_list) == 0:
                return False
            if tem_list.pop() != close_bracket.index(each):
                return False
    if len(tem_list) == 0:
        return True

    return False

# Test case:
if __name__ == '__main__':
    assert p_balance('([{}])') == True, "example 1"
    assert p_balance('([()}') == False, "example 2"
    assert p_balance('((5+3)*2+1)') == True, "Simple"
    assert p_balance('{[(3+1)+2]+}') == True, "Different types"
    assert p_balance('(3+{1-1)}') == False, ") is alone inside {}"
    assert p_balance('[1+1]+(2*2)-{3/3}') == True, "Different operators"
    assert p_balance('(({[(((1)-2)+3)-3]/3}-3)') == False, "the first '(' is redundant"
    assert p_balance('2+3') == True, "No brackets, no problem"
    print('all passed')
