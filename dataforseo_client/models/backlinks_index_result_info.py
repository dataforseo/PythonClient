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

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from dataforseo_client.models.index_history import IndexHistory
from typing import Optional, Set
from typing_extensions import Self

class BacklinksIndexResultInfo(BaseModel):
    """
    BacklinksIndexResultInfo
    """ # noqa: E501
    total_backlinks: Optional[StrictInt] = Field(default=None, description="total number of backlinks our database contains for the moment of checking")
    total_pages: Optional[StrictInt] = Field(default=None, description="total number of pages our database contains for the moment of checking")
    total_domains: Optional[StrictInt] = Field(default=None, description="total number of domains our database contains for the moment of checking")
    index_history: Optional[List[IndexHistory]] = Field(default=None, description="index volume data for the past 12 months")
    __properties: ClassVar[List[str]] = ["total_backlinks", "total_pages", "total_domains", "index_history"]

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
        """Create an instance of BacklinksIndexResultInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in index_history (list)
        _items = []
        if self.index_history:
            for _item_index_history in self.index_history:
                if _item_index_history:
                    _items.append(_item_index_history.to_dict())
            _dict['index_history'] = _items
        # set to None if total_backlinks (nullable) is None
        # and model_fields_set contains the field
        if self.total_backlinks is None and "total_backlinks" in self.model_fields_set:
            _dict['total_backlinks'] = None

        # set to None if total_pages (nullable) is None
        # and model_fields_set contains the field
        if self.total_pages is None and "total_pages" in self.model_fields_set:
            _dict['total_pages'] = None

        # set to None if total_domains (nullable) is None
        # and model_fields_set contains the field
        if self.total_domains is None and "total_domains" in self.model_fields_set:
            _dict['total_domains'] = None

        # set to None if index_history (nullable) is None
        # and model_fields_set contains the field
        if self.index_history is None and "index_history" in self.model_fields_set:
            _dict['index_history'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BacklinksIndexResultInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "total_backlinks": obj.get("total_backlinks"),
            "total_pages": obj.get("total_pages"),
            "total_domains": obj.get("total_domains"),
            "index_history": [IndexHistory.from_dict(_item) for _item in obj["index_history"]] if obj.get("index_history") is not None else None
        })
        return _obj


