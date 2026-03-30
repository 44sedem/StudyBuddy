class PromptManager:
    """Central registry for all prompt templates with versioning"""
    _prompts = {}

    @classmethod
    def register(cls, name: str, version: int, template: str):
        cls._prompts[f"{name}_v{version}"] = template

    @classmethod
    def get(cls, name: str, version: int = 1) -> str:
        return cls._prompts.get(f"{name}_v{version}", "")
