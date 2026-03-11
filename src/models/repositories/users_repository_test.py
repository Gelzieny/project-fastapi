import pytest
from sqlalchemy import text

from src.models.repositories.users_repository import UsersRepository
from src.models.settings.database_connection_handler import DBConnectionHandler


@pytest.mark.asyncio
async def test_insert_user():
  users_repository = UsersRepository()

  user_data = {
    "user_name": "Teste",
    "age": 30,
    "uf": "SP"
  }

  await users_repository.insert_users(user_data)

  async with DBConnectionHandler() as session:
    query = text("SELECT * FROM users WHERE user_name = :name")
    result = await session.execute(query, {"name": "Teste"})
    user = result.fetchone()

    assert user is not None
    assert user.user_name == "Teste"


@pytest.mark.asyncio
async def test_get_user_by_name():

    repo = UsersRepository()

    await repo.insert_users({
        "user_name": "Maria",
        "age": 25,
        "uf": "RJ"
    })

    users = await repo.get_user_by_name("Maria")

    assert len(users) > 0
    assert users[0]["user_name"] == "Maria"
    assert users[0]["age"] == 25