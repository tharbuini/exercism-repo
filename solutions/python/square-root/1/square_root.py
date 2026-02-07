def square_root(number):
    x = [1]

    # Calculating 10 times for better precision
    for i in range(10):
        heron_number = (1/2) * (x[i] + (number/x[i]))
        x.append(heron_number)

    return int(x[-1])