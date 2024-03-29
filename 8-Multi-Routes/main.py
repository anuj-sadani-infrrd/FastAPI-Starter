from fastapi import FastAPI
from routes import users, items

app = FastAPI()

app.include_router(users.api)
app.include_router(items.api)
