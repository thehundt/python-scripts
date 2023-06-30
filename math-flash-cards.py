from colorama import Fore, Back, Style

correct_count = 0
incorrect_count = 0

while True:
    from random import randint
    a = randint(1, 12)
    b = randint(1, 12)

    product = a * b
    answer = input('%d x %d = ' % (a, b))

    if answer.lower() == 'q':
        total = correct_count + incorrect_count
        percent = round(((correct_count / total) * 100), 1)
        print('\nYou got %d correct out of %d for a score of %s percent' %
              (correct_count, total, percent))
        print('See you soon!!!\n')
        break

    if answer.isdigit() and int(answer) == product:
        correct_count += 1
        print(Fore.GREEN + 'Correct!\n')
        print(Style.RESET_ALL)
    else:
        incorrect_count += 1
        print(Fore.RED + 'Incorrect!' + Style.RESET_ALL + 
              ' %d x %d =  %d \n' % (a, b, product))
