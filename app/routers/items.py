from fastapi import APIRouter


router = APIRouter()

items = []

@router.get("/items/")
async def read_items():
    return items

@router.post("/items/")
async def create_item(item: dict):
    item["id"] = len(items) + 1
    items.append(item)
    return item

@router.get("/items/{item_id}")
async def read_item(item_id: int):
    for item in items:
        if item["id"] == item_id:
            return item
    return {"error": "Item not found"}
