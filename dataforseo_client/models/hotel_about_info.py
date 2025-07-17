from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.time_info import TimeInfo
from dataforseo_client.models.hotel_amenity_info import HotelAmenityInfo
from dataforseo_client.models.hotel_amenity_item_info import HotelAmenityItemInfo



class HotelAboutInfo(BaseModel):
    """
    HotelAboutInfo
    """ # noqa: E501
    description: Optional[StrictStr] = Field(default=None, description="description of the hotel. the description of the hotel entity for which the results are collected")
    sub_descriptions: Optional[List[Optional[StrictStr]]] = Field(default=None, description="additional description of the hotel. details about the hotel provided in addition to the description")
    check_in_time: Optional[TimeInfo] = Field(default=None, description="hotel check-in time. check-in time indicated in the hotel listing")
    check_out_time: Optional[TimeInfo] = Field(default=None, description="hotel check-out time. check-out time indicated in the hotel listing")
    full_address: Optional[StrictStr] = Field(default=None, description="full address of the hotel. address of the hotel indicated in the standardised format")
    domain: Optional[StrictStr] = Field(default=None, description="hotel domain. domain of the hotel’s website")
    url: Optional[StrictStr] = Field(default=None, description="hotel url. URL to the hotel’s website indicated in the listing")
    amenities: Optional[List[Optional[HotelAmenityInfo]]] = Field(default=None, description="hotel amenities. information about hotel amenities")
    popular_amenities: Optional[List[Optional[HotelAmenityItemInfo]]] = Field(default=None, description="hotel amenities. information about hotel amenities labelled as “popular”")
    __properties: ClassVar[List[str]] = [
        "description", 
        "sub_descriptions", 
        "check_in_time", 
        "check_out_time", 
        "full_address", 
        "domain", 
        "url", 
        "amenities", 
        "popular_amenities", 
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

        _dict['description'] = self.description
        _dict['sub_descriptions'] = self.sub_descriptions
        _dict['check_in_time'] = self.check_in_time.to_dict() if self.check_in_time else None
        _dict['check_out_time'] = self.check_out_time.to_dict() if self.check_out_time else None
        _dict['full_address'] = self.full_address
        _dict['domain'] = self.domain
        _dict['url'] = self.url
        amenities_items = []
        if self.amenities:
            for _item in self.amenities:
                if _item:
                    amenities_items.append(_item.to_dict())
            _dict['amenities'] = amenities_items
        popular_amenities_items = []
        if self.popular_amenities:
            for _item in self.popular_amenities:
                if _item:
                    popular_amenities_items.append(_item.to_dict())
            _dict['popular_amenities'] = popular_amenities_items
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "description": obj.get("description"),
            "sub_descriptions": obj.get("sub_descriptions"),
            "check_in_time": TimeInfo.from_dict(obj["check_in_time"]) if obj.get("check_in_time") is not None else None,
            "check_out_time": TimeInfo.from_dict(obj["check_out_time"]) if obj.get("check_out_time") is not None else None,
            "full_address": obj.get("full_address"),
            "domain": obj.get("domain"),
            "url": obj.get("url"),
            "amenities": [HotelAmenityInfo.from_dict(_item) for _item in obj["amenities"]] if obj.get("amenities") is not None else None,
            "popular_amenities": [HotelAmenityItemInfo.from_dict(_item) for _item in obj["popular_amenities"]] if obj.get("popular_amenities") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj