a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(len(a)):

    selected_idx = randint(i, len(a)-1)
    a[i], a[selected_idx] = a[selected_idx], a[i]

print(a)
