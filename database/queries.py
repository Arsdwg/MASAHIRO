class Queries:
    CREATE_TABLE = '''CREATE TABLE IF NOT EXISTS survey (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    rate TEXT,
    capt TEXT
    )'''