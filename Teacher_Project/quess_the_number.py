import random
import time


play_again = 'y'

while play_again == 'y':
    computer_number = random.randint(1, 100)  # рандомне число від 1 до 100 (включно)
    attempts = 0  # кількість спроб (з якої спроби вгадав число)
    start_time = time.time()  # фіксуємо поточний час

    while True:
        user_number = int(input('Я загадав число від 1 до 100, вгадай його: '))
        attempts += 1

        if computer_number > user_number:
            print('Моє число більше!')
        elif computer_number < user_number:
            print('Моє число менше!')
        else:
            end_time = time.time()  # фіксуємо час закінчення
            result_time = round(end_time - start_time, 2)  # заміряємо, скільки секунд між двома часовими мітками

            print(f'Вгадав! Моє число: {computer_number}!')
            print(f'Ти вгадав за {attempts} спроб!')
            print(f'Час проходження: {result_time} секунд!')
            break

    play_again = input('y - зіграти ще: ')
