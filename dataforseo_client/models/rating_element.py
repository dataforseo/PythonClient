# coding: utf-8

"""
    DataForSEO API documentation

    DataForSEO API is the starting point on your journey towards building powerful SEO software. With DataForSEO you can get all the data you need to build an efficient application while also saving your time and budget. DataForSEO API is using the REST technology for interchanging data between your application and our service. The data exchange is made through the widely used HTTP protocol, which allows applying our API to almost all programming languages.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class RatingElement(BaseModel):
    """
    RatingElement
    """ # noqa: E501
    rating_type: Optional[StrictStr] = Field(default=None, description="the type of rating here you can find the following elements: Max5, Percents, CustomMax")
    value: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="the value of the rating")
    votes_count: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="the amount of feedbac")
    rating_max: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="the maximum value for a rating_type")
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    position: Optional[StrictStr] = Field(default=None, description="the alignment of the element in Google Shopping SERP possible values: left, right")
    __properties: ClassVar[List[str]] = ["rating_type", "value", "votes_count", "rating_max", "type", "position"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of RatingElement from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if rating_type (nullable) is None
        # and model_fields_set contains the field
        if self.rating_type is None and "rating_type" in self.model_fields_set:
            _dict['rating_type'] = None

        # set to None if value (nullable) is None
        # and model_fields_set contains the field
        if self.value is None and "value" in self.model_fields_set:
            _dict['value'] = None

        # set to None if votes_count (nullable) is None
        # and model_fields_set contains the field
        if self.votes_count is None and "votes_count" in self.model_fields_set:
            _dict['votes_count'] = None

        # set to None if rating_max (nullable) is None
        # and model_fields_set contains the field
        if self.rating_max is None and "rating_max" in self.model_fields_set:
            _dict['rating_max'] = None

        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        # set to None if position (nullable) is None
        # and model_fields_set contains the field
        if self.position is None and "position" in self.model_fields_set:
            _dict['position'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RatingElement from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "rating_type": obj.get("rating_type"),
            "value": obj.get("value"),
            "votes_count": obj.get("votes_count"),
            "rating_max": obj.get("rating_max"),
            "type": obj.get("type"),
            "position": obj.get("position")
        })
        return _obj


