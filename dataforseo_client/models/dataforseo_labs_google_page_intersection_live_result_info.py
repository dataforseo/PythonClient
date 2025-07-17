from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.dataforseo_labs_page_intersection_live_item import DataforseoLabsPageIntersectionLiveItem



class DataforseoLabsGooglePageIntersectionLiveResultInfo(BaseModel):
    """
    DataforseoLabsGooglePageIntersectionLiveResultInfo
    """ # noqa: E501
    se_type: Optional[StrictStr] = Field(default=None, description="search engine type")
    pages: Optional[Dict[str, Optional[StrictStr]]] = Field(default=None, description="URLs you specified a POST array")
    exclude_pages: Optional[List[Optional[StrictStr]]] = Field(default=None, description="URLs you specified in a POST array that will be excluded from the results")
    location_code: Optional[StrictInt] = Field(default=None, description="location code in a POST array")
    language_code: Optional[StrictStr] = Field(default=None, description="language code in a POST array")
    total_count: Optional[StrictInt] = Field(default=None, description="total amount of results in our database relevant to your request")
    items_count: Optional[StrictInt] = Field(default=None, description="the number of results returned in the items array")
    items: Optional[List[Optional[DataforseoLabsPageIntersectionLiveItem]]] = Field(default=None, description="contains keywords, relevant SERP elements and related data")
    __properties: ClassVar[List[str]] = [
        "se_type", 
        "pages", 
        "exclude_pages", 
        "location_code", 
        "language_code", 
        "total_count", 
        "items_count", 
        "items", 
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

        _dict['se_type'] = self.se_type
        _dict['pages'] = self.pages
        _dict['exclude_pages'] = self.exclude_pages
        _dict['location_code'] = self.location_code
        _dict['language_code'] = self.language_code
        _dict['total_count'] = self.total_count
        _dict['items_count'] = self.items_count
        items_items = []
        if self.items:
            for _item in self.items:
                if _item:
                    items_items.append(_item.to_dict())
            _dict['items'] = items_items
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "se_type": obj.get("se_type"),
            "pages": obj.get("pages"),
            "exclude_pages": obj.get("exclude_pages"),
            "location_code": obj.get("location_code"),
            "language_code": obj.get("language_code"),
            "total_count": obj.get("total_count"),
            "items_count": obj.get("items_count"),
            "items": [DataforseoLabsPageIntersectionLiveItem.from_dict(_item) for _item in obj["items"]] if obj.get("items") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj