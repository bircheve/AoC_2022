with open('input') as f:
    data = f.read().split('\n\n')
    print('Part 1:', max(sum(map(int, x.split())) for x in data))
    print('Part 2:', sum(max(map(int, x.split())) for x in data))