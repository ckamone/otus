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
import asyncio
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
    declared_attr,
    scoped_session,
)


PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://username:passwd!@localhost/postgres"
print(PG_CONN_URI)


class Base:
    @declared_attr
    def __tablename__(cls):
        return f"{cls.__name__.lower()}s"
    id = Column(Integer, primary_key=True)
    def __repr__(self):
        return str(self)


async_engine: AsyncEngine = create_async_engine(
    url=PG_CONN_URI,
    echo=True,
)
Base = declarative_base(bind=async_engine, cls=Base)

session_factory = sessionmaker(
    async_engine,
    class_=AsyncSession,
    expire_on_commit=False,
)
Session=scoped_session(session_factory)
class User(Base):
    name = Column(String(64), unique=False, nullable=False, default="")
    username = Column(String(64), unique=True, nullable=False, default="")
    email = Column(String(64), unique=True, nullable=False, default="")
    user_id = Column(Integer, ForeignKey("users_id"), nullable=False, unique=True)

    posts = relationship("Post", back_populates="user", uselist=True)
    def __str__(self):
        return f"{self.__class__.__name__}(" f"id={self.id}, " f"name={self.name}"
class Post(Base):
    title = Column(String(64), unique=False, nullable=False)
    body = Column(Text, nullable=False, default="")
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False,)

    user = relationship("User", back_populates="posts", uselist=False)
    def __str__(self):
        return f"{self.__class__.__name__}(" f"id={self.id}, " f"name={self.title}"