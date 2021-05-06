def prime_list(n):
    '''
    Takes an integer and returns a list of prime numbers to the given number.
    '''
    prime_list = []

    for j in range(n + 1):
        control = False

        if j > 1:
            for i in range(2, j):
                if (j % i) == 0:
                    control = True

            if not control:
                prime_list.append(j)
            else:
                pass

    return prime_list