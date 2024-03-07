import pytest
import sqlite3


@pytest.fixture
def db_connection():
    conn = sqlite3.connect('cars.db')
    yield conn
    conn.close()
