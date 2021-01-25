a = [6, 4, 1, 4, 6, 3, 3, 4, 4, 4, 4, 1, 6]
amount = len(a)
ready = [None] * amount


def check_one(p):
    x = a[p]
    if x is not None:
        a[p] = None
        if check_two((p + x) % amount, (p - x) % amount):
            print(f"{p:2} ({x})")
            return True
        else:
            a[p] = x
            return False
    else:
        return False


def check_two(p1, p2):
    if not (check_one(p1) or check_one(p2)):
        return a == ready
    else:
        return True


for first in range(amount):
    if check_one(first): break
