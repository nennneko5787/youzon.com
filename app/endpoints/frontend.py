import aiofiles
from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import idna

from ..services import MeigenBotService

router = APIRouter()
templates = Jinja2Templates(directory="pages")


@router.get(
    "/",
    response_class=HTMLResponse,
    include_in_schema=False,
)
async def index(request: Request):
    domain = idna.decode(request.url.hostname.lower()).split(".")
    if (
        domain[0] == "www"
        or domain[0] == "妖zon"
        or domain[0] == "localhost"
        or domain[0] == "127"
    ):
        async with aiofiles.open("./pages/index.html", "r", encoding="utf-8") as f:
            return await f.read()
    elif domain[0] in MeigenBotService.bots:
        context = {"request": request, "bot": MeigenBotService.bots[domain[0]]}
        return templates.TemplateResponse("profile.html", context)
    else:
        raise HTTPException(status_code=404, detail="エラーページは実装されていません")


@router.get(
    "/bots/{botid:str}",
    response_class=HTMLResponse,
    include_in_schema=False,
)
async def profile(request: Request, botid: str):
    domain = idna.decode(request.url.hostname.lower()).split(".")
    if not (
        domain[0] == "www"
        or domain[0] == "妖zon"
        or domain[0] == "localhost"
        or domain[0] == "127"
    ):
        raise HTTPException(status_code=404, detail="エラーページは実装されていません")
    elif botid in MeigenBotService.bots:
        context = {"request": request, "bot": MeigenBotService.bots[botid]}
        return templates.TemplateResponse("profile.html", context)
    else:
        raise HTTPException(status_code=404, detail="エラーページは実装されていません")
