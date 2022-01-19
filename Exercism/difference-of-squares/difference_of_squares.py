def square_of_sum(number):
    l_numbers = []
    for i_number in range(1, number + 1):
        l_numbers.append(i_number)   
    return sum(l_numbers) ** 2


def sum_of_squares(number):
    s_numbers = []
    for i_num in range(1, number + 1):
        square_i_num = i_num ** 2
        s_numbers.append(square_i_num)
    return sum(s_numbers)


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)


