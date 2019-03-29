def pyg(n):
    if n == 0:
        return 0
    else:
        return n + pyg(n-1)
