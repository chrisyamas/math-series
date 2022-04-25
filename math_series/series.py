

def fibonacci(n):
    """Takes in a number n, returns the nth value in the Fibonacci sequence.
    Assumes starting position of zero. Achieves result through recursion."""
    n = int(abs(n))
    if n <= 0:
        fib_value = 0
    elif n == 1:
        fib_value = 1
    else:
        fib_value = fibonacci(n - 1) + fibonacci(n - 2)
    return fib_value


def fibonacci_iterate(n):
    """Takes in a number n, returns the nth value in the Fibonacci sequence.
    Assumes starting position of zero. Achieves result through iteration."""
    n = int(abs(n))
    i = 0
    fib_list = []
    while i <= n:
        if i == 0:
            fib_list.append(0)
        elif i == 1:
            fib_list.append(1)
        else:
            fib_value = fib_list[i - 1] + fib_list[i - 2]
            fib_list.append(fib_value)
        i += 1
    return fib_list[n]


def lucas(n):
    """Takes in a number n, returns the nth value in the Lucas numbers sequence.
    Assumes starting position of zero. Achieves result through recursion."""
    n = int(abs(n))
    if n <= 0:
        lucas_value = 2
    elif n == 1:
        lucas_value = 1
    else:
        lucas_value = lucas(n - 1) + lucas(n - 2)
    return lucas_value


def lucas_iterate(n):
    """Takes in a number n, returns the nth value in the Lucas numbers sequence.
    Assumes starting position of zero. Achieves result through iteration."""
    n = int(abs(n))
    i = 0
    lucas_list = []
    while i <= n:
        if i == 0:
            lucas_list.append(2)
        elif i == 1:
            lucas_list.append(1)
        else:
            lucas_value = lucas_list[i - 1] + lucas_list[i - 2]
            lucas_list.append(lucas_value)
        i += 1
    return lucas_list[n]


def sum_series(n, first=0, second=1):
    """Takes in a number n, and two optional parameters first and second.
    Optional params respectively determine first two values of a number sequence.
    Default values of optional params correspond to those of Fibonacci sequence.
    Returns the nth value of sequence specified by two optional params.
    Assumes starting position of zero. Achieves result through recursion."""
    n = int(abs(n))
    if n <= 0:
        series_value = first
    elif n == 1:
        series_value = second
    else:
        series_value = sum_series(n - 1, first, second) + sum_series(n - 2, first, second)
    return series_value


def sum_series_iterate(n, first=0, second=1):
    """Takes in a number n, and two optional parameters first and second.
    Optional params respectively determine first two values of a number sequence.
    Default values of optional params correspond to those of Fibonacci sequence.
    Returns the nth value of sequence specified by two optional params.
    Assumes starting position of zero. Achieves result through iteration."""
    n = int(abs(n))
    i = 0
    series_list = []
    while i <= n:
        if i == 0:
            series_list.append(first)
        elif i == 1:
            series_list.append(second)
        else:
            series_value = series_list[i - 1] + series_list[i - 2]
            series_list.append(series_value)
        i += 1
    return series_list[n]

