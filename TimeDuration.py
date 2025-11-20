N = int(input())  # number of works

for _ in range(N):
    SH, SM, EH, EM = map(int, input().split())

    start = SH * 60 + SM      # convert start time to minutes
    end = EH * 60 + EM        # convert end time to minutes

    duration = end - start    # difference in minutes

    hours = duration // 60
    minutes = duration % 60

    print(hours, minutes)
