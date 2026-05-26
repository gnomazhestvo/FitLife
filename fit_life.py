# Константы
WATER_PER_KG = 30
ML_PER_L = 1000

# Вывод приветствия
print('Добро пожаловать в приложение FitLife!')

# Запрос данных о пользователе
# имя
user_name = input('Как вас зовут? ').title()

# возраст
while True:
    try:
        user_age = int(input('Сколько вам полных лет? '))
        if 0 <= user_age <= 120:
            break
        else:
            print('Введите возраст в диапазоне от 0 до 120 лет.')
    except ValueError:
        print('Введите количество полных лет числом, например: 15.')

# вес
while True:
    try:
        user_weight = float(input('Введите ваш вес (в кг): '))
        if 15 <= user_weight <= 300:
            break
        else:
            print('Введите вес в диапазоне от 15 до 300 кг.')
    except ValueError:
        print('Введите вес в кг, например: 80.5.')

# рост
while True:
    try:
        user_height = float(input('Введите ваш рост (в м): '))
        if 0.5 <= user_height <= 2.5:
            break
        else:
            print('Введите рост в диапазоне от 0.5 до 2.5 м.')
    except ValueError:
        print('Введите рост в м, например: 1.75.')


# Расчет ИМТ и нормы потребления воды
bmi = round((user_weight / (user_height ** 2)), 1)
water_l = (user_weight * WATER_PER_KG) / ML_PER_L


# Вывод отчета для пользователя
print('=' * 45)
print(f'Отчет для пользователя {user_name}.\n')
print(f'Ваш ИМТ (индекс массы тела): {bmi}')
print(f'Рекомендуемая норма воды: {water_l} л. в день')
print(f"\nРасчет окончен. Будьте здоровы!\n{'=' * 45}")
