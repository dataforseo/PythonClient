from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.location_chain import LocationChain



class HotelLocationInfo(BaseModel):
    """
    HotelLocationInfo
    """ # noqa: E501
    neighborhood: Optional[StrictStr] = Field(default=None, description="name of the neighborhood where the hotel is located")
    neighborhood_description: Optional[StrictStr] = Field(default=None, description="description of the neighborhood where the hotel is located")
    maps_url: Optional[StrictStr] = Field(default=None, description="url to the location of the hotel in google maps")
    overall_score: Optional[StrictFloat] = Field(default=None, description="overall score of the hotel location. indicates the overall score of the hotel’s location in the range from 1 to 5;. calculated based on data from the hotel’s proximity to nearby things to do and restaurants, transportation, and airports;. note that the criteria are not weighted equally in the overall score")
    score_by_categories: Optional[Dict[str, Optional[StrictFloat]]] = Field(default=None, description="category scores of the hotel location. the scores of the hotel’s location tied to the categories that indicate the proximity to nearby things to do, restaurants, transportation, and airports;")
    latitude: Optional[StrictFloat] = Field(default=None, description="hotel latitude. latitude coordinates of the hotel’s location. example:. 39.4806397")
    longitude: Optional[StrictFloat] = Field(default=None, description="hotel longitude. latitude coordinates of the hotel’s location. example:. -106.0512973")
    location_chain: Optional[List[Optional[LocationChain]]] = Field(default=None, description="elements of the location chain. additional parameters of each element of the location chain")
    __properties: ClassVar[List[str]] = [
        "neighborhood", 
        "neighborhood_description", 
        "maps_url", 
        "overall_score", 
        "score_by_categories", 
        "latitude", 
        "longitude", 
        "location_chain", 
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

        _dict['neighborhood'] = self.neighborhood
        _dict['neighborhood_description'] = self.neighborhood_description
        _dict['maps_url'] = self.maps_url
        _dict['overall_score'] = self.overall_score
        _dict['score_by_categories'] = self.score_by_categories
        _dict['latitude'] = self.latitude
        _dict['longitude'] = self.longitude
        location_chain_items = []
        if self.location_chain:
            for _item in self.location_chain:
                if _item:
                    location_chain_items.append(_item.to_dict())
            _dict['location_chain'] = location_chain_items
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "neighborhood": obj.get("neighborhood"),
            "neighborhood_description": obj.get("neighborhood_description"),
            "maps_url": obj.get("maps_url"),
            "overall_score": obj.get("overall_score"),
            "score_by_categories": obj.get("score_by_categories"),
            "latitude": obj.get("latitude"),
            "longitude": obj.get("longitude"),
            "location_chain": [LocationChain.from_dict(_item) for _item in obj["location_chain"]] if obj.get("location_chain") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj