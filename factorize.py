import concurrent.futures

def check_last_number(number: int):
    """A function that checks the last digit of a number"""
    last_number = number % 10
    if last_number == 0:
        return 'Zero'
    elif last_number % 2 == 0:
        return 'Even'
    else:
        return 'Odd'

def all_dividers(number: int, parity: str):
    """A function that returns all divisors of a number"""
    if parity == 'Zero':
        dividers_list = [1] + [num for num in range(2, number+1) if number % num == 0 ]
    elif parity == 'Even':
        dividers_list = [1] + [num for num in range(2, number+1, 2) if number % num == 0 ]
    else:
        dividers_list = [1] + [num for num in range(3, number+1, 2) if number % num == 0 ]
    return dividers_list 

def factorize(number: int) -> list:
    """A function that takes a list of numbers and returns a list of numbers by which the numbers in the input list are divisible without remainder."""
    result = []
    result.append(all_dividers(number, check_last_number(number)))
    return result
    raise NotImplementedError()

# Implementation of multithreading
if __name__ == '__main__':
    numbers = [128, 255, 99999, 10651060]
    result = []
    with concurrent.futures.ProcessPoolExecutor(4) as executor:
        for res in executor.map(factorize, numbers):
            result.append(*res)
    a, b, c, d = result
    
    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]