from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class DomainAnalyticsTechnologiesAggregationTechnologiesLiveItem(BaseModel):
    """
    DomainAnalyticsTechnologiesAggregationTechnologiesLiveItem
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    group: Optional[StrictStr] = Field(default=None, description="technology group id")
    category: Optional[StrictStr] = Field(default=None, description="technology category id")
    technology: Optional[StrictStr] = Field(default=None, description="technology name")
    groups_count: Optional[StrictInt] = Field(default=None, description="technology groups count. number of domains that match the parameters you specified and are using technologies from the indicated group")
    categories_count: Optional[StrictInt] = Field(default=None, description="technology categories count. number of domains that match the parameters you specified and are using technologies from the indicated category")
    technologies_count: Optional[StrictInt] = Field(default=None, description="technologies count. number of domains that match the parameters you specified and are using the indicated technology")
    __properties: ClassVar[List[str]] = [
        "type", 
        "group", 
        "category", 
        "technology", 
        "groups_count", 
        "categories_count", 
        "technologies_count", 
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
        _dict['group'] = self.group
        _dict['category'] = self.category
        _dict['technology'] = self.technology
        _dict['groups_count'] = self.groups_count
        _dict['categories_count'] = self.categories_count
        _dict['technologies_count'] = self.technologies_count
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "group": obj.get("group"),
            "category": obj.get("category"),
            "technology": obj.get("technology"),
            "groups_count": obj.get("groups_count"),
            "categories_count": obj.get("categories_count"),
            "technologies_count": obj.get("technologies_count"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj