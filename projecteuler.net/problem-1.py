#Challenge #2
#find all multiples of 3 and 5 in the number 666, sum them. The resulting number is the flag.
def find_sum(maximum):
    _sum = 0
    for i in range(maximum):
        if (i % 3 == 0) or (i % 5 == 0): _sum = _sum + i
    return _sum

if __name__ == '__main__':
    maximum = 666
    flag = find_sum(maximum)
