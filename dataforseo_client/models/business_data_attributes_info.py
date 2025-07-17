from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class BusinessDataAttributesInfo(BaseModel):
    """
    BusinessDataAttributesInfo
    """ # noqa: E501
    available_attributes: Optional[Dict[str, Optional[List[Optional[StrictStr]]]]] = Field(default=None, description="available attributes. indicates attributes a business entity can offer")
    unavailable_attributes: Optional[Dict[str, Optional[List[Optional[StrictStr]]]]] = Field(default=None, description="unavailable attributes. indicates attributes a business entity cannot offer")
    __properties: ClassVar[List[str]] = [
        "available_attributes", 
        "unavailable_attributes", 
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

        _dict['available_attributes'] = self.available_attributes
        _dict['unavailable_attributes'] = self.unavailable_attributes
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "available_attributes": obj.get("available_attributes"),
            "unavailable_attributes": obj.get("unavailable_attributes"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj