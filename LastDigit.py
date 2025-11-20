def last_digit(a, b):
    # Last digit cycles for base 0-9
    cycles = {
        0: [0],
        1: [1],
        2: [2, 4, 8, 6],
        3: [3, 9, 7, 1],
        4: [4, 6],
        5: [5],
        6: [6],
        7: [7, 9, 3, 1],
        8: [8, 4, 2, 6],
        9: [9, 1]
    }
    
    last = a % 10
    cycle = cycles[last]
    cycle_len = len(cycle)

    # For very large b, use modulo to find the correct index
    index = (b % cycle_len) - 1
    return cycle[index]


# Main Program
N = int(input().strip())

for _ in range(N):
    a, b = map(int, input().split())
    print(last_digit(a, b))
