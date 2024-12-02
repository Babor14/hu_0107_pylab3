import random


with open('f.txt', 'w') as f:
    for _ in range(100):  
        number = random.randint(1, 100)  
        f.write(f"{number}\n")


with open('f.txt', 'r') as f:
    even_numbers = [line.strip() for line in f if int(line.strip()) % 2 == 0]

with open('g.txt', 'w') as g:
    for number in even_numbers:
        g.write(f"{number}\n")

print("Генерация файлов завершена. Четные числа записаны в g.txt.")
