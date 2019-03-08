
# Q1 Twin String
# 找出两个string是否为twins:
# 若是两者有且只有一组奇数或者偶数index的字符互为swap,其他都一样就是twins
def twinString(a, b):
    aL, bL = len(a), len(b)
    if aL != bL:
        return 'No'
    i = 0
    checklist = []
    while i != aL:
        if a[i] != b[i]:
            checklist.append(i)
        i += 1

    if len(checklist) != 2:
        return 'No'
    else:
        x, y = checklist[0], checklist[1]
        A1, A2, B1, B2 = a[x], a[y], b[x], b[y]
        if (A1 == B2 and A2 == B1) and \
               (x % 2 == 0 and y % 2 == 0) or \
               (x % 2 != 0 and y % 2 != 0):
            return 'Yes'
        else:
            return 'No'


if __name__ == '__main__':
    assert twinString('a', 'b') == 'No'
    assert twinString('ab', 'ba') == 'No'
    assert twinString('abc', 'cba') == 'Yes'
    assert twinString('abcd', 'cbad') == 'Yes'
    assert twinString('abcd', 'bacd') == 'No'
    print('all passed')



# Q2 Consecutive Sums
# 找出一个>=1的正整数X有几种可能性可以被拆成一个连续的正整数(至少两个数)之和

# 假设存在一个n项的等差数列A,之和刚好等于X, 根据等差数列求和公式:
# (A0+An)*n/2 = X, 也就是:
# (A0+An)*n = 2X --- 注意2X必为偶数
from math import sqrt
def consecutiveSums(X):
    if X <= 2:
        return 0

    result = 0
    doubleX= 2*X
    for n in range(2, int(sqrt(doubleX))+1):  # 范围限定,必须至少2个数,而最多只除到sqrt(2X), 因为A0AN 必须 > n
        if doubleX % n == 0:  # 也就是能整除
            A0AN = doubleX // n # 存在一个n项数列,首尾相加等于A0AN
            # 这里必须要讨论奇偶性:
            if n % 2 == 0 and A0AN % 2 != 0:     # 偶数项数列, 首尾相加必是奇数
                result += 1
            # elif n % 2 != 0 and A0AN % 2 == 0: # 奇数项数列, 首尾相加必是偶数
            #     result += 1  # (其实这条是多余的, 因为2X必为偶数, 如果n是奇数, 那么2X/n=A0AN在数学上只可能是偶数)
            # 所以可以简化为:
            elif n % 2 != 0: # n为奇数项就必可行
                result += 1
    return result

if __name__ == '__main__':
    assert consecutiveSums(1) == 0
    assert consecutiveSums(2) == 0
    assert consecutiveSums(3) == 1
    assert consecutiveSums(21) == 3, '123456, 678, 1011'
    assert consecutiveSums(15) == 3, '12345, 456, 78'
    print('all passed')





