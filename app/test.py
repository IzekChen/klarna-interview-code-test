def sum_fibo(n):
    if n == 0:
        return 0
    pre, cur = 1, 1

    for i in range(n-1):
        pre, cur = cur, cur+pre
    return pre
    
def factorial(n):
    if n < 0:
        return "the input number required a non-negative number"
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)


def ackermann(m, n):
    return 0

if __name__ == "__main__":
    print(sum_fibo(10))
    print(factorial(10))