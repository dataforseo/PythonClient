from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.advertiser import Advertiser
from dataforseo_client.models.base_serp_api_ads_advertiser_element_item import BaseSerpApiAdsAdvertiserElementItem



class SerpApiAdsMultiAccountAdvertiserElementItem(BaseSerpApiAdsAdvertiserElementItem):
    """
    SerpApiAdsMultiAccountAdvertiserElementItem
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    rank_group: Optional[StrictInt] = Field(default=None, description="group rank in SERP. position within a group of elements with identical type values. positions of elements with different type values are omitted from rank_group")
    rank_absolute: Optional[StrictInt] = Field(default=None, description="absolute rank in SERP. absolute position among all the elements in SERP")
    title: Optional[StrictStr] = Field(default=None, description="title of the element")
    location: Optional[StrictStr] = Field(default=None, description="advertiser location")
    approx_ads_count: Optional[StrictInt] = Field(default=None, description="ads count. the approximate number of ads that are run by the advertiser across all available Google Ads platforms")
    advertisers: Optional[List[Optional[Advertiser]]] = Field(default=None, description="associated advertiser accounts. contains objects with data on associated advertiser accounts")
    __properties: ClassVar[List[str]] = [
        "type", 
        "rank_group", 
        "rank_absolute", 
        "title", 
        "location", 
        "approx_ads_count", 
        "advertisers", 
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
        _dict['rank_group'] = self.rank_group
        _dict['rank_absolute'] = self.rank_absolute
        _dict['title'] = self.title
        _dict['location'] = self.location
        _dict['approx_ads_count'] = self.approx_ads_count
        advertisers_items = []
        if self.advertisers:
            for _item in self.advertisers:
                if _item:
                    advertisers_items.append(_item.to_dict())
            _dict['advertisers'] = advertisers_items
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "rank_group": obj.get("rank_group"),
            "rank_absolute": obj.get("rank_absolute"),
            "title": obj.get("title"),
            "location": obj.get("location"),
            "approx_ads_count": obj.get("approx_ads_count"),
            "advertisers": [Advertiser.from_dict(_item) for _item in obj["advertisers"]] if obj.get("advertisers") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj