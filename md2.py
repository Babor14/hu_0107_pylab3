def countletters_and_digits(file_path):
    letters_count = 0
    digits_count = 0

    letters_range = (ord('а'), ord('я')) + (ord('А'), ord('Я'))
    digits_range = (ord('0'), ord('9'))

    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

        for char in text:
            if (letters_range[0] <= ord(char) <= letters_range[1]) or \
               (letters_range[2] <= ord(char) <= letters_range[3]):
                letters_count += 1
            elif digits_range[0] <= ord(char) <= digits_range[1]:
                digits_count += 1

    return letters_count, digits_count

file_path = 'your_file.txt'
russian_letters, digits = countletters_and_digits(file_path)

if russian_letters > digits:
    print("В файле больше русских букв.")
elif digits > russian_letters:
    print("В файле больше цифр.")
else:
    print("В файле одинаковое количество русских букв и цифр.")