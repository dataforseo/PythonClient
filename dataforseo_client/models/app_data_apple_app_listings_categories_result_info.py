from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class AppDataAppleAppListingsCategoriesResultInfo(BaseModel):
    """
    AppDataAppleAppListingsCategoriesResultInfo
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="task identifier. unique task identifier in our system in the UUID format")
    se: Optional[StrictStr] = Field(default=None, description="")
    se_type: Optional[StrictStr] = Field(default=None, description="")
    date_posted: Optional[StrictStr] = Field(default=None, description="")
    tag: Optional[StrictStr] = Field(default=None, description="")
    endpoint_advanced: Optional[StrictStr] = Field(default=None, description="")
    endpoint_html: Optional[StrictStr] = Field(default=None, description="")
    __properties: ClassVar[List[str]] = [
        "id", 
        "se", 
        "se_type", 
        "date_posted", 
        "tag", 
        "endpoint_advanced", 
        "endpoint_html", 
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

        _dict['id'] = self.id
        _dict['se'] = self.se
        _dict['se_type'] = self.se_type
        _dict['date_posted'] = self.date_posted
        _dict['tag'] = self.tag
        _dict['endpoint_advanced'] = self.endpoint_advanced
        _dict['endpoint_html'] = self.endpoint_html
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "se": obj.get("se"),
            "se_type": obj.get("se_type"),
            "date_posted": obj.get("date_posted"),
            "tag": obj.get("tag"),
            "endpoint_advanced": obj.get("endpoint_advanced"),
            "endpoint_html": obj.get("endpoint_html"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj