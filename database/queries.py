class Queries:
    CREATE_TABLE = '''CREATE TABLE IF NOT EXISTS survey (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    rate INTEGER NOT NULL CHECK (rate > 0 AND rate < 6),
    capt TEXT
    )'''