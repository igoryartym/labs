A = [
    [3, 5, 0, -1],
    [-2, 9, 1, 0],
    [2, 0, -1, 3],
    [-4, 3, 0, 6]
]
# Створюємо відсортований список списків
lis = []
for el in A[::2]:
    B = [sorted(el, reverse=True)]
    lis += B
    # Замінюємо списки на відсортовані
A[::2] = lis
for i in A:
    print(i)
