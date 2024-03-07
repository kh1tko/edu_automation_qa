def test_check_car_price_above(db_connection):
    # Задаємо мінімальну ціну для перевірки
    min_price = 25000

    # Дістаємо дані із таблиці "cars"
    cursor = db_connection.cursor()
    cursor.execute('SELECT * FROM cars')

    # Перевіряємо чи є хоча би один автомобіль вище ніж наша заданна мінімальна ціна
    has_car_above_price = any(row[4] > min_price for row in cursor.fetchall())

    # Асертемо )))
    assert has_car_above_price, f'No find any auto with price high  {min_price}.'
