""" several ways to compute fibonacci seq """
from functools import lru_cache
from functools import partial
import math
import timeit


def simple_fibonacci(n, start=0):
    """ simple form """
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return simple_fibonacci(n - 2, start) + simple_fibonacci(n - 1, start)

def memo_fibonacci(n, start=0):
    """ with memoization """
    cache = dict()
    def compute_fib(n, start):
        """ compute """
        if n in cache.keys():
            return cache[n]
        if n == 0:
            return 0
        if n == 1:
            return 1
        else:
            f = compute_fib(n - 2, start) + compute_fib(n - 1, start)
            cache[n] = f
            return f
    return compute_fib(n, start)


def memo_decor_fibonacci(n, start=0):
    """ with decorator memoization """
    @lru_cache(maxsize=100)
    def compute_fib(n, start):
        """ compute """
        if n == 0:
            return 0
        if n == 1:
            return 1
        else:
            return compute_fib(n - 2, start) + compute_fib(n - 1, start)
    return compute_fib(n, start)

def sanitize_input(from_r, to_r, fn=simple_fibonacci):
    """ sanitize input"""
    # ToDo: doplit exceptions + dopsat unit testy
    try:
        from_r = math.floor(from_r)
        to_r = math.floor(to_r)
    except:
        return None

    if (from_r < 0) or (to_r < from_r):
        return None

    if not fn in [simple_fibonacci, memo_fibonacci, memo_decor_fibonacci]:
        return None

    return (from_r, to_r, fn)

def fib_runner(from_r, to_r, fn=simple_fibonacci):
    """ run fibonacci for a given range """
    inp = sanitize_input(from_r, to_r, fn)
    if inp is None:
        return None
    else:
        from_r, to_r, fn = inp
    fib_numbers = list()
    for i in range(from_r, to_r):
        fib = fn(i, from_r)
        fib_numbers.append(fib)
        #print("{0}: {1}".format(i, fib))
    return fib_numbers
        
fib_runner(0, 10)
# fib_runner(0, 10, memo_fibonacci)
# fib_runner(0, 10, memo_decor_fibonacci)

# print(fib_runner(5, 10))
# print(fib_runner(1, 11))
# print(fib_runner(0, 10, memo_fibonacci))
# print(fib_runner(0, 10, memo_decor_fibonacci))

# def to_time():
#     # fib_runner(0, 30)
#     #fib_runner(0, 30, memo_fibonacci)
#     fib_runner(0, 30, memo_decor_fibonacci)s
#t = timeit.Timer(to_time).timeit(number=5) 

def convergence_fibs():
    """ convergence podílu dvou po sobě jdoucích fibs """
    fibs_50 = fib_runner(0, 50, memo_fibonacci)
    for i in range(2, 50):
        x = fibs_50[i]/fibs_50[i-1]
        print(x)




def measure_time():
    """ měřená funkce se zabalí do jiné funkce bez parametrů, která se předá timeit """
    for a in [(0, 30), (0, 30, memo_fibonacci), (0, 30, memo_decor_fibonacci)]:
        def to_time():
            fib_runner(*a)
        t = timeit.Timer(to_time).timeit(number=5)
        print(t)

def measure_time2():
    """ do měřené funkce se předají argumenty pomocí partial """
    t1 = timeit.Timer(partial(fib_runner, 0, 30)).timeit(number=5)
    t2 = timeit.Timer(partial(fib_runner, 0, 30, memo_fibonacci)).timeit(number=5)
    t3 = timeit.Timer(partial(fib_runner, 0, 30, memo_decor_fibonacci)).timeit(number=5)
    print("{0}\n{1}\n{2}".format(t1, t2, t3))

# measure_time()
# measure_time2()
