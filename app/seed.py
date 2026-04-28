from db import get_db_connection
import time

time.sleep(5)

conn = get_db_connection()
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name TEXT
);
""")

cur.execute("INSERT INTO users (name) VALUES ('Yogesh'), ('Rahul'), ('Amit');")

conn.commit()
cur.close()
conn.close()

print("Seed done")
