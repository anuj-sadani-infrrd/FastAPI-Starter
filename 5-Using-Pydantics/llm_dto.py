from pydantic import BaseModel


class LLMModel(BaseModel):
    id: int
    model_name: str
    organization: str
    parameter_size: str
    is_multi_modal: bool = False
    architecture: str | None = None
    context_window: int | None = None
