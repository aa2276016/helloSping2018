class ClassA(object):
    def __init__(self, name):
        self.name = name


class ClassB(object):
    def __init__(self, name):
        self.name = name

    def gen_list_A(self, n):
        result = []
        for i in range(n):
            result.append(ClassA('Ye Luo'))
        return result


T = ClassB('Test')
lst = T.gen_list_A(5)
print(lst)
# >>>
# [<__main__.ClassA object at 0x00000224EDCF9198>, <__main__.ClassA object at 0x00000224EDCF92E8>, <__main__.ClassA object at 0x00000224EDCF92B0>, <__main__.ClassA object at 0x00000224EDD010F0>, <__main__.ClassA object at 0x00000224EDD01470>]
