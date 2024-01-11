# FastAPI is a Python class that provides all the functionality for your API.
from fastapi import FastAPI

# app variable will be an "instance" of the class FastAPI
app = FastAPI()


# "Operation" here refers to one of the HTTP "methods".
# A "path" is also commonly called an "endpoint" or a "route".
@app.get("/")
async def root():  # Note the async keyword is not must unless you are developing asynchronous api
    # return the content
    return {"message": "Hello World"}
