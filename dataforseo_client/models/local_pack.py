from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.rating_element import RatingElement



class LocalPack(BaseModel):
    """
    LocalPack
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    rank_group: Optional[StrictInt] = Field(default=None, description="group rank in SERP. position within a group of elements with identical type values. positions of elements with different type values are omitted from rank_group")
    rank_absolute: Optional[StrictInt] = Field(default=None, description="absolute rank in SERP. absolute position among all the elements in SERP")
    position: Optional[StrictStr] = Field(default=None, description="the alignment of the element in SERP. can take the following values:. left, right")
    xpath: Optional[StrictStr] = Field(default=None, description="the XPath of the element")
    title: Optional[StrictStr] = Field(default=None, description="title of the element")
    description: Optional[StrictStr] = Field(default=None, description="description of the results element in SERP")
    domain: Optional[StrictStr] = Field(default=None, description="domain in SERP")
    phone: Optional[StrictStr] = Field(default=None, description="phone number")
    url: Optional[StrictStr] = Field(default=None, description="search URL with refinement parameters")
    is_paid: Optional[StrictBool] = Field(default=None, description="indicates whether the element is an ad")
    rating: Optional[RatingElement] = Field(default=None, description="the item’s rating . the popularity rate based on reviews and displayed in SERP")
    cid: Optional[StrictStr] = Field(default=None, description="google-defined client id. unique id of a local establishment;. can be used with Google Reviews API to get a full list of reviews")
    rectangle: Optional[Any] = Field(default=None, description="rectangle parameters. contains cartesian coordinates and pixel dimensions of the result’s snippet in SERP. in this case, will equal null")
    __properties: ClassVar[List[str]] = [
        "type", 
        "rank_group", 
        "rank_absolute", 
        "position", 
        "xpath", 
        "title", 
        "description", 
        "domain", 
        "phone", 
        "url", 
        "is_paid", 
        "rating", 
        "cid", 
        "rectangle", 
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
        _dict['position'] = self.position
        _dict['xpath'] = self.xpath
        _dict['title'] = self.title
        _dict['description'] = self.description
        _dict['domain'] = self.domain
        _dict['phone'] = self.phone
        _dict['url'] = self.url
        _dict['is_paid'] = self.is_paid
        _dict['rating'] = self.rating.to_dict() if self.rating else None
        _dict['cid'] = self.cid
        _dict['rectangle'] = self.rectangle
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
            "position": obj.get("position"),
            "xpath": obj.get("xpath"),
            "title": obj.get("title"),
            "description": obj.get("description"),
            "domain": obj.get("domain"),
            "phone": obj.get("phone"),
            "url": obj.get("url"),
            "is_paid": obj.get("is_paid"),
            "rating": RatingElement.from_dict(obj["rating"]) if obj.get("rating") is not None else None,
            "cid": obj.get("cid"),
            "rectangle": obj.get("rectangle"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj