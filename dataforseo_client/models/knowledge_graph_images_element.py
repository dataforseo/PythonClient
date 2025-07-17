from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class KnowledgeGraphImagesElement(BaseModel):
    """
    KnowledgeGraphImagesElement
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    url: Optional[StrictStr] = Field(default=None, description="relevant URL in SERP")
    domain: Optional[StrictStr] = Field(default=None, description="domain in SERP of the ad element")
    alt: Optional[StrictStr] = Field(default=None, description="alt tag of the image")
    image_url: Optional[StrictStr] = Field(default=None, description="URL of the image. the URL leading to the image on the original resource or DataForSEO storage (in case the original source is not available)")
    xpath: Optional[StrictStr] = Field(default=None, description="the XPath of the element")
    __properties: ClassVar[List[str]] = [
        "type", 
        "url", 
        "domain", 
        "alt", 
        "image_url", 
        "xpath", 
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
        _dict['url'] = self.url
        _dict['domain'] = self.domain
        _dict['alt'] = self.alt
        _dict['image_url'] = self.image_url
        _dict['xpath'] = self.xpath
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "url": obj.get("url"),
            "domain": obj.get("domain"),
            "alt": obj.get("alt"),
            "image_url": obj.get("image_url"),
            "xpath": obj.get("xpath"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj