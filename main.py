from fastapi import FastAPI

from app.endpoints import frontend

app = FastAPI(
    title="妖zon.com",
    description="妖怪ウォッチに出てくる[**妖zon.com**](妖zon.com)のオマージュ",
    version="2024.07.15",
)

app.include_router(frontend.router)
