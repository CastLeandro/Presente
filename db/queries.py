import asyncpg

class Database:
    _pool = None

    @classmethod
    async def connect(cls):
        if not cls._pool:
            cls._pool = await asyncpg.create_pool(
                user= 'postgres',
                password= ''
            )