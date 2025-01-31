import psycopg2
import os

def get_db_connection():
    """Create and return a database connection."""
    conn = psycopg2.connect(
        dbname=os.getenv('DATABASE_NAME', 'test_db'),
        user=os.getenv('DATABASE_USER', 'postgres'),
        password=os.getenv('DATABASE_PASSWORD', 'password'),
        host=os.getenv('DATABASE_HOST', 'localhost'),
        port=os.getenv('DATABASE_PORT', '5432')
    )
    return conn

def insert_user(name, email):
    """Insert a new user into the database."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO users (name, email) VALUES (%s, %s) RETURNING id;
    ''', (name, email))
    user_id = cursor.fetchone()[0]
    conn.commit()
    cursor.close()
    conn.close()
    return user_id

def update_user_email(user_id, new_email):
    """Update user's email by user ID."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
    UPDATE users SET email = %s WHERE id = %s RETURNING id;
    ''', (new_email, user_id))
    updated_user_id = cursor.fetchone()[0]
    conn.commit()
    cursor.close()
    conn.close()
    return updated_user_id

def get_user_by_id(user_id):
    """Fetch user by their ID."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
    SELECT id, name, email FROM users WHERE id = %s;
    ''', (user_id,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return user

def delete_user(user_id):
    """Delete a user from the database by user ID."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
    DELETE FROM users WHERE id = %s RETURNING id;
    ''', (user_id,))
    deleted_user_id = cursor.fetchone()[0]
    conn.commit()
    cursor.close()
    conn.close()
    return deleted_user_id
