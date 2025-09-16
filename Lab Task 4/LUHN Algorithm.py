def luhn(card_no):
    rem = int(card_no[-1])
    l = list(card_no[:-1])
    n = []
    for i in l:
        n.append(int(i))
    n.reverse()

    for i in range(len(n)):
        if i % 2 == 0:
            n[i] *= 2
            if n[i] > 9:
                n[i] -= 9

    t = sum(n) + rem
    print(t)
    return t % 10 == 0


print(luhn("5893804115457289"))
print(luhn("5893804115457288"))