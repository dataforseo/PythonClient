from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.appendix_info import AppendixInfo



class AppendixBusinessListingsBusinessDataLimitsRatesDataInfo(BaseModel):
    """
    AppendixBusinessListingsBusinessDataLimitsRatesDataInfo
    """ # noqa: E501
    search: Optional[AppendixInfo] = Field(default=None, description="")
    categories_aggregation: Optional[AppendixInfo] = Field(default=None, description="")
    categories: Optional[StrictFloat] = Field(default=None, description="")
    locations: Optional[StrictFloat] = Field(default=None, description="")
    __properties: ClassVar[List[str]] = [
        "search", 
        "categories_aggregation", 
        "categories", 
        "locations", 
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

        _dict['search'] = self.search.to_dict() if self.search else None
        _dict['categories_aggregation'] = self.categories_aggregation.to_dict() if self.categories_aggregation else None
        _dict['categories'] = self.categories
        _dict['locations'] = self.locations
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "search": AppendixInfo.from_dict(obj["search"]) if obj.get("search") is not None else None,
            "categories_aggregation": AppendixInfo.from_dict(obj["categories_aggregation"]) if obj.get("categories_aggregation") is not None else None,
            "categories": obj.get("categories"),
            "locations": obj.get("locations"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj