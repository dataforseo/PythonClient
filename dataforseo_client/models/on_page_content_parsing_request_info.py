from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class OnPageContentParsingRequestInfo(BaseModel):
    """
    OnPageContentParsingRequestInfo
    """ # noqa: E501
    url: Optional[StrictStr] = Field(default=None, description="URL of the content to parse. required field. URL of the page to parse. example:. https://dataforseo.com/blog/a-versatile-alternative-to-google-trends-exploring-the-power-of-dataforseo-trends-api")
    id: Optional[StrictStr] = Field(default=None, description="ID of the task. required field. you can get this ID in the response of the Task POST endpoint. note: the enable_content_parsing parameter in the POST request must be set to true. example:. '07131248-1535-0216-1000-17384017ad04'")
    markdown_view: Optional[StrictBool] = Field(default=None, description="return page content as markdown. optional field. if set to true, the markdown-formatted content of the page will be returned in the page_as_markdown field of the response;. default value: false")
    __properties: ClassVar[List[str]] = [
        "url", 
        "id", 
        "markdown_view", 
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

        _dict['url'] = self.url
        _dict['id'] = self.id
        _dict['markdown_view'] = self.markdown_view
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "url": obj.get("url"),
            "id": obj.get("id"),
            "markdown_view": obj.get("markdown_view"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj