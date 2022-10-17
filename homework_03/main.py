from fastapi import FastAPI
from items_views import router as items_router
from ping_views import router as ping_router

app = FastAPI()
app.include_router(items_router)
app.include_router(ping_router)

@app.get("/")
def read_root():
    return {"Hello": "World"}