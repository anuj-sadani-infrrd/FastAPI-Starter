from llm_dto import LLMModel

llms_list = [
    {
        "model_name": "bard",
        "organization": "Google AI",
        "parameter_size": "137B",
        "is_multi_modal": True,
        "architecture": "Transformer-based with Meena decoder",
        "context_window": 4096,
    },
    {
        "model_name": "gpt3.5",
        "organization": "OpenAI",
        "parameter_size": "175B",
        "is_multi_modal": False,
        "architecture": "Transformer-based with decoder-only architecture",
        "context_window": 2048,
    },
    {
        "model_name": "gpt4",
        "organization": "OpenAI",
        "parameter_size": "unreleased",
        "is_multi_modal": False,
        "architecture": "unreleased",
        "context_window": None,
    },
    {
        "model_name": "llama2-7b",
        "organization": "Meta",
        "parameter_size": "7B",
        "is_multi_modal": False,
        "architecture": "Transformer-based with dense attention",
        "context_window": 4096,
    },
    {
        "model_name": "claud2",
        "organization": "Anthropic",
        "parameter_size": "137B",
        "is_multi_modal": True,
        "architecture": "Transformer-based with vision and language encoders",
        "context_window": 100000,
    },
    {
        "model_name": "mistral-7b",
        "organization": "Mistral AI",
        "parameter_size": "7B",
        "is_multi_modal": False,
        "architecture": "Dense Transformer",
        "context_window": 8192,
    },
]

llms_list = [LLMModel(id=ix, **llm) for ix, llm in enumerate(llms_list, start=1)]
