from math_series.series import fibonacci, fibonacci_iterate
from math_series.series import lucas, lucas_iterate
from math_series.series import sum_series, sum_series_iterate

# ----- Tests for fibonacci() function -----


def test_fibonacci_zero():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected


def test_fibonacci_one():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected


def test_fibonacci_two():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected


def test_fibonacci_seven():
    actual = fibonacci(7)
    expected = 13
    assert actual == expected


def test_fibonacci_float():
    actual = fibonacci(7.99)
    expected = 13
    assert actual == expected


def test_fibonacci_negative():
    actual = fibonacci(-7)
    expected = 13
    assert actual == expected


# ----- Tests for fibonacci_iterate() function -----

def test_fibonacci_iterate_zero():
    actual = fibonacci_iterate(0)
    expected = 0
    assert actual == expected


def test_fibonacci_iterate_one():
    actual = fibonacci_iterate(1)
    expected = 1
    assert actual == expected


def test_fibonacci_iterate_two():
    actual = fibonacci_iterate(2)
    expected = 1
    assert actual == expected


def test_fibonacci_iterate_seven():
    actual = fibonacci_iterate(7)
    expected = 13
    assert actual == expected


def test_fibonacci_iterate_float():
    actual = fibonacci_iterate(7.99)
    expected = 13
    assert actual == expected


def test_fibonacci_iterate_negative():
    actual = fibonacci_iterate(-7)
    expected = 13
    assert actual == expected


# ----- Tests for lucas() function -----

def test_lucas_zero():
    actual = lucas(0)
    expected = 2
    assert actual == expected


def test_lucas_one():
    actual = lucas(1)
    expected = 1
    assert actual == expected


def test_lucas_two():
    actual = lucas(2)
    expected = 3
    assert actual == expected


def test_lucas_seven():
    actual = lucas(7)
    expected = 29
    assert actual == expected


def test_lucas_float():
    actual = lucas(7.99)
    expected = 29
    assert actual == expected


def test_lucas_negative():
    actual = lucas(-7)
    expected = 29
    assert actual == expected


# ----- Tests for lucas_iterate() function -----

def test_lucas_iterate_zero():
    actual = lucas_iterate(0)
    expected = 2
    assert actual == expected


def test_lucas_iterate_one():
    actual = lucas_iterate(1)
    expected = 1
    assert actual == expected


def test_lucas_iterate_two():
    actual = lucas_iterate(2)
    expected = 3
    assert actual == expected


def test_lucas_iterate_seven():
    actual = lucas_iterate(7)
    expected = 29
    assert actual == expected


def test_lucas_iterate_float():
    actual = lucas_iterate(7.99)
    expected = 29
    assert actual == expected


def test_lucas_iterate_negative():
    actual = lucas_iterate(-7)
    expected = 29
    assert actual == expected


# ----- Tests for sum_series() function -----

def test_sum_series_zero_fibonacci():
    actual = sum_series(0)
    expected = 0
    assert actual == expected


def test_sum_series_zero_lucas():
    actual = sum_series(0, 2, 1)
    expected = 2
    assert actual == expected


def test_sum_series_one_fibonacci():
    actual = sum_series(1)
    expected = 1
    assert actual == expected


def test_sum_series_one_lucas():
    actual = sum_series(1, 2, 1)
    expected = 1
    assert actual == expected


def test_sum_series_two_fibonacci():
    actual = sum_series(2)
    expected = 1
    assert actual == expected


def test_sum_series_two_lucas():
    actual = sum_series(2, 1, 2)
    expected = 3
    assert actual == expected


# ----- Tests for sum_series_iterate() function -----

def test_sum_series_iterate_zero_fibonacci():
    actual = sum_series_iterate(0)
    expected = 0
    assert actual == expected


def test_sum_series_iterate_zero_lucas():
    actual = sum_series_iterate(0, 2, 1)
    expected = 2
    assert actual == expected


def test_sum_series_iterate_one_fibonacci():
    actual = sum_series_iterate(1)
    expected = 1
    assert actual == expected


def test_sum_series_iterate_one_lucas():
    actual = sum_series_iterate(1, 2, 1)
    expected = 1
    assert actual == expected


def test_sum_series_iterate_two_fibonacci():
    actual = sum_series_iterate(2)
    expected = 1
    assert actual == expected


def test_sum_series_iterate_two_lucas():
    actual = sum_series_iterate(2, 1, 2)
    expected = 3
    assert actual == expected

