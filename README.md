# LAB - Class 02

## Project: Modules and Testing

### Author: Christopher Yamas

#### Tests (section to be filled out tomorrow with answers to the following questions)

For each function, there are several tests.

For the `fibonacci()` function which takes in a number n and uses recursion to return the nth value of the Fibonacci sequence (with presumed n starting point of zero), there are tests for:

- n value of 0
- n value of 1
- n value of 2
- n value of 7
- n value of 7.99 (to test float)
- n value of -7 (to test negative)

For the `fibonacci_iterate()` function which takes in a number n and uses iteration to return the nth value of the Fibonacci sequence (with presumed n starting point of zero), there are tests for:

- n value of 0
- n value of 1
- n value of 2
- n value of 7
- n value of 7.99 (to test float)
- n value of -7 (to test negative)

For the `lucas()` function which takes in a number n and uses recursion to return the nth value of the Lucas numbers sequence (with presumed n starting point of zero), there are tests for:

- n value of 0
- n value of 1
- n value of 2
- n value of 7
- n value of 7.99 (to test float)
- n value of -7 (to test negative)

For the `lucas_iterate()` function which takes in a number n and uses iteration to return the nth value of the Lucas numbers sequence (with presumed n starting point of zero), there are tests for:

- n value of 0
- n value of 1
- n value of 2
- n value of 7
- n value of 7.99 (to test float)
- n value of -7 (to test negative)

For the `sum_series()` function which takes in a number `n` (required parameter) and two optional parameters `first` and `second` (with default values of 0 and 1, respectively, which correspond to Fibonacci's starting points). Other values can be passed in for these optional parameters, resulting in the function returning numbers for a different specified sequence (i.e. first=2, second=1 would specify Lucas numbers sequence). The function then uses recursion to return the nth value of the specified sequence (with presumed n starting point of zero), there are tests for:

- n value of 0, first value of 0, second value of 1 (fibonacci specification)
- n value of 0, first value of 2, second value of 1 (lucas specification)
- n value of 1, first value of 0, second value of 1 (fibonacci specification)
- n value of 1, first value of 2, second value of 1 (lucas specification)
- n value of 2, first value of 0, second value of 1 (fibonacci specification)
- n value of 2, first value of 2, second value of 1 (lucas specification)


For the `sum_series_iterate()` function which takes in a number `n` (required parameter) and two optional parameters `first` and `second` (with default values of 0 and 1, respectively, which correspond to Fibonacci's starting points). Other values can be passed in for these optional parameters, resulting in the function returning numbers for a different specified sequence (i.e. first=2, second=1 would specify Lucas numbers sequence). The function then uses iteration to return the nth value of the specified sequence (with presumed n starting point of zero), there are tests for:

- n value of 0, first value of 0, second value of 1 (fibonacci specification)
- n value of 0, first value of 2, second value of 1 (lucas specification)
- n value of 1, first value of 0, second value of 1 (fibonacci specification)
- n value of 1, first value of 2, second value of 1 (lucas specification)
- n value of 2, first value of 0, second value of 1 (fibonacci specification)
- n value of 2, first value of 2, second value of 1 (lucas specification)

Did not complete tests for the sum_series() and sum_series_iterate() functions for n values higher than 2, less than zero, or of type float. I was confident that the desire results would be produced, since I was using same methods as in the earlier recursive and iterative functions.
