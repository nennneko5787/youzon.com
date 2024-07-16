from typing import List

from fastapi import APIRouter

from ...objects import Item
from ...services import ItemService

router = APIRouter(prefix="/api")


@router.get(
    "/topsales",
    summary="トップメニューに表示する商品の一覧を取得します。",
    response_model=List[Item],
)
async def topsale():
    """
    トップメニューに表示する商品の一覧を取得します。
    """
    return ItemService.getItems(21)
