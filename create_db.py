from database.db import Base, engine
from asyncio import run

async def create_db():
    async with engine.begin() as conn:
        from models.url import Url

        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    await engine.dispose()

run(create_db())