from fastapi import APIRouter
from fastapi.responses import JSONResponse

user_routes = APIRouter(prefix="/users", tags=["Usuários"])

@user_routes.post("/", response_class=JSONResponse)
async def criar_usuario():
    # Lógica para criar um usuário com base no user_id
    return JSONResponse(content={"message": "Hello world!"}, status_code=200)