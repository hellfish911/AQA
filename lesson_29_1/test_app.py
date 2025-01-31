import pytest
import psycopg2
import time


def connect_to_db():
    retries = 5
    delay = 5  # seconds
    while retries > 0:
        try:
            conn = psycopg2.connect(
                dbname='testdb',
                user='postgres',
                password='password',
                host='db',
                port=5432
            )
            return conn
        except psycopg2.OperationalError as e:
            print(f"Database connection failed. Retrying in {delay} seconds...")
            time.sleep(delay)
            retries -= 1
    raise Exception("Unable to connect to the database after multiple attempts")

@pytest.fixture
def db_connection():
    conn = connect_to_db()
    yield conn
    conn.close()

# Test 1: Insert record and check
def test_insert(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS test_table (id SERIAL PRIMARY KEY, name VARCHAR(100));")
    cursor.execute("INSERT INTO test_table (id, name) VALUES (1, 'Test')")
    db_connection.commit()

    cursor.execute("SELECT * FROM test_table WHERE id = 1;")
    result = cursor.fetchone()

    assert result is not None
    assert result[1] == 'Test'

# Test 2: Select record
def test_select(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM test_table WHERE id = 1;")
    result = cursor.fetchone()

    assert result is not None
    assert result[1] == 'Test'

# Test 3: Update record and check
def test_update(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("UPDATE test_table SET name = 'Updated Test' WHERE id = 1;")
    db_connection.commit()

    cursor.execute("SELECT * FROM test_table WHERE id = 1;")
    result = cursor.fetchone()

    assert result is not None
    assert result[1] == 'Updated Test'
