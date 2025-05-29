from fastapi import APIRouter, HTTPException
from typing import Optional
from schemas.item import Item, ItemOut

router = APIRouter()

@router.post("/", response_model=ItemOut)
async def create_item(item: Item):
    price_with_tax = item.price + (item.tax or 0)
    return ItemOut(name=item.name, price_with_tax=price_with_tax)

@router.put("/{item_id}")
async def update_item(
    item_id: int,
    item: Item,
    q: Optional[str] = None
):
    return {"item_id": item_id, **item.dict(), **({"q": q} if q else {})}
