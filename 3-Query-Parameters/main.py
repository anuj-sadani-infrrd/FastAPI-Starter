from fastapi import FastAPI, Path

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


# @app.get("/llms/")
# def query_llm(parameter_size: str) -> list:
#     results = []
#     for llm in llms_list:
#         if parameter_size and llm["parameter_size"].lower() == parameter_size.lower():
#             results.append(llm)
#     return results


@app.get("/llms/")
def query_llm(parameter_size: str | None = None, context_window: int | None = None) -> list:
    def check_param(item):
        return all(
            (
                parameter_size is None or item["parameter_size"].lower() == parameter_size.lower(),
                context_window is None or item["context_window"] == context_window,
            )
        )

    return [llm for llm in llms_list if check_param(llm)]
