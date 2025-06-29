import sqlite3

conn = sqlite3.connect("users.db")
c = conn.cursor()

# Drop table if exists
c.execute("DROP TABLE IF EXISTS users")

# Create table
c.execute("""
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL
)
""")

# Insert some fake users
c.execute("INSERT INTO users (username, password) VALUES ('admin', 'admin123')")
c.execute("INSERT INTO users (username, password) VALUES ('richaa', 'heartping')")
c.execute("INSERT INTO users (username, password) VALUES ('guest', '1234')")

conn.commit()
conn.close()

print("Database created successfully.")
