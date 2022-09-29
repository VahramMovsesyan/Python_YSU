def func(*args):
    mixed_arr = args

    prime_num = []
    perfect_num = []

    for i in mixed_arr:
        if i > 1:
            prime = True
            for j in range(2, i + 1 // 2):
                if i % j == 0:
                    prime = False
                    break
            if prime:
                prime_num.append(i)

        sum_v = 0
        for tiv in range(1, i):
            if i % tiv == 0:
                sum_v = sum_v + tiv
        if sum_v == i:
            perfect_num.append(i)

    print(
        f"""started arr: {mixed_arr}
prime number arr: {prime_num}
perfect number arr: {perfect_num}""")


func(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30)
