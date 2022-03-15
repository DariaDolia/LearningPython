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
        print([])


masiv([-1, 2, 3, 4], 22)


def sum_of_two(mas, k):
    for i in range(len(mas)):
        summa = mas[0] + mas[-1]
        if summa > k:
            del mas[-1]
        elif summa < k:
            del mas[0]
        elif summa == k:
            print(f'Answer: {mas[0]} and {mas[-1]}')
            break
        else:
            print([])


sum_of_two([-1, 0, 1, 3, 5, 7], 1)


def sum_two_num(mas, k):
    start = 0
    end = len(mas) - 1
    while start != end:
        summa = mas[start] + mas[end]
        if summa == k:
            print(f'Answer: {mas[start]} and {mas[end]}')
            return
        elif summa > k:
            end -= 1
        else:
            start += 1
    print([])


sum_two_num([-1, 4, 7, 7, 7], 3)
