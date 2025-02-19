import allure
import pytest
from src.database import DBManager  # Використовуємо новий шлях


@allure.feature("Database Operations")
class TestDatabaseCRUD:

    @pytest.fixture(scope="class")
    def db(self):
        db = DBManager()
        yield db
        db.close()

    @allure.story("Connection Test")
    def test_connection(self, db):
        with allure.step("Verify DB connection status"):
            assert db.conn.status == psycopg2.extensions.STATUS_READY

    # Решта тестів...

    @allure.story("CRUD Operations")
    @allure.title("Test record lifecycle")
    def test_full_crud_cycle(self, db):
        # Create
        with allure.step("Create test table"):
            db.execute_query("CREATE TEMP TABLE test (id SERIAL PRIMARY KEY, data VARCHAR);")

        with allure.step("Insert record"):
            db.execute_query("INSERT INTO test (data) VALUES (%s)", ("test_data",))
            result = db.fetch_data("SELECT * FROM test WHERE data = 'test_data'")
            assert len(result) == 1

        # Read
        with allure.step("Read record"):
            result = db.fetch_data("SELECT * FROM test WHERE data = 'test_data'")
            assert result[0]['data'] == "test_data"

        # Update
        with allure.step("Update record"):
            db.execute_query("UPDATE test SET data = %s WHERE data = %s",
                             ("updated_data", "test_data"))
            result = db.fetch_data("SELECT * FROM test WHERE data = 'updated_data'")
            assert len(result) == 1

        # Delete
        with allure.step("Delete record"):
            db.execute_query("DELETE FROM test WHERE data = 'updated_data'")
            result = db.fetch_data("SELECT * FROM test WHERE data = 'updated_data'")
            assert len(result) == 0