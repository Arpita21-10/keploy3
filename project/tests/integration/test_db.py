import sqlite3

def test_create_user():
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE user (id INTEGER PRIMARY KEY, name TEXT)')
    cursor.execute('INSERT INTO user (name) VALUES (?)', ("Alice",))
    conn.commit()

    cursor.execute('SELECT * FROM user')
    result = cursor.fetchone()
    assert result[1] == "Alice"
