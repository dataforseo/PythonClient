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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from dataforseo_client.models.html_item import HtmlItem
from typing import Optional, Set
from typing_extensions import Self

class SerpGoogleFinanceMarketsLiveHtmlResultInfo(BaseModel):
    """
    SerpGoogleFinanceMarketsLiveHtmlResultInfo
    """ # noqa: E501
    keyword: Optional[StrictStr] = Field(default=None, description="keyword received in a POST array keyword is returned with decoded %## (plus character ‘+’ will be decoded to a space character)")
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    se_domain: Optional[StrictStr] = Field(default=None, description="search engine domain in a POST array")
    location_code: Optional[StrictInt] = Field(default=None, description="location code in a POST array")
    language_code: Optional[StrictStr] = Field(default=None, description="language code in a POST array")
    datetime: Optional[StrictStr] = Field(default=None, description="date and time when the result was received in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00")
    items_count: Optional[StrictInt] = Field(default=None, description="the number of results returned in the items array")
    items: Optional[List[HtmlItem]] = Field(default=None, description="elements of search results found in SERP")
    __properties: ClassVar[List[str]] = ["keyword", "type", "se_domain", "location_code", "language_code", "datetime", "items_count", "items"]

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
        """Create an instance of SerpGoogleFinanceMarketsLiveHtmlResultInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in items (list)
        _items = []
        if self.items:
            for _item_items in self.items:
                if _item_items:
                    _items.append(_item_items.to_dict())
            _dict['items'] = _items
        # set to None if keyword (nullable) is None
        # and model_fields_set contains the field
        if self.keyword is None and "keyword" in self.model_fields_set:
            _dict['keyword'] = None

        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        # set to None if se_domain (nullable) is None
        # and model_fields_set contains the field
        if self.se_domain is None and "se_domain" in self.model_fields_set:
            _dict['se_domain'] = None

        # set to None if location_code (nullable) is None
        # and model_fields_set contains the field
        if self.location_code is None and "location_code" in self.model_fields_set:
            _dict['location_code'] = None

        # set to None if language_code (nullable) is None
        # and model_fields_set contains the field
        if self.language_code is None and "language_code" in self.model_fields_set:
            _dict['language_code'] = None

        # set to None if datetime (nullable) is None
        # and model_fields_set contains the field
        if self.datetime is None and "datetime" in self.model_fields_set:
            _dict['datetime'] = None

        # set to None if items_count (nullable) is None
        # and model_fields_set contains the field
        if self.items_count is None and "items_count" in self.model_fields_set:
            _dict['items_count'] = None

        # set to None if items (nullable) is None
        # and model_fields_set contains the field
        if self.items is None and "items" in self.model_fields_set:
            _dict['items'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SerpGoogleFinanceMarketsLiveHtmlResultInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "keyword": obj.get("keyword"),
            "type": obj.get("type"),
            "se_domain": obj.get("se_domain"),
            "location_code": obj.get("location_code"),
            "language_code": obj.get("language_code"),
            "datetime": obj.get("datetime"),
            "items_count": obj.get("items_count"),
            "items": [HtmlItem.from_dict(_item) for _item in obj["items"]] if obj.get("items") is not None else None
        })
        return _obj


