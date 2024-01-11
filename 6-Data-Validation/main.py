from uuid import UUID

from fastapi import FastAPI, HTTPException
from starlette import status

from llm_dto import LLMModel
from llms import llms_list

app = FastAPI()


@app.get("/llms", status_code=status.HTTP_200_OK)
def get_all_llm() -> list[LLMModel]:
    return llms_list


@app.post("/llm")
def add_llm(new_llm: LLMModel) -> LLMModel:
    llms_list.append(new_llm)
    return new_llm


# @app.put("/llm/{model_id}", status_code=status.HTTP_204_NO_CONTENT)
@app.put("/llm/{model_id}")
def update_llm(request_llm: LLMModel, model_id: UUID) -> LLMModel:
    request_llm.id = model_id
    for llm in llms_list:
        if llm.id == model_id:
            for key, value in request_llm.model_dump().items():
                setattr(llm, key, value)
            break
    else:
        raise HTTPException(status_code=404, detail="Item not found")

    return request_llm
