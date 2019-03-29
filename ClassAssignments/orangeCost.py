def cost(n):
    if n > 100:
        return ((n*32)/100) + 6
    else:
        return ((n*32)/100) + 7.5


def pay(r,h):
    if h <= 40: return h*r
    return r*1.5 *(h - 40) + (r * 40)
print(pay(100, 50))
