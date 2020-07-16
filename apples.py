"""
Author  : Vivek Shinde
Date    : 02/06/2020
purpose : Practice problem solving
code    : To take quantity of apples, minimum range, maximum range as input and print which number is divisible
          from minimum range to maximum range
"""



def apples():
    for i in range(user_input_min, user_input_max + 1):
        if user_input_apples % i == 0:
            print(f'{i} is a divisor of {user_input_apples}')
        else:
            print(f'{i} is not a divisor of {user_input_apples}')


if __name__ == '__main__':
    while True:
        user_input_apples = input('Enter how manny apples you have :')
        if user_input_apples.isalpha():
            print('Please enter integer\n')
            continue
        else:
            user_input_apples = int(user_input_apples)
            break

    while True:
        user_input_min = input('Enter minimum range :')
        if user_input_min.isalpha():
            print('Please enter integer\n')
            continue
        else:
            user_input_min = int(user_input_min)
            break

    while True:
        user_input_max = input('Enter maximum range :')
        if user_input_max.isalpha():
            print('Please enter integer\n')
            continue
        else:
            user_input_max = int(user_input_max)
            break

    if user_input_min == user_input_max:
        min_max_equals = user_input_apples % user_input_min
        print(f'\nThis is not in range, the result is {min_max_equals}')
    elif user_input_min > user_input_max:
        print('\nYou entered incorrect range i.e. maximum to minimum')
    else:
        apples()
