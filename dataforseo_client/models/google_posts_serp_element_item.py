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

from pydantic import ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from dataforseo_client.models.base_serp_element_item import BaseSerpElementItem
from dataforseo_client.models.rectangle import Rectangle
from typing import Optional, Set
from typing_extensions import Self

class GooglePostsSerpElementItem(BaseSerpElementItem):
    """
    GooglePostsSerpElementItem
    """ # noqa: E501
    position: Optional[StrictStr] = Field(default=None, description="the alignment of the element in SERP can take the following values: left, right")
    xpath: Optional[StrictStr] = Field(default=None, description="the XPath of the element")
    posts_id: Optional[StrictStr] = Field(default=None, description="the identifier of the google_posts feature")
    feature: Optional[StrictStr] = Field(default=None, description="the additional feature of the review")
    cid: Optional[StrictStr] = Field(default=None, description="google-defined client id")
    rectangle: Optional[Rectangle] = None
    __properties: ClassVar[List[str]] = ["type", "rank_group", "rank_absolute", "position", "xpath", "posts_id", "feature", "cid", "rectangle"]

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
        """Create an instance of GooglePostsSerpElementItem from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of rectangle
        if self.rectangle:
            _dict['rectangle'] = self.rectangle.to_dict()
        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        # set to None if rank_group (nullable) is None
        # and model_fields_set contains the field
        if self.rank_group is None and "rank_group" in self.model_fields_set:
            _dict['rank_group'] = None

        # set to None if rank_absolute (nullable) is None
        # and model_fields_set contains the field
        if self.rank_absolute is None and "rank_absolute" in self.model_fields_set:
            _dict['rank_absolute'] = None

        # set to None if position (nullable) is None
        # and model_fields_set contains the field
        if self.position is None and "position" in self.model_fields_set:
            _dict['position'] = None

        # set to None if xpath (nullable) is None
        # and model_fields_set contains the field
        if self.xpath is None and "xpath" in self.model_fields_set:
            _dict['xpath'] = None

        # set to None if posts_id (nullable) is None
        # and model_fields_set contains the field
        if self.posts_id is None and "posts_id" in self.model_fields_set:
            _dict['posts_id'] = None

        # set to None if feature (nullable) is None
        # and model_fields_set contains the field
        if self.feature is None and "feature" in self.model_fields_set:
            _dict['feature'] = None

        # set to None if cid (nullable) is None
        # and model_fields_set contains the field
        if self.cid is None and "cid" in self.model_fields_set:
            _dict['cid'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GooglePostsSerpElementItem from a dict"""
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
            "posts_id": obj.get("posts_id"),
            "feature": obj.get("feature"),
            "cid": obj.get("cid"),
            "rectangle": Rectangle.from_dict(obj["rectangle"]) if obj.get("rectangle") is not None else None
        })
        return _obj


