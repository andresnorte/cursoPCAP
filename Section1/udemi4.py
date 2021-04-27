
def any_duplicates(square):
    s1 = set(square[0])
    s2 = set(square[1])
    s3 = set(square[2])
    s4 = s1.union(s2, s3)
    if len(s4) == 9:
        return False
    else:
        return True

print(any_duplicates([[1, 3, 2], [9, 7, 8], [4, 5, 6]]))