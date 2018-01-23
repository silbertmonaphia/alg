#! /usr/bin/env python3
# encoding:utf-8

# 费波纳茨数列和青蛙跳台阶问题


def perf_time(func):
    import functools
    import time

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        s = time.time()
        try:
            result = func(*args, **kwargs)
        except Exception:
            import traceback
            print(traceback.format_exc())
        print('perf_time: elaspsed {0:.6f}s'.format(time.time() - s))
        return result

    return wrapper


def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n - 2) + fib_recursive(n - 1)


def fib_refine(n):
    # O(n)
    fib_n_minus_two = 0
    fib_n_minus_one = 1
    if n in (0, 1):
        return n
    for i in range(2, n + 1):
        fib_n = fib_n_minus_two + fib_n_minus_one
        fib_n_minus_two = fib_n_minus_one
        fib_n_minus_one = fib_n
    return fib_n


def test_fib():
    wanted_result = 5
    result = fib_refine(5)
    print(result)
    assert(result == wanted_result), '1'


@perf_time
def test_fib_recursive_perf():
    fib_recursive(20)


@perf_time
def test_fib_refine_perf():
    fib_refine(20)


if __name__ == '__main__':
    test_fib()
    test_fib_recursive_perf()
    test_fib_refine_perf()
