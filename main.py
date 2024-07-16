from fastapi import FastAPI

from app.endpoints import frontend
from app.endpoints.api import topsale

app = FastAPI(
    title="妖zon.com",
    description="妖怪ウォッチに出てくる[**妖zon.com**](妖zon.com)のオマージュ",
    version="2024.07.15",
)

app.include_router(frontend.router)
app.include_router(topsale.router)
