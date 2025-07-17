from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.google_business_post import GoogleBusinessPost



class BusinessDataGoogleMyBusinessUpdatesTaskGetResultInfo(BaseModel):
    """
    BusinessDataGoogleMyBusinessUpdatesTaskGetResultInfo
    """ # noqa: E501
    keyword: Optional[StrictStr] = Field(default=None, description="keyword received in a POST array. keyword is returned with decoded %## (plus character ‘+’ will be decoded to a space character). this field will contain the cid parameter if you specified it in the keyword field when setting a task;. example:. cid:2946633002421908862. learn more about the parameter in this help center article")
    se_domain: Optional[StrictStr] = Field(default=None, description="search engine domain as specified in a POST array")
    location_code: Optional[StrictInt] = Field(default=None, description="location code in a POST array")
    language_code: Optional[StrictStr] = Field(default=None, description="language code in a POST array")
    check_url: Optional[StrictStr] = Field(default=None, description="direct URL to search engine results. you can use it to make sure that we provided accurate results")
    datetime: Optional[StrictStr] = Field(default=None, description="date and time when the result was received. in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”. example:. 2019-11-15 12:57:46 +00:00")
    business_updates_id: Optional[StrictStr] = Field(default=None, description="identifier of the business updates element in SERP")
    cid: Optional[StrictStr] = Field(default=None, description="google-defined client id. unique id of a local establishment. learn more about the cid identifier in this help center article")
    feature_id: Optional[StrictStr] = Field(default=None, description="the unique identifier of the element in SERP. learn more about the identifier in this help center article")
    item_types: Optional[List[Optional[StrictStr]]] = Field(default=None, description="item types. types of search engine results encountered in the items array;. possible item types: google_business_post")
    items_count: Optional[StrictInt] = Field(default=None, description="item types. the number of items in the items array")
    items: Optional[List[Optional[GoogleBusinessPost]]] = Field(default=None, description="encountered item types. types of search engine results encountered in the items array;. possible item types: google_business_post")
    __properties: ClassVar[List[str]] = [
        "keyword", 
        "se_domain", 
        "location_code", 
        "language_code", 
        "check_url", 
        "datetime", 
        "business_updates_id", 
        "cid", 
        "feature_id", 
        "item_types", 
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

        _dict['keyword'] = self.keyword
        _dict['se_domain'] = self.se_domain
        _dict['location_code'] = self.location_code
        _dict['language_code'] = self.language_code
        _dict['check_url'] = self.check_url
        _dict['datetime'] = self.datetime
        _dict['business_updates_id'] = self.business_updates_id
        _dict['cid'] = self.cid
        _dict['feature_id'] = self.feature_id
        _dict['item_types'] = self.item_types
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
            "keyword": obj.get("keyword"),
            "se_domain": obj.get("se_domain"),
            "location_code": obj.get("location_code"),
            "language_code": obj.get("language_code"),
            "check_url": obj.get("check_url"),
            "datetime": obj.get("datetime"),
            "business_updates_id": obj.get("business_updates_id"),
            "cid": obj.get("cid"),
            "feature_id": obj.get("feature_id"),
            "item_types": obj.get("item_types"),
            "items_count": obj.get("items_count"),
            "items": [GoogleBusinessPost.from_dict(_item) for _item in obj["items"]] if obj.get("items") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj