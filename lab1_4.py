# Инициализация
print('НАХОЖДЕНИЕ ВРЕМЕНИ ЗАВЕРШЕНИЯ УРОКА')
# Бесконечный цикл
while True:
    print('\nДля завершения программы введите любой не числовой символ или отрицательное число (включая 0)\n')

    lesson = input('Введите номер урока: ')

    if not lesson.isdigit(): break
    lesson = int(lesson)
    # Введено отрицательное число
    if lesson<=0 : break

# Ограничения по количеству уроков в день
    # Если урок 11 ...
    if lesson > 10:
         print('Занятия в школе закончились! Все ученики ушли домой!')
         continue

    # Урок четный ...
    if (lesson % 2) == 0:
        all_time_in_minutes = ((lesson // 2) * 110) - 15
        
    # Урок нечетный ...
    if (lesson % 2) > 0:
        all_time_in_minutes = ((lesson // 2) * 110) + 45
        
    print(f'Время: {all_time_in_minutes // 60 + 9:02d}:{all_time_in_minutes % 60:02d}')

# Завершение работы
print('\n\aПока, пока ...')