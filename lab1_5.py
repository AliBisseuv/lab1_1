# Инициализация
print('СРАВНЕНИЕ ДВУХ ЧИСЕЛ')

# Бесконечный цикл
while True:
    print('\nДля завершения программы введите любой не числовой символ \n')

# Ввод 1-го числа
    x1 = input('Введите первое число: ')
    if not x1.isdigit(): break        
    x1 = int(x1)

# Ввод 2-го числа
    x2 = input('Введите второе число: ')
    if not x2.isdigit(): break        
    x2 = int(x2)

# Сравнение чисел
    # Если число 1 больше 2 числа
    if x1 > x2:
         print('1')
         continue

    # Если  число 1 меньше 2 числа
    if x1 < x2:
         print('2')
         continue
        
    # Если число 1 равно числу 2
    if x1 == x2:
         print('0')
         continue

# Завершение работы
print('\n\aПока, пока ...')