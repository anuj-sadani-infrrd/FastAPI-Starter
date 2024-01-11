from fastapi import FastAPI

from llms import llms_list

app = FastAPI()


@app.get("/llms")
def get_all_llm() -> list:
    return llms_list


@app.get("/llm/{name}")
def get_llm_by_name(name: str) -> dict:  # try with typehints and comment out line 18
    for llm in llms_list:
        if name.lower() == llm["model_name"].lower():
            return llm
    return {}


# Important: Chronology matters top-to-bottom
@app.get("/llm/infrrd_llm")
def get_best_llm():
    return {"model_name": "ILLM"}
