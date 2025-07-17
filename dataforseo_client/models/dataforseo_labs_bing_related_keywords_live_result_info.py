from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.keyword_data_info import KeywordDataInfo
from dataforseo_client.models.dataforseo_labs_related_keywords_live_item import DataforseoLabsRelatedKeywordsLiveItem



class DataforseoLabsBingRelatedKeywordsLiveResultInfo(BaseModel):
    """
    DataforseoLabsBingRelatedKeywordsLiveResultInfo
    """ # noqa: E501
    se_type: Optional[StrictStr] = Field(default=None, description="search engine type")
    seed_keyword: Optional[StrictStr] = Field(default=None, description="keyword in a POST array")
    seed_keyword_data: Optional[KeywordDataInfo] = Field(default=None, description="keyword data for the seed keyword. fields in the array are identical to that of keyword_data")
    location_code: Optional[StrictInt] = Field(default=None, description="location code in a POST array")
    language_code: Optional[StrictStr] = Field(default=None, description="language code in a POST array")
    total_count: Optional[StrictInt] = Field(default=None, description="total amount of results in our database relevant to your request")
    items_count: Optional[StrictInt] = Field(default=None, description="the number of results returned in the items array")
    items: Optional[List[Optional[DataforseoLabsRelatedKeywordsLiveItem]]] = Field(default=None, description="contains keywords and related data")
    __properties: ClassVar[List[str]] = [
        "se_type", 
        "seed_keyword", 
        "seed_keyword_data", 
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
        _dict['seed_keyword'] = self.seed_keyword
        _dict['seed_keyword_data'] = self.seed_keyword_data.to_dict() if self.seed_keyword_data else None
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
            "seed_keyword": obj.get("seed_keyword"),
            "seed_keyword_data": KeywordDataInfo.from_dict(obj["seed_keyword_data"]) if obj.get("seed_keyword_data") is not None else None,
            "location_code": obj.get("location_code"),
            "language_code": obj.get("language_code"),
            "total_count": obj.get("total_count"),
            "items_count": obj.get("items_count"),
            "items": [DataforseoLabsRelatedKeywordsLiveItem.from_dict(_item) for _item in obj["items"]] if obj.get("items") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj