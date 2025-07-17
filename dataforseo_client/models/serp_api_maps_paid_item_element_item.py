from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.base_serp_api_google_maps_element_item import BaseSerpApiGoogleMapsElementItem
from dataforseo_client.models.rating_element import RatingElement



class SerpApiMapsPaidItemElementItem(BaseSerpApiGoogleMapsElementItem):
    """
    SerpApiMapsPaidItemElementItem
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    rank_group: Optional[StrictInt] = Field(default=None, description="group rank in SERP. position within a group of elements with identical type values. positions of elements with different type values are omitted from rank_group")
    rank_absolute: Optional[StrictInt] = Field(default=None, description="absolute rank in SERP. absolute position among all the elements in SERP")
    domain: Optional[StrictStr] = Field(default=None, description="domain in SERP")
    title: Optional[StrictStr] = Field(default=None, description="title of the element")
    url: Optional[StrictStr] = Field(default=None, description="search URL with refinement parameters")
    rating: Optional[RatingElement] = Field(default=None, description="the element’s rating . the popularity rate based on reviews and displayed in SERP")
    rating_distribution: Optional[Dict[str, Optional[StrictInt]]] = Field(default=None, description="the distribution of ratings of the business entity. the object displays the number of 1-star to 5-star ratings, as reviewed by users")
    __properties: ClassVar[List[str]] = [
        "type", 
        "rank_group", 
        "rank_absolute", 
        "domain", 
        "title", 
        "url", 
        "rating", 
        "rating_distribution", 
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
        _dict['domain'] = self.domain
        _dict['title'] = self.title
        _dict['url'] = self.url
        _dict['rating'] = self.rating.to_dict() if self.rating else None
        _dict['rating_distribution'] = self.rating_distribution
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
            "domain": obj.get("domain"),
            "title": obj.get("title"),
            "url": obj.get("url"),
            "rating": RatingElement.from_dict(obj["rating"]) if obj.get("rating") is not None else None,
            "rating_distribution": obj.get("rating_distribution"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj