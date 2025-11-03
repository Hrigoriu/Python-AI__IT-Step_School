input_filename = "D:\\IT school\\Projects\\Git_learning\\Git_word\\PythonAI51PublicHForc\\input.txt"
longest_word = ''

try:
    with open(input_filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            current_word = line.strip()
            if len(current_word) > len(longest_word):
                longest_word = current_word
    print(longest_word)

except FileNotFoundError:
    print(f'Помилка: Файл "{input_filename}" не знайдено.')