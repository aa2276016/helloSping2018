# Liars and True Tellers

# 4 3
# 1 4 L
# 2 3 T
# 4 1 T


def truthteller(raw):
    """raw in the form of list"""
    hashtable = {}
    true_statement = 0

    for state in raw[1:]:

        cowA, cowB, Bstate = state[0], state[2], state[4]

        if cowA not in hashtable:
            hashtable[cowA] = 'T'
        elif hashtable[cowA] == 'L':
            Bstate = 'T' if state[4] == 'L' else 'F'

        if cowB not in hashtable:
            hashtable[cowB] = Bstate
        elif hashtable[cowB] != Bstate:
            break

        true_statement += 1

    return true_statement




if __name__ == '__main__':
    case1 = [
        "4 3",
        "1 4 L", # 1
        "2 3 T", # 2
        "4 1 T", # 3 出现矛盾
    ]  # Example

    # 和上个case开头几乎一样, 但是加一点点
    case2 = [
        "4 6",
        "1 4 L",  # 1
        "2 3 T",  # 2
        "3 1 T",  # 3 改成正确的
        "1 3 T",  # 4 正确
        "3 4 T",  # 5 矛盾
        "3 2 T",  # 6 正确
    ]  # 返回4, 前四条时对的

    case3 = [
        "4 6",
        "1 4 L",  # 1
        "2 3 T",  # 2
        "4 3 L",  # 3 这里还是正确的, 因为4是假话, 所以3不是L而是T,和#2一致,不矛盾
        "1 3 T",  # 4 正确
        "3 4 T",  # 5 矛盾
        "3 2 T",  # 6 正确
    ]


    assert truthteller(case1) == 2
    assert truthteller(case2) == 4
    assert truthteller(case3) == 4
    print('all passed')
