def test_check_car_price_above(db_connection):
    # Set a minimal price to check
    min_price = 25000

    # Get up data from table 'cars'
    cursor = db_connection.cursor()
    cursor.execute('SELECT * FROM cars')

    # Test for include any cars with a minimum price from the table
    has_car_above_price = any(row[4] > min_price for row in cursor.fetchall())

    # Assert it)))
    assert has_car_above_price, f'No find any auto with price high  {min_price}.'
