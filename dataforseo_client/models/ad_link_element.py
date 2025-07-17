from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class AdLinkElement(BaseModel):
    """
    AdLinkElement
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    title: Optional[StrictStr] = Field(default=None, description="reference page title")
    description: Optional[StrictStr] = Field(default=None, description="link description")
    url: Optional[StrictStr] = Field(default=None, description="reference page URL")
    domain: Optional[StrictStr] = Field(default=None, description="domain where a link points")
    ad_aclk: Optional[StrictStr] = Field(default=None, description="the identifier of the ad")
    __properties: ClassVar[List[str]] = [
        "type", 
        "title", 
        "description", 
        "url", 
        "domain", 
        "ad_aclk", 
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
        _dict['title'] = self.title
        _dict['description'] = self.description
        _dict['url'] = self.url
        _dict['domain'] = self.domain
        _dict['ad_aclk'] = self.ad_aclk
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "title": obj.get("title"),
            "description": obj.get("description"),
            "url": obj.get("url"),
            "domain": obj.get("domain"),
            "ad_aclk": obj.get("ad_aclk"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj