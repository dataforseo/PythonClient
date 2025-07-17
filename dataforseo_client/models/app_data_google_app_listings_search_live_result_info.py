from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.app_data_google_app_listings_search_live_item import AppDataGoogleAppListingsSearchLiveItem



class AppDataGoogleAppListingsSearchLiveResultInfo(BaseModel):
    """
    AppDataGoogleAppListingsSearchLiveResultInfo
    """ # noqa: E501
    total_count: Optional[StrictInt] = Field(default=None, description="the total number of relevant results in the database")
    count: Optional[StrictInt] = Field(default=None, description="the number of items in the results array")
    offset: Optional[StrictInt] = Field(default=None, description="offset in the results array of returned apps")
    offset_token: Optional[StrictStr] = Field(default=None, description="token for subsequent requests. you can use this parameter in the POST request to avoid timeouts while trying to obtain over 100,000 results in a single request")
    items: Optional[List[Optional[AppDataGoogleAppListingsSearchLiveItem]]] = Field(default=None, description="array of apps and related data")
    __properties: ClassVar[List[str]] = [
        "total_count", 
        "count", 
        "offset", 
        "offset_token", 
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

        _dict['total_count'] = self.total_count
        _dict['count'] = self.count
        _dict['offset'] = self.offset
        _dict['offset_token'] = self.offset_token
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
            "total_count": obj.get("total_count"),
            "count": obj.get("count"),
            "offset": obj.get("offset"),
            "offset_token": obj.get("offset_token"),
            "items": [AppDataGoogleAppListingsSearchLiveItem.from_dict(_item) for _item in obj["items"]] if obj.get("items") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj