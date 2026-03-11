from sqlalchemy import insert, select
from src.models.entities.users import Users
from src.models.settings.database_connection_handler import DBConnectionHandler

class UsersRepository:

  async def insert_users(self, user_infos: dict) -> None:
    async with DBConnectionHandler() as db_session:
      insert_query = insert(Users).values(**user_infos)
      await db_session.execute(insert_query)
      await db_session.commit()

  async def get_user_by_name(self, name: str) -> list[dict]:
    async with DBConnectionHandler() as db_session:
      query = select(Users).where(Users.c.user_name == name)
      result = await db_session.execute(query)
      users = result.mappings().all()
      return users