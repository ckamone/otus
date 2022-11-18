"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""
import asyncio

from sqlalchemy.ext.asyncio import (
    AsyncSession,
)

from jsonplaceholder_requests import fetch_users_data, fetch_posts_data
from models import Base, User, Post, Session, async_engine


async def create_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def create_user(
        session: AsyncSession,
        username: str,
        name: str,
        email: str
) -> User:
    user = User(
        username=username,
        name=name,
        email=email,
    )
    session.add(user)
    print("user create", user)

    await session.commit()
    print("user saved", user)

    return user


async def create_users(conn, users_info_list):
    tasks = set()
    for user_info in users_info_list:
        tasks.add(asyncio.create_task(create_user(
            session=conn,
            username=user_info['username'],
            name=user_info['name'],
            email=user_info['email'],
        )))
        await asyncio.wait(tasks)


async def create_post(
        session: AsyncSession,
        user_id: int,
        title: str,
        body: str
) -> User:
    post = Post(
        user_id=user_id,
        title=title,
        body=body,
    )
    session.add(post)
    print("post create", post)

    await session.commit()
    print("post saved", post)

    return post


async def create_posts(conn, posts_info_list):
    tasks = set()
    for post_info in posts_info_list:
        tasks.add(asyncio.create_task(create_post(
            session=conn,
            user_id=post_info['userId'],
            title=post_info['title'],
            body=post_info['body'],
        )))
        await asyncio.wait(tasks)


async def async_main():
    await create_tables()
    users_data, posts_data = await asyncio.gather(fetch_users_data(), fetch_posts_data())

    async with Session() as conn:
        await create_users(conn, users_data)
        await create_posts(conn, posts_data)


def main():
    coro_1 = async_main()
    asyncio.run(coro_1)


if __name__ == "__main__":
    main()
