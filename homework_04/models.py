"""
создайте алхимичный engine +
добавьте declarative base (свяжите с engine)+
создайте объект Session+
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""

import os

from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncEngine,
    AsyncSession,
)
from sqlalchemy.orm import (
    sessionmaker,
    declarative_base,
    relationship,
)

PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://username:passwd!@localhost/postgres"

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(20), unique=True, nullable=False, default="")
    name = Column(String(40), unique=False, nullable=False, default="")
    email = Column(String(64), unique=True, nullable=False, default="")

    posts = relationship("Post", back_populates="user")

    def __str__(self):
        return f"{self.__class__.__name__}(" f"id={self.id}, " f"name={self.username!r}"


class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True)
    title = Column(String(100), unique=False, nullable=False)
    body = Column(Text, nullable=False, default="")
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, )

    user = relationship("User", back_populates="posts")

    def __str__(self):
        return f"{self.__class__.__name__}(" f"id={self.id}, " f"name={self.title}"


# async
async_engine: AsyncEngine = create_async_engine(
    url=PG_CONN_URI,
    echo=False,
)

Session = sessionmaker(
    async_engine,
    class_=AsyncSession,
    expire_on_commit=False,
)
