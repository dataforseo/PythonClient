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

from pydantic import BaseModel, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from dataforseo_client.models.content_url_info import ContentUrlInfo
from typing import Optional, Set
from typing_extensions import Self

class RowCellInfo(BaseModel):
    """
    RowCellInfo
    """ # noqa: E501
    text: Optional[StrictStr] = Field(default=None, description="content text")
    urls: Optional[List[ContentUrlInfo]] = Field(default=None, description="contains other URLs and anchors found in the content element")
    is_header: Optional[StrictBool] = Field(default=None, description="indicates if the text belongs to the header")
    __properties: ClassVar[List[str]] = ["text", "urls", "is_header"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of RowCellInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in urls (list)
        _items = []
        if self.urls:
            for _item in self.urls:
                if _item:
                    _items.append(_item.to_dict())
            _dict['urls'] = _items
        # set to None if text (nullable) is None
        # and model_fields_set contains the field
        if self.text is None and "text" in self.model_fields_set:
            _dict['text'] = None

        # set to None if urls (nullable) is None
        # and model_fields_set contains the field
        if self.urls is None and "urls" in self.model_fields_set:
            _dict['urls'] = None

        # set to None if is_header (nullable) is None
        # and model_fields_set contains the field
        if self.is_header is None and "is_header" in self.model_fields_set:
            _dict['is_header'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RowCellInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "text": obj.get("text"),
            "urls": [ContentUrlInfo.from_dict(_item) for _item in obj["urls"]] if obj.get("urls") is not None else None,
            "is_header": obj.get("is_header")
        })
        return _obj

