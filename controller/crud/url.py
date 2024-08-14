from sqlalchemy import select
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from models.url import Url
from controller.errors.http.exceptions import not_found, bad_request, internal_server_error

class UrlCrud:
    async def get_all_urls(self, async_session: async_sessionmaker[AsyncSession]) -> [Url]:
        async with async_session() as session:
            try:
                statement = select(Url)
                urls = await session.execute(statement)
                return urls.scalars().all()
            except Exception as error:
                await session.rollback()
                raise internal_server_error(f"{error!r}")

    async def get_url_by_alias(self, async_session: async_sessionmaker[AsyncSession], url_alias: str) -> Url:
        async with async_session() as session:
            try:
                statement = select(Url).filter(Url.alias == url_alias)
                url = await session.execute(statement)
                return url.scalars().one()
            except Exception as error:
                await session.rollback()
                raise not_found(f"{error!r}")

    async def get_url_by_url(self, async_session: async_sessionmaker[AsyncSession], url: str, total: int = 0) -> [Url]:
        async with async_session() as session:
            try:
                if total == 0:
                    statement = select(Url).filter(Url.url == url)
                else:
                    statement = select(Url).filter(Url.url == url).limit(total)
                urls = await session.execute(statement)
                return urls.scalars().all()
            except Exception as error:
                await session.rollback()
                raise not_found(f"{error!r}")

    async def create_url(self, async_session: async_sessionmaker[AsyncSession], url: Url) -> Url:
        async with async_session() as session:
            try:
                session.add(url)
                await session.commit()
                return url
            except Exception as error:
                await session.rollback()
                raise bad_request(f"{error!r}")

    async def delete_url(self, async_session: async_sessionmaker[AsyncSession], url: Url) -> str:
        async with async_session() as session:
            try:
                await session.delete(url)
                await session.commit()
                return f"{url.alias} deleted"
            except Exception as error:
                await session.rollback()
                raise not_found(f"{error!r}")

    async def delete_url_by_alias(self, async_session: async_sessionmaker[AsyncSession], url_alias: str) -> str:
        async with async_session() as session:
            try:
                statement = select(Url).filter(Url.alias == url_alias)
                url = await session.execute(statement)
                url = url.scalars().one()
                await session.delete(url)
                await session.commit()
                return f"{url.alias} deleted"
            except Exception as error:
                await session.rollback()
                raise not_found(f"{error!r}")