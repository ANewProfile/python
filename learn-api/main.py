from fastapi import FastAPI

app = FastAPI()

grocery_list = {0: "broccoli", 1: "apples", 2: "chocolate"}

@app.get("/")
async def read_root():
    return { "message": "Hello, world!" }

@app.get("/greet")
async def greet_person(name: str):
    return { "message": f"Hello, {name}!"}

@app.get("/list-items")
async def show_grocery_list():
    return { "items": grocery_list }

@app.post("/add-item")
async def add_item(item: str):
    global grocery_list
    new_id = max(grocery_list.keys()) + 1
    grocery_list[new_id] = item
    return { "message": f"Item {item} added at id {new_id}" }

@app.put("/modify-item")
async def change_item(id: int, new_item: str):
    global grocery_lsit
    grocery_list[id] = new_item
    return { "message": f"Item #{id} changed to {new_item}" }

@app.delete("/remove-item")
async def remove_item(id: int):
    global grocery_list
    try:
        grocery_list.__delitem__(id)
        return { "message": f"Item #{id} successfully removed" }
    except KeyError:
        return { "message": f"Item does not exist with ID {id}" }
