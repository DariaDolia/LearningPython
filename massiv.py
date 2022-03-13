def masiv(mas, k):
    has_k = False
    for i in mas:
        ind = mas.index(i)
        for j in mas[ind + 1:]:
            summa = i + j
            if summa == k:
                print(f'{k} = {i} + {j}')
                has_k = True
                break
    if not has_k:
        print('There is no such numbers')


masiv([-1, 2, 3, 4], 22)