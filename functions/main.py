def func(*args):
    mixed_arr = args

    prime_num = []
    perfect_num = []
    other_ele = []

    for i in mixed_arr:
        if i.isdigit():
            i = int(i)
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
        else:
            other_ele.append(i)

    print(
        f"""Started arr: {mixed_arr}
Prime number arr: {prime_num}
Perfect number arr: {perfect_num}
The other elements: {other_ele}""")


func("1", "a", "b", "2", "3", "4", "5", "6")
