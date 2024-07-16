import aiofiles
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

router = APIRouter()


@router.get(
    "/",
    response_class=HTMLResponse,
    include_in_schema=False,
)
async def index(request: Request):
    async with aiofiles.open("./pages/index.html", "r", encoding="utf-8") as f:
        return await f.read()
