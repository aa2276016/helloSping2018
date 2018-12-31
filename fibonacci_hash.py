def fib_gen_r(i):
    """
    Fibonacci function generator
    generate the fibonacci number at 'i'th posistion
    """
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        return fib_gen_r(i - 1) + fib_gen_r(i - 2)


# Memorization method + recursion
# This will increase efficiency as the recursion method repeatedly calculate f(n-1), f(n-2)...to f(0) many times.

def fib_gen_r_mem(n):
    mem_dict = {0: 0, 1: 1}

    def helper(n):
        if n in mem_dict:
            return mem_dict[n]
        else:
            ans = helper(n - 1) + helper(n - 2)
            mem_dict[n] = ans
            return ans

    return helper(n)


import time
if __name__ == '__main__':
    start_time = time.time()
    print(fib_gen_r(35))
    print(f"--- {time.time() - start_time}s seconds ---\n")

    start_time = time.time()
    print(fib_gen_r_mem(35))
    print(f"--- {time.time() - start_time}s seconds ---\n")
    
