from typing import Optional
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

CONNECTION_STRING = "sqlite+aiosqlite:///schema.db"

engine = create_async_engine(
  CONNECTION_STRING,
  echo=False,
  pool_size=2,
  max_overflow=0,
  pool_timeout=30,
)

async_session = sessionmaker(bind=engine, expire_on_commit=False, class_=AsyncSession)

class DBConnectionHandler:
  def __init__(self) -> None:
    self.session: Optional[AsyncSession] = None

  async def __aenter__(self):
    self.session = async_session()
    return self.session

  async def __aexit__(self, exc_type, exc, tb):
    await self.session.close()