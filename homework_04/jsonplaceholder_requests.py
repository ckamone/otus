"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"

import aiohttp

async def fetch_users_data():
    async with aiohttp.ClientSession() as session:
        response = await session.get(USERS_DATA_URL)
        data = await response.json()
        return data

async def fetch_posts_data():
    async with aiohttp.ClientSession() as session:
        response = await session.get(POSTS_DATA_URL)
        data = await response.json()
        return data

