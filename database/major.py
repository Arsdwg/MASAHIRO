import aiosqlite
from database.queries import Queries

class DataBase:
    def __init__(self, path) -> None:
        self.path = path

    async def create_table(self) -> None:
        async with aiosqlite.connect(self.path) as db:
            await db.execute(Queries.CREATE_TABLE)
            await db.commit()

    async def execute(self, query: str, params: tuple | None = None) -> None:
        async with aiosqlite.connect(self.path) as db:
            await db.execute(query, params or ())
            await db.commit()
