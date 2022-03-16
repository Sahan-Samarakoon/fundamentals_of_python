import random
number = random.randint(0,100)
while True:
    my_no = input('Enter a number between 1 and 100:')
    if not bool(my_no.rstrip()):
        print('Please enter a value')
    else:
        changed_no = int(my_no)
    if changed_no >= 1 and changed_no <= 100:
        if changed_no > number:
                print('Try a little lower')
        elif changed_no < number:
                print('Try a little higher')
        else:
            print('You guessed it right!')
            break
    else:
        print('Enter a valid input')
