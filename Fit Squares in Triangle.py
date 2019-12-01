'''

What is the maximum number of squares of size 2x2 that can be fit in a right angled isosceles triangle of base B.
One side of the square must be parallel to the base of the isosceles triangle.
Base is the shortest side of the triangle

'''

test_cases = int(input())

for i in range(test_cases):
    base = int(input())

    if base == 1 or base == 2 or base == 3:
        print('0')

    else:
        base = base // 2
        p = ((base ** 2 - base) // 2)

        print(p)
