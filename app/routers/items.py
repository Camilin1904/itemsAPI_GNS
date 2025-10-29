from fastapi import APIRouter


router = APIRouter()

items = []

# Query All Items
@router.get("/items/")
async def read_items():
    return items

# Create a single Item
@router.post("/items/")
async def create_item(item: dict):
    item["id"] = len(items) + 1
    items.append(item)
    return item

# Query a single Item by its Id
@router.get("/items/{item_id}")
async def read_item(item_id: int):
    # Search through all Items
    for item in items:
        # If the Item is found, return it
        if item["id"] == item_id:
            return item
    # If the Item is not found, return an error message
    return {"error": "Item not found"}
