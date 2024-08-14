from pydantic import BaseModel, ConfigDict
from datetime import datetime

class UrlModel(BaseModel):
    id: str
    url: str
    alias: str
    posted_at: datetime

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": "id of the object",
                "url": "url of the object",
                "alias": "alias of the object",
                "posted_at": "when object was posted"
            }
        }
    )

class CreateUrlModel(BaseModel):
    alias: str
    url: str

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example":{
                "alias": "alias of url",
                "url": "url"
            }
        }
    )