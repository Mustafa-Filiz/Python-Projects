def fibonacci(x):
    '''
    Takes an integer and return the exact amount of Fibonacci sequence.
    '''
    fibo = [0, 1]
    count = 0
    while count < (x - 2):
        n = fibo[count] + fibo[count + 1]
        fibo.append(n)
        count += 1
    return fibo
