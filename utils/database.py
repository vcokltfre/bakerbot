from asyncpg import create_pool
from asyncio import get_event_loop
from os import environ as env
from json import dumps, loads

with open("./static/init.sql") as f:
    initscript = f.read()


class DatabaseInterface:
    def __init__(self):
        self.creds = {
            "user": env.get("DB_USER", "root"),
            "password": env.get("DB_PASS", "password"),
            "database": env.get("DB_DATABASE", "bakerbot"),
            "host": env.get("DB_HOST", "db")
        }

        get_event_loop().create_task(self.init())

    async def hardreset(self):
        async with self.pool.acquire() as conn:
            await conn.execute("DROP TABLE Users; DROP TABLE Bakeries")
        self.pool = None
        await self.init()

    async def init(self):
        self.pool = await create_pool(**self.creds)

        async with self.pool.acquire() as conn:
            await conn.execute(initscript)

    async def create_user(self, userid: int, username: str):
        async with self.pool.acquire() as conn:
            try:
                await conn.execute("INSERT INTO Users (id, name) VALUES ($1, $2);", userid, username)
                return True
            except Exception as e:
                print(e)
                return False

    async def get_user_id(self, userid: int):
        async with self.pool.acquire() as conn:
            return await conn.fetchrow("SELECT * FROM Users WHERE id = $1;", userid)

    async def create_bakery(self, userid: int, name: str):
        async with self.pool.acquire() as conn:
            await conn.execute("INSERT INTO Bakeries (owner_id, name, inventory) VALUES ($1, $2, $3);", userid, name, dumps({}))

    async def get_bakery_id(self, userid: int):
        async with self.pool.acquire() as conn:
            return await conn.fetchrow("SELECT * FROM Bakeries WHERE owner_id = $1;", userid)