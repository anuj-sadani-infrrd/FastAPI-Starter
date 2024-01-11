from fastapi import FastAPI, Path, Body

from llms import llms_list

app = FastAPI()


@app.get("/llms")
def get_all_llm() -> list:
    return llms_list


@app.get("/llms/{name}")
def get_llm_by_name(name: str | None = Path(description="Name of the LLM", max_length=10)) -> dict:
    for llm in llms_list:
        if name.lower() == llm["model_name"].lower():
            return llm
    return {}


@app.post("/llm")
def add_llm(new_llm=Body()):
    llms_list.append(new_llm)


@app.put("/llm")
def update_llm(updated_llm=Body()):
    for llm in llms_list:
        try:
            if llm["model_name"] == updated_llm["model_name"]:
                llm.update(updated_llm)
                break
        except KeyError:
            pass


@app.delete("/llm/{model_name}")
def delete_llm(model_name: str):
    for llm in llms_list:
        try:
            if llm["model_name"] == model_name:
                llms_list.remove(llm)
                break
        except KeyError:
            pass
