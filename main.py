from fastapi import FastAPI
from typing import List

app = FastAPI()

# Simple in-memory storage for items
items = []

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI app!"}

@app.get("/items")
def read_items():
    return items

@app.post("/items")
def create_item(item: str):
    items.append(item)
    return {"message": "Item created successfully"}

@app.post("/items/batch")
def create_items_batch(item_list: List[str]):
    items.extend(item_list)
    return {"message": f"{len(item_list)} items created successfully"}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: str):
    if item_id < 0 or item_id >= len(items):
        return {"error": "Item not found"}
    items[item_id] = item
    return {"message": "Item updated successfully"}

@app.put("/items/batch")
def update_items_batch(item_updates: List[dict]):
    updated_items = []
    for update in item_updates:
        item_id = update.get("item_id")
        item = update.get("item")
        if item_id is None or item is None:
            continue
        if item_id >= 0 and item_id < len(items):
            items[item_id] = item
            updated_items.append(item_id)
    return {"message": f"{len(updated_items)} items updated successfully"}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id < 0 or item_id >= len(items):
        return {"error": "Item not found"}
    items.pop(item_id)
    return {"message": "Item deleted successfully"}

@app.delete("/items/batch")
def delete_items_batch(item_ids: List[int]):
    deleted_items = []
    for item_id in item_ids:
        if item_id >= 0 and item_id < len(items):
            items.pop(item_id)
            deleted_items.append(item_id)
    return {"message": f"{len(deleted_items)} items deleted successfully"}