from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class TechnologiesInfo(BaseModel):
    """
    TechnologiesInfo
    """ # noqa: E501
    add_ons: Optional[Dict[str, Optional[List[Optional[StrictStr]]]]] = Field(default=None, description="")
    analytics: Optional[Dict[str, Optional[List[Optional[StrictStr]]]]] = Field(default=None, description="")
    web_development: Optional[Dict[str, Optional[List[Optional[StrictStr]]]]] = Field(default=None, description="")
    security: Optional[Dict[str, Optional[List[Optional[StrictStr]]]]] = Field(default=None, description="")
    business_tools: Optional[Dict[str, Optional[List[Optional[StrictStr]]]]] = Field(default=None, description="")
    sales: Optional[Dict[str, Optional[List[Optional[StrictStr]]]]] = Field(default=None, description="")
    other: Optional[Dict[str, Optional[List[Optional[StrictStr]]]]] = Field(default=None, description="")
    user_generated_content: Optional[Dict[str, Optional[List[Optional[StrictStr]]]]] = Field(default=None, description="")
    booking: Optional[Dict[str, Optional[List[Optional[StrictStr]]]]] = Field(default=None, description="")
    privacy: Optional[Dict[str, Optional[List[Optional[StrictStr]]]]] = Field(default=None, description="")
    servers: Optional[Dict[str, Optional[List[Optional[StrictStr]]]]] = Field(default=None, description="")
    location: Optional[Dict[str, Optional[List[Optional[StrictStr]]]]] = Field(default=None, description="")
    content: Optional[Dict[str, Optional[List[Optional[StrictStr]]]]] = Field(default=None, description="")
    media: Optional[Dict[str, Optional[List[Optional[StrictStr]]]]] = Field(default=None, description="")
    marketing: Optional[Dict[str, Optional[List[Optional[StrictStr]]]]] = Field(default=None, description="")
    communication: Optional[Dict[str, Optional[List[Optional[StrictStr]]]]] = Field(default=None, description="")
    utilities: Optional[Dict[str, Optional[List[Optional[StrictStr]]]]] = Field(default=None, description="")
    __properties: ClassVar[List[str]] = [
        "add_ons", 
        "analytics", 
        "web_development", 
        "security", 
        "business_tools", 
        "sales", 
        "other", 
        "user_generated_content", 
        "booking", 
        "privacy", 
        "servers", 
        "location", 
        "content", 
        "media", 
        "marketing", 
        "communication", 
        "utilities", 
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

        _dict['add_ons'] = self.add_ons
        _dict['analytics'] = self.analytics
        _dict['web_development'] = self.web_development
        _dict['security'] = self.security
        _dict['business_tools'] = self.business_tools
        _dict['sales'] = self.sales
        _dict['other'] = self.other
        _dict['user_generated_content'] = self.user_generated_content
        _dict['booking'] = self.booking
        _dict['privacy'] = self.privacy
        _dict['servers'] = self.servers
        _dict['location'] = self.location
        _dict['content'] = self.content
        _dict['media'] = self.media
        _dict['marketing'] = self.marketing
        _dict['communication'] = self.communication
        _dict['utilities'] = self.utilities
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "add_ons": obj.get("add_ons"),
            "analytics": obj.get("analytics"),
            "web_development": obj.get("web_development"),
            "security": obj.get("security"),
            "business_tools": obj.get("business_tools"),
            "sales": obj.get("sales"),
            "other": obj.get("other"),
            "user_generated_content": obj.get("user_generated_content"),
            "booking": obj.get("booking"),
            "privacy": obj.get("privacy"),
            "servers": obj.get("servers"),
            "location": obj.get("location"),
            "content": obj.get("content"),
            "media": obj.get("media"),
            "marketing": obj.get("marketing"),
            "communication": obj.get("communication"),
            "utilities": obj.get("utilities"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj