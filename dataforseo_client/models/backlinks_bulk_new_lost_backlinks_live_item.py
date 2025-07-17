from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class BacklinksBulkNewLostBacklinksLiveItem(BaseModel):
    """
    BacklinksBulkNewLostBacklinksLiveItem
    """ # noqa: E501
    target: Optional[StrictStr] = Field(default=None, description="domain, subdomain or webpage from a POST array")
    new_backlinks: Optional[StrictInt] = Field(default=None, description="number of new backlinks. number of new backlinks pointing to the target")
    lost_backlinks: Optional[StrictInt] = Field(default=None, description="number of lost backlinks. number of lost backlinks of the target")
    __properties: ClassVar[List[str]] = [
        "target", 
        "new_backlinks", 
        "lost_backlinks", 
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

        _dict['target'] = self.target
        _dict['new_backlinks'] = self.new_backlinks
        _dict['lost_backlinks'] = self.lost_backlinks
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "target": obj.get("target"),
            "new_backlinks": obj.get("new_backlinks"),
            "lost_backlinks": obj.get("lost_backlinks"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj