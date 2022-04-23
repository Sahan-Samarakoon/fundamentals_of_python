import random
number = random.randint(0, 100)
while True:
    my_no = input('Enter a number between 1 and 100:')
    if not bool(my_no.rstrip()):
        print('Please enter a value')
    else:
        changed_no = int(my_no)
    if changed_no >= 1 and changed_no <= 100:
        if changed_no > number:
            print('Try lower')
        elif changed_no < number:
            print('Try higher')
        else:
            print('You guessed it right!')
            break
    else:
        print('Enter a number between 1 and 100')
# 2 functions validate input and process input
# no of chances
