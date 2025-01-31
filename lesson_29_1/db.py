import psycopg2

def connect_to_db():
    return psycopg2.connect(
        dbname='testdb',
        user='postgres',
        password='password',
        host='db',
        port='5432'
    )
