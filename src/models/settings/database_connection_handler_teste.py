import pytest
from sqlalchemy import text
from src.models.settings.database_connection_handler import DBConnectionHandler

@pytest.mark.asyncio
async def test_connection():
  async with DBConnectionHandler() as session:
    result = await session.execute(text("SELECT 1"))
    assert result.scalar() == 1