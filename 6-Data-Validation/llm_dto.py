from uuid import UUID, uuid4

from pydantic import BaseModel, Field, field_validator


class LLMModel(BaseModel):
    id: UUID | None = Field(default_factory=uuid4, title="not needed")
    model_name: str = Field(min_length=2, max_length=80)
    organization: str = Field(min_length=1)
    parameter_size: str
    is_multi_modal: bool = False
    architecture: str | None = None
    context_window: int | None = None

    @classmethod
    @field_validator("id", mode="after")
    def set_id(cls, v):
        return v or uuid4()

    class Config:
        json_schema_extra = {
            "example": {
                "model_name": "mistral-7b",
                "organization": "Mistral AI",
                "parameter_size": "7B",
                "is_multi_modal": False,
                "architecture": "Dense Transformer",
                "context_window": 8192,
            }
        }
