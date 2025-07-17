from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.rating_element import RatingElement



class PeopleAlsoSearch(BaseModel):
    """
    PeopleAlsoSearch
    """ # noqa: E501
    cid: Optional[StrictStr] = Field(default=None, description="google-defined client id. unique id of a local establishment. learn more about the identifier in this help center article")
    feature_id: Optional[StrictStr] = Field(default=None, description="the unique identifier of the element in SERP. learn more about the identifier in this help center article")
    title: Optional[StrictStr] = Field(default=None, description="title of the element in SERP. the name of the business entity for which the results are collected")
    rating: Optional[RatingElement] = Field(default=None, description="the element’s rating . the popularity rate based on reviews and displayed in SERP")
    __properties: ClassVar[List[str]] = [
        "cid", 
        "feature_id", 
        "title", 
        "rating", 
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

        _dict['cid'] = self.cid
        _dict['feature_id'] = self.feature_id
        _dict['title'] = self.title
        _dict['rating'] = self.rating.to_dict() if self.rating else None
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "cid": obj.get("cid"),
            "feature_id": obj.get("feature_id"),
            "title": obj.get("title"),
            "rating": RatingElement.from_dict(obj["rating"]) if obj.get("rating") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj