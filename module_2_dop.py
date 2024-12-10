def get_password(left_number):
    result = ""
    for i in range(1, left_number):
        for j in range(i + 1, left_number):
            if left_number % (i + j) == 0:
                result += str(i) + str(j)
    return result

print('Введите число от 3 до 20: ')

print(get_password(int(input())))