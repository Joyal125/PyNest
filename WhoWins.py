N = int(input())

stones = N
i = 1   # Ramesh starts putting 1 stone

while stones > 0:
    # Ramesh's turn
    r_put = i
    stones -= r_put
    if stones <= 0:
        print("Ramesh")
        break

    # Suresh's turn
    s_put = 2 * i
    if s_put > stones:
        s_put = stones

    stones -= s_put
    if stones <= 0:
        print("Suresh")
        break

    i += 1
