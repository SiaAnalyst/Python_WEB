from multiprocessing import Pool, cpu_count


def factorize(*number):
    list_num = []

    for el in number:
        new_el = el

        while new_el != 0:
            if el % new_el == 0:
                list_num.append(new_el)
            new_el = new_el - 1

        list_num.reverse()
        print(list_num)
        list_num = []

    return


if __name__ == "__main__":
    print(f"Count CPU: {cpu_count()}")
    with Pool(cpu_count()) as p:
        p.map(factorize, [128, 255, 99999, 10651060])