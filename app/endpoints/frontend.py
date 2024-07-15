from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
import aiofiles

router = APIRouter()


@router.get(
    "/",
    response_class=HTMLResponse,
    include_in_schema=False,
)
async def index(request: Request):
    async with aiofiles.open("./pages/index.html", "r") as f:
        return await f.read()
