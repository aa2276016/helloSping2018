# p119 Pasical's Trianle II
# Easy

# Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.
# Note that the row index starts from 0.

# Follow up: Could you optimize your algorithm to use only O(k) extra space?

from math import factorial

class Solution:

    def getRow_old(self, rowIndex):  # 方法1, 普通
        """
        :type rowIndex: int
        :rtype: List[int]
        """

        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]

        current = 1
        result = [1, 1]

        while current < rowIndex:
            result = [1] + [result[i] + result[i-1] for i in range(1, len(result))] + [1]
            current += 1

        return result


    def getRow(self, rowIndex):  # 方法二, 利用对称性只做一半的工作
        """
        :type rowIndex: int
        :rtype: List[int]
        """

        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]

        current = 2
        result = [1, 2]

        while current < rowIndex:
            x = result[-1]
            result = [1] + [result[i] + result[i+1] for i in range(current // 2)]  # 不如只求一半,另一半用复制法节省时间 # 确实快了一倍
            if current % 2 != 0:
                result += [x*2]

            current += 1

        # 根据奇数或者偶数长度判断怎么对折复制
        if rowIndex % 2 == 0:
            return result + result[-2::-1]
        else:
            return result + result[::-1]


    # 利用杨辉三角数学性质, 第 n 行的第  k 个数字为组合数 C(k/n)
    def getRow_math(self, rowIndex):

        result = []
        for k in range(0, rowIndex+1):
            result.append(factorial(rowIndex) // factorial(k) // factorial(rowIndex-k))  # 用阶乘做组合运算

        return result


    # 就这样还是慢,阶乘算太多次了, 必须结合折半法...
    def getRow_math2(self, rowIndex):

        result = []
        for k in range(0, rowIndex // 2 + 1):
            result.append(factorial(rowIndex) // factorial(k) // factorial(rowIndex-k))

        if rowIndex % 2 == 0:
            return result + result[-2::-1]
        else:
            return result + result[::-1]



if __name__ == '__main__':
    assert Solution().getRow(2) == [1, 2, 1]
    assert Solution().getRow(3) == [1, 3, 3, 1]
    assert Solution().getRow(4) == [1, 4, 6, 4, 1]
    print('all passed')

    print(Solution().getRow_math(4))
