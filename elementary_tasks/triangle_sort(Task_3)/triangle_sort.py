from math import sqrt

side_a = int(input('a'))
side_b = int(input('b'))
side_c = int(input('c'))


p = (side_a + side_b + side_c)/2
Square = (p*(p-side_a)*(p-side_b)*(p-side_c))**0.5

if side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a:
    print("есть")
else:
    print('no')