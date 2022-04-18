class CoffeeHouse:


    def __init__(self, db_connect):
        self.database_object = db_connect



    def barista_random_select(self):
        barista = self.database_object.select_one_random_row('name, id', 'cofffeeee_person', ('post', "'Бариста'"))
        print("Вас обслуживает Бариста,", barista[0], "его id -", barista[1])
        return barista



    def user_check(self,checked_name):

        name = checked_name.upper()

        result_name = self.database_object.check_user('name, id', 'cofffeeee_client', ('name', f"'{name}'"))

        print(result_name)
        if result_name:
            print("Клиент найден в базе данных")
            client_id = result_name[1]
            return client_id
        else:
            print("Клиент не найден")
            client_id = self.database_object.insert('cofffeeee_client', {'name': f"'{name}'"})
            return client_id

    def volume_check(self):
        try:
            final_volume = int(input('Объем стакана?:\n'))
            if final_volume < 1 or final_volume < 200:
                raise UserWarning('')

        except UserWarning:
            print("Мы не наливаем в стаканы меньше 200 мл.")
            return self.volume_check()
        except ValueError:
            print('Введите корректное значение.')
            return self.volume_check()
        return final_volume

    def get_milk(self,name, volume):
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
            return self.get_milk(name, volume)

    def grade_coffee(self):
        try:
            grade = int(input('Оцените нашу работу от 1 до 5:'))
            if grade < 1 or grade > 5:
                raise ValueError('')
        except:
            print('Пожалуйста, поставьте оценку от 1 до 5')
            return self.grade_coffee()
        return grade

    def run_coffee_shop(self):
        name_any = input('Ваше имя?\n')

        barista = self.barista_random_select()

        check_user = self.user_check(name_any)
        print(check_user)

        volume_check = self.volume_check()
        order_id = self.database_object.insert('cofffeeee_order',
                                          {'client_id': str(check_user), 'person_id': str(barista[1])})
        res_get_milk = self.get_milk(name_any, volume_check)

        self.database_object.update_db(volume_check, res_get_milk, order_id)

        final_grade = self.grade_coffee()

        self.database_object.update_dbone(final_grade, "grade", order_id)