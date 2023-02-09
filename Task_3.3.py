def calculate_word_value(word, alphabet):
    word = word.upper()
    value = 0
    for char in word:
        if alphabet == 'english':
            if char in 'AEIOULNRST':
                value += 1
            elif char in 'DG':
                value += 2
            elif char in 'BCMP':
                value += 3
            elif char in 'FHVWY':
                value += 4
            elif char in 'K':
                value += 5
            elif char in 'JX':
                value += 8
            elif char in 'QZ':
                value += 10
        elif alphabet == 'russian':
            if char in 'АВЕИНОРСТ':
                value += 1
            elif char in 'ДКЛМПУ':
                value += 2
            elif char in 'БГЁЬЯ':
                value += 3
            elif char in 'ЙЫ':
                value += 4
            elif char in 'ЖЗХЦЧ':
                value += 5
            elif char in 'ШЭЮ':
                value += 8
            elif char in 'ФЩЪ':
                value += 10
    return value


word = input('Введите слово: ')
alphabet = input('Введите алфавит (english or russian): ')
value = calculate_word_value(word, alphabet)
print('Значение слова:', value)
