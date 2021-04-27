
def calc_dice_scores(lst):
    i = 0
    for (d, b) in lst:
        if d == b:
            return 0
        else:
            i = i + (d + b)
    return i

print(calc_dice_scores([(1, 2), (4, 3), (5, 6)]))

def calc_dice_scores(lst):
    return sum([a + b for a, b in lst]) if not any([a==b for a, b in lst]) else 0


print(calc_dice_scores([(1, 2), (4, 3), (5, 6)]))
