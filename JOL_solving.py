def intprint(n:list):
    MAX, MIN = max(n), min(n)
    arr = list(n)
    arr.remove(MAX)
    arr.remove(MIN)
    AVG = arr[0]

    if (MAX - int(MAX)) != 0:
        MAX = int(MAX) + 1
    else:
        MAX = int(MAX)

    MIN = int(MIN)
    AVG = f"{AVG:.0f}"

    return MAX, MIN, AVG

n = list(map(float, input().split()))
MAX, MIN, AVG = intprint(n)
print(MAX, MIN, AVG)

