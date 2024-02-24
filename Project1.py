#Натуральные числа , состоящие из чётных и нечётных чередующихся цифр . Для каждого числа минимальную и максимальную цифру вывести прописью.ВАРИАНТ-20
words = {'0': 'ноль', '1': 'один', '2': 'два', '3': 'три', '4': 'четыре', '5': 'пять', '6': 'шесть', '7': 'семь', '8': 'восемь', '9': 'девять'}

def is_alt(number):
    digits = [int(digit) for digit in str(number)]
    for i in range(1, len(digits)):
        if digits[i] % 2 == digits[i - 1] % 2:
            return False
    return True

with open("lorem.txt", 'r') as file:
    try:
        block = file.read(1024)
    except FileNotFoundError:
        print('<<END>>')
    if len(block)>0:
        lexemes = block.split()
        for lexeme in lexemes:
            if lexeme.isdigit() and is_alt(lexeme):
                min_digit = min(lexeme)
                max_digit = max(lexeme)
                print(f"Число: {lexeme}\n Минимальная цифра: {words[min_digit]}\n Максимальная цифра: {words[max_digit]}")
    else:
        print('Empty')
