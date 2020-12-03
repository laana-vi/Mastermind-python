import random


def mastermind():
    print('                         ' + '*' * 10 + 'MASTERMIND' + '*' * 10)
    print('''Enter four digits in range of 1 to 4 and try to guess the computers digits! You have 8 attempts  
to guess it right.''')
    print('\nEnter q to quit.')
    # Mastermind game where number of guesses and numbers or letters can be changed
    solution = random.choices([1, 2, 3, 4], k=4)
    # Solution makes a list out of random four number in range from 1 to 4

    guess_number = 1
    guesses = 8

    while guesses > 0:
        attempt = []
        try:
            attempt_input = (input(f'\n\tAttempt number{str(guess_number)}: '))
            if attempt_input == 'q'.lower():
                break
            for number_attempt in attempt_input:
                attempt.append(int(number_attempt))
        except ValueError:
            print('\nInvalid input!')
            # If user enters characters that are not numbers
            continue

        if len(solution) != len(attempt):
            # If user enters more than four characters
            print('\nYou have to enter four numbers!')
            continue

        if attempt[0] not in range(1, 5) or attempt[1] not in range(1, 5) or attempt[2] \
                not in range(1, 5) or attempt[3] not in range(1, 5):
            # If characters are not in range from 1 to 4
            print('\nYour number must be in range from 1 to 4!')
            continue

        guess_number += 1
        actual_exact = 0
        # Number of right guesses in the right place
        actual_wrong = 0
        # Number of right guesses but in the wrong place

        solution_dict = {}
        # keys-characters in the solution  that are not in the attempt, values number of appearances in the solution
        for index_s, number_s in enumerate(solution):
            if number_s == attempt[index_s]:
                actual_exact += 1
            else:
                if number_s in solution_dict:
                    solution_dict[number_s] += 1
                else:
                    solution_dict[number_s] = 1

        for index_a, number_a in enumerate(attempt):
            try:
                if number_a == solution[index_a]:
                    continue
                if number_a in solution_dict.keys():
                    actual_wrong += 1
                    if solution_dict[number_a] == 1:
                        solution_dict.pop(number_a)
                    else:
                        solution_dict[number_a] -= 1
            except IndexError:
                # If user input is more than five characters it raises an IndexError
                pass
        if actual_exact == 4:
            print(
                f'\nYou got in right! The correct number is {str(solution[0])} {str(solution[1])}'
                f' {str(solution[2])} {str(solution[3])}')
            break
        elif actual_exact < 4:
            print(f'\nYou got {str(actual_exact)} number(s) in the right place and'
                  f' {str(actual_wrong)} number(s) right but in the wrong place.')
        guesses -= 1
        if guesses == 0:
            print(f'\nSorry, you lost! The number was {str(solution[0])} {str(solution[1])}'
                  f' {str(solution[2])} {str(solution[3])}')
    return '                          ' + '*' * 10 + 'END' + '*' * 10


def play_again():
    # Asks if user wants to play again
    while True:
        question = input('\nDo you want to play again? \nY/N \n-')
        if question == 'y'.lower():
            print(mastermind())
        else:
            break
    return '\nThanks for playing'


print(mastermind())
print(play_again())
