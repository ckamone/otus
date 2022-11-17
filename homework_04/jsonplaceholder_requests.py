"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


import aiohttp
import asyncio

async def fetch_json(url):
    async with aiohttp.ClientSession() as session:
        response = await session.get(url)
        data = await response.json()
        print(data)
        return data



def main():
    asyncio.run(fetch_json(USERS_DATA_URL))
    asyncio.run(fetch_json(POSTS_DATA_URL))


if __name__ == "__main__":
    main()