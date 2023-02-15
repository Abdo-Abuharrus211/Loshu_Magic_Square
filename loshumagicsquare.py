def loshumagic(square):
    """"
    Return True
    """
    is_loshu = True
    for position in range(0, len(square)):
        row_sum = sum(square[0])
        column_sum = 0
        # columns
        for row in square:
            row_sum = sum(row)
            column_sum += row[position]
        if column_sum != row_sum:
            is_loshu = False
        else:
            continue
        # rows
        for side in square:
            if sum(side) != row_sum:
                is_loshu = False
            else:
                continue
        # diagonals
        # for
    return is_loshu


def main():
    """
    Drives program
    """
    square_one = ([1, 7, 3, 4], [2, 6, 4, 3], [6, 1, 1, 7], [6, 4, 1, 4])
    square_two = ([1, 1, 1], [1, 1, 1], [1, 1, 1])
    square_three = ([1, 1, 1], [1, 2, 1], [1, 1, 1])
    print(loshumagic(([16, 2, 3, 13], [5, 11, 10, 8], [9, 7, 6, 12], [4, 14, 15, 1])))
    print(loshumagic(([6, 1, 8], [7, 5, 3], [2, 9, 4])))
    print(loshumagic([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))
    print(loshumagic([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]))
    print(loshumagic([[2, 2], [2, 2]]))
    print(loshumagic(square_one))
    print(loshumagic(square_two))
    print(loshumagic(square_three))


if __name__ == "__main__":
    main()
