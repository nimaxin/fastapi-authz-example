from pydantic import BaseModel as PydanticBaseModel
from pydantic import ConfigDict, alias_generators


class BaseSchema(PydanticBaseModel):
    model_config = ConfigDict(
        alias_generator=alias_generators.to_camel,
        populate_by_name=True,
        from_attributes=True,
        str_strip_whitespace=True,
    )
