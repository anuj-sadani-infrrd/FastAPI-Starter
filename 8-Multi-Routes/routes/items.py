from fastapi import APIRouter

api = APIRouter(prefix="/items", tags=["items"])

ITEMS = [
    {"name": "laptop", "price": 50000},
    {"name": "keyboard", "price": 500},
    {"name": "coffee mug", "price": 200},
]
USER_ITEMS = {"anuj": ITEMS, "mohit": ITEMS[1:2]}


@api.get("/")
def get_items():
    return ITEMS


@api.get("/{name}")
def get_user_by_name(name):
    for item in ITEMS:
        if name == item["name"]:
            return item


@api.get("/user/{user_name}", tags=["users"])
def get_user_items(user_name):
    return USER_ITEMS.get(user_name, [])
