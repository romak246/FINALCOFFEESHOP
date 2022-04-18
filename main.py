from database import Database, volume_check

database_object = Database('localhost', 'root', '14481488Russia!', 'coffee_house_django')

barista = database_object.select_one_random_row('name, id', 'cofffeeee_person', ('post', "'Бариста'"))
print("Вас обслуживает Бариста,", barista[0], "его id -", barista[1])
name_any = input('Ваше имя?\n')
name = name_any.upper()

result_name = database_object.check_user('name, id','cofffeeee_client', ('name', f"'{name}'"))

print(result_name)
if result_name:
    print("Клиент найден в базе данных")
    client_id = result_name[1]
else:
    print("Клиент не найден")
    client_id = database_object.insert('cofffeeee_client', {'name': f"'{name}'"})
volume = volume_check()

order_id = database_object.insert('cofffeeee_order', {'client_id': str(client_id), 'person_id': str(barista[1])})


def get_milk(name, volume):
    milks = input('Добавить ли молоко?\n')
    milk = milks.lower()
    if milk == 'да':
        print('Готово, ваш кофе,', name + ',', 'объем составил', volume, 'мл, с молоком.')
        return 1
    elif milk == 'нет':
        print('Готово, ваш кофе,', name + ',', 'объем составил', volume, 'мл, без молока.')
        return 0
    else:
        print('Пожалуйста введите Да или Нет')
        return get_milk(name, volume)


res_get_milk = get_milk(name, volume)
database_object.update_db( volume, res_get_milk, order_id)


def grade_coffee():
    try:
        grade = int(input('Оцените нашу работу от 1 до 5:'))
        if grade < 1 or grade > 5:
            raise ValueError('')
    except:
        print('Пожалуйста, поставьте оценку от 1 до 5')
        return grade_coffee()
    return grade


final_grade = grade_coffee()

print("Ваша оценка - ", final_grade)

database_object.update_dbone(final_grade,"grade", order_id)
