from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse, HTMLResponse

from routes.user_route import user_routes

app = FastAPI(
  title="Api Portal IA",
  description=""
)

app.include_router(user_routes)


@app.get("/", include_in_schema=False)
async def redirect_to_docs():
  return RedirectResponse(url="/docs")

@app.get("/monitor", tags=["Health"])
async def statusaplicacao():
  return True


