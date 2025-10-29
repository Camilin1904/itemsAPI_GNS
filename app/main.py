from fastapi import FastAPI
from app.routers import items

app = FastAPI()

# Import the Item Roter
app.include_router(items.router)