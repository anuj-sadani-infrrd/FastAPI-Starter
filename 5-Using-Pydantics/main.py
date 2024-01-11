from fastapi import FastAPI

from llm_dto import LLMModel
from llms import llms_list

app = FastAPI()


@app.get("/llms")
def get_all_llm() -> list[LLMModel]:
    return llms_list


@app.post("/llm")
def add_llm(new_llm: LLMModel):
    llms_list.append(new_llm)
    return new_llm.model_dump()
