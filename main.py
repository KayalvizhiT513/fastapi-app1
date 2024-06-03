from fastapi import FastAPI

# Create an instance of the FastAPI class
app = FastAPI()

# Define a route for the root endpoint
@app.get("/")
async def read_root():
    return {"message": "Hello, World"}

# Define a route for a GET request to /items/{item_id}
@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

# Define a route for a POST request to /items/
@app.post("/items/")
async def create_item(item: dict):
    return item
