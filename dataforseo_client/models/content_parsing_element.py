from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.page_content_info import PageContentInfo



class ContentParsingElement(BaseModel):
    """
    ContentParsingElement
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    fetch_time: Optional[StrictStr] = Field(default=None, description="date and time when the content was fethced. example:. '2022-11-01 10:02:52 +00:00'")
    status_code: Optional[StrictInt] = Field(default=None, description="status code of the page")
    page_content: Optional[PageContentInfo] = Field(default=None, description="parsed content of the page")
    page_as_markdown: Optional[StrictStr] = Field(default=None, description="page content in the markdown format. page content in the text-to-HTML markdown format. specify markdown_view as true in the request to return the value")
    __properties: ClassVar[List[str]] = [
        "type", 
        "fetch_time", 
        "status_code", 
        "page_content", 
        "page_as_markdown", 
        ]

    additional_properties: Dict[str, Any] = Field(default_factory=dict)

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )

    def to_str(self) -> str:
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        excluded_fields: Set[str] = set([
        ])

        _dict = {}

        _dict['type'] = self.type
        _dict['fetch_time'] = self.fetch_time
        _dict['status_code'] = self.status_code
        _dict['page_content'] = self.page_content.to_dict() if self.page_content else None
        _dict['page_as_markdown'] = self.page_as_markdown
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "fetch_time": obj.get("fetch_time"),
            "status_code": obj.get("status_code"),
            "page_content": PageContentInfo.from_dict(obj["page_content"]) if obj.get("page_content") is not None else None,
            "page_as_markdown": obj.get("page_as_markdown"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj