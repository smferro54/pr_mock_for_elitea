from fastapi import FastAPI

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

@app.put("/items/{item_id}")
def update_item(item_id: int, item: str):
    if item_id < 0 or item_id >= len(items):
        return {"error": "Item not found"}
    items[item_id] = item
    return {"message": "Item updated successfully"}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id < 0 or item_id >= len(items):
        return {"error": "Item not found"}
    items.pop(item_id)
    return {"message": "Item deleted successfully"}