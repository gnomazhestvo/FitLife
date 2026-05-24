"""Финальный проект первого спринта курса Python-разработчик расширенный."""

# Проект FitLife - MVP версия 1.0
WATER_PER_KG = 30
ML_PER_L = 1000
print('Добро пожаловать в приложение FitLife!')

# 1. Знакомство
# TODO: Спроси у пользователя имя и сохрани в переменную user_name
user_name = input('Как вас зовут? ')
user_name_formatted = user_name.title()

# TODO: Спроси возраст и сохрани в переменную user_age (не забудь преобразовать
# в число)
while True:
    try:
        user_age = int(input('Сколько вам полных лет? '))
        if 0 <= user_age <= 120:
            break
        else:
            print('Введите возраст в диапазоне от 0 до 120 лет.')
    except ValueError:
        print('Введите количество полных лет числом, например: 15.')


# 2. Сбор данных
# TODO: Запроси вес (в кг) и сохрани в user_weight (тип float)
while True:
    try:
        user_weight = float(input('Введите ваш вес (в кг): '))
        if 15 <= user_weight <= 300:
            break
        else:
            print('Введите вес в диапазоне от 15 до 300 кг.')
    except ValueError:
        print('Введите вес в кг, например: 80.5.')

# TODO: Запроси рост (в метрах, например 1.75) и сохрани в user_height (тип
# float)
while True:
    try:
        user_height = float(input('Введите ваш рост (в м): '))
        if 0.5 <= user_height <= 2.5:
            break
        else:
            print('Введите рост в диапазоне от 0.5 до 2.5 м.')
    except ValueError:
        print('Введите рост в м, например: 1.75.')


# 3. Логика расчетов (Функции как "черный ящик": используем арифметику)
# Формула ИМТ: вес разделить на (рост в квадрате)
# TODO: Рассчитай bmi (Индекс массы тела)
bmi = round((user_weight / (user_height ** 2)), 1)

# Подсчет воды: вес * 30 мл
# TODO: Рассчитай water_needed
water_ml = user_weight * WATER_PER_KG
water_l = water_ml / ML_PER_L


# 4. Вывод красивого результата
# TODO: Используй f-строку, чтобы вывести приветствие, например: "Привет,
# Иван!"
print('=' * 45)
print(f'Отчет для пользователя {user_name_formatted}.\n')
# TODO: Выведи возраст, ИМТ (округленный до 1 знака) и норму воды.
print(f'Ваш ИМТ (индекс массы тела): {bmi}')
print(f'Рекомендуемая норма воды: {water_l} л. в день')
print(f"\nРасчет окончен. Будьте здоровы!\n{'=' * 45}")
