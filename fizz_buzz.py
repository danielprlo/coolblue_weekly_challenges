import time

n = 100


def not_using_mod():
    start_time = time.time()
    three = 3
    five = 5
    result = list(range(1, n + 1))
    while three <= n:
        result[three - 1] = 'Fizz'
        three += 3
    while five <= n:
        result[five - 1] = 'FizzBuzz' if result[five - 1] == 'Fizz' else 'Buzz'
        five += 5

    print(result)
    final_time = time.time() - start_time
    print(final_time * 1000)


not_using_mod()
