import sqlite3

def get_user_data(unique_id):
    conn = sqlite3.connect("form_data.db")
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE unique_id = ?', (unique_id,))
    result = cursor.fetchone()
    conn.close()
    return result
