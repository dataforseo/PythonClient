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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class Rectangle(BaseModel):
    """
    Rectangle
    """ # noqa: E501
    x: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="x-axis coordinate x-axis coordinate of the top-left corner of the result’s snippet, where top-left corner of the screen is the origin")
    y: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="y-axis coordinate y-axis coordinate of the top-left corner of the result’s snippet, where top-left corner of the screen is the origin")
    width: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="width of the element in pixels")
    height: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="height of the element in pixels")
    __properties: ClassVar[List[str]] = ["x", "y", "width", "height"]

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
        """Create an instance of Rectangle from a JSON string"""
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
        # set to None if x (nullable) is None
        # and model_fields_set contains the field
        if self.x is None and "x" in self.model_fields_set:
            _dict['x'] = None

        # set to None if y (nullable) is None
        # and model_fields_set contains the field
        if self.y is None and "y" in self.model_fields_set:
            _dict['y'] = None

        # set to None if width (nullable) is None
        # and model_fields_set contains the field
        if self.width is None and "width" in self.model_fields_set:
            _dict['width'] = None

        # set to None if height (nullable) is None
        # and model_fields_set contains the field
        if self.height is None and "height" in self.model_fields_set:
            _dict['height'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Rectangle from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "x": obj.get("x"),
            "y": obj.get("y"),
            "width": obj.get("width"),
            "height": obj.get("height")
        })
        return _obj


