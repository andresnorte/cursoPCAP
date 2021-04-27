

def solve_hanoi_tower(discs):
    if discs == 0:
        return 0
    else:
        i = 1
        x = 1 #S(1) = 1
        while i < discs:
            k = 2*x + 1
            x = k
            i += 1
        return(x)

print((solve_hanoi_tower(4)))