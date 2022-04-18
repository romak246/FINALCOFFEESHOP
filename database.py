import pymysql
from psycopg2 import sql


class Database:
    def __init__(self, host, user, password, db):
        self.connection = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=db,
        )
        self.cur = self.connection.cursor()

    def __del__(self):
        self.connection.close()
        print("Спасибо за заказ, всего доброго!")

    def select_one_random_row(self, select_fields, table, where):
        self.cur.execute(f"SELECT {select_fields} FROM {table} WHERE {where[0]} = {where[1]} ORDER BY RAND()")
        return self.cur.fetchone()

    def check_user(self, select_field, table, where):
        self.cur.execute(f"SELECT {select_field} FROM {table} WHERE {where[0]} = {where[1]} ")
        return self.cur.fetchone()


    def insert(self, table, insert_data):
        fields = ', '.join(insert_data)
        values = ', '.join(str(x) for x in insert_data.values())
        self.cur.execute(f"INSERT INTO {table} (" + fields + ") VALUES (" + values + ")")
        returning_id = self.connection.insert_id()
        self.connection.commit()
        return returning_id

    def update_db(self, volume_size, milk_availability, number_of_order):
        self.cur.execute(
            f"UPDATE cofffeeee_order SET  volume ='{volume_size}', is_milk = '{milk_availability}' WHERE  id = '{number_of_order}' ")
        self.connection.commit()

    def update_dbone(self, value, updated_column, key_value):
        self.cur.execute(
            f"UPDATE cofffeeee_order SET {updated_column} = '{value}' WHERE  id = '{key_value}' ")
        self.connection.commit()


def volume_check():
    try:
        final_volume = int(input('Объем стакана?:\n'))
        if final_volume < 1 or final_volume < 200:
            raise UserWarning('')

    except UserWarning:
        print("Мы не наливаем в стаканы меньше 200 мл.")
        return volume_check()
    except ValueError:
        print('Введите корректное значение.')
        return volume_check()
    return final_volume

# def update_grade(final_grade,order_id):
#     connection = pymysql.connect(
#         host='localhost',
#         user='root',
#         password='14481488Russia!',
#         database='Coffee_house',
#     )
#
#     cur = connection.cursor()
#     cur.execute(
#         f"UPDATE Orderlist SET Grade = '{final_grade}' WHERE  id = '{order_id}' ")
#     connection.commit()
#     connection.close()
