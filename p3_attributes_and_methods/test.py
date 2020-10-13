# variant 1
def f1():
    x = int(input())
    y = int(input())
    result = x + y
    print(result)


# correct variant
def f2(x, y):
    result = x + y
    return result


def solve():
    x = int(input())
    y = int(input())
    result = f2(x, y)
    print(result)


test = [
    ([1, 3], 4),
    ([2, 6], 8),
    ([-2, 2], 0),
    ([-6, 12], 6),

]


def execute_test(func, params, expected_output):
    output = func(*params)
    print(f'Input: {params}, ' +
          f' Actual: {output},' +
          f' Expected: {expected_output}, '+
          f'Correct {output == expected_output}')


[execute_test(f2, params, expected) for (params, expected) in test]

