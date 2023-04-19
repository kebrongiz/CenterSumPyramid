def center_sum_pyramid():
    for i in range(1, 8 + 1):
        row = []
        for j in range(0, i):
            row.append(str(2 ** j))

        row_len = len(row)

        for idx, k in enumerate(row[:-1]):
            row.insert(row_len, row[idx])

        padding = " " * (
            (8 * 2) - ((i * 2)))
        print(padding, end='')
        print(" ".join(row))


center_sum_pyramid()
