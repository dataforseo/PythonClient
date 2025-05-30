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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class StoresCountInfo(BaseModel):
    """
    StoresCountInfo
    """ # noqa: E501
    count: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="number of stores that offer the product")
    displayed_text: Optional[StrictStr] = Field(default=None, description="text displayed on the Google Shopping page")
    count_from_text: Optional[StrictBool] = Field(default=None, description="whether the number of stores is taken from text indicates whether the number of stores is taken from displayed_text; if the API finds the exact number of stores in the HTML code of the Google Shopping page, this parameter is false; if the API cannot find the number of stores in the HTML code of the page, it takes the number from the displayed_text; in this case, the parameter is true")
    __properties: ClassVar[List[str]] = ["count", "displayed_text", "count_from_text"]

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
        """Create an instance of StoresCountInfo from a JSON string"""
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
        # set to None if count (nullable) is None
        # and model_fields_set contains the field
        if self.count is None and "count" in self.model_fields_set:
            _dict['count'] = None

        # set to None if displayed_text (nullable) is None
        # and model_fields_set contains the field
        if self.displayed_text is None and "displayed_text" in self.model_fields_set:
            _dict['displayed_text'] = None

        # set to None if count_from_text (nullable) is None
        # and model_fields_set contains the field
        if self.count_from_text is None and "count_from_text" in self.model_fields_set:
            _dict['count_from_text'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of StoresCountInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "count": obj.get("count"),
            "displayed_text": obj.get("displayed_text"),
            "count_from_text": obj.get("count_from_text")
        })
        return _obj


