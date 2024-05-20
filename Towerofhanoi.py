def toh(N, fromm, to, aux):
    if N == 1:
        print("move disk", N, "from rod", fromm, "to rod", to)
        return 1
    moves = 0
    moves += toh(N-1, fromm, aux, to)
    print("move disk", N, "from rod", fromm, "to rod", to)
    moves += 1
    moves += toh(N-1, aux, to, fromm)
    return moves

# Example usage:
N = int(input("number of disks "))
print(toh(N, 1, 3, 2))