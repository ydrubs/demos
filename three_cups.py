swaps = 'acbacbabcacb'

pos = 1
for swap in swaps:
    if swap == 'a':
        if pos == 1:
            pos = 2
        elif pos == 2:
            pos = 1
        elif pos == 3:
            pos = 3

    if swap == 'b':
        if pos == 1:
            pos = 1
        elif pos == 2:
            pos = 3
        elif pos == 3:
            pos = 2

    if swap == 'c':
        if pos == 1:
            pos = 3
        elif pos == 2:
            pos = 2
        elif pos == 3:
            pos = 1

print(pos)