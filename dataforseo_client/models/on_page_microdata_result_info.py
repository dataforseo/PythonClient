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

from pydantic import BaseModel, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from dataforseo_client.models.crawl_status_info import CrawlStatusInfo
from dataforseo_client.models.on_page_microdata_item import OnPageMicrodataItem
from dataforseo_client.models.test_summary import TestSummary
from typing import Optional, Set
from typing_extensions import Self

class OnPageMicrodataResultInfo(BaseModel):
    """
    OnPageMicrodataResultInfo
    """ # noqa: E501
    crawl_progress: Optional[StrictStr] = Field(default=None, description="status of the crawling session possible values: in_progress, finished")
    crawl_status: Optional[CrawlStatusInfo] = None
    test_summary: Optional[TestSummary] = None
    items_count: Optional[StrictInt] = Field(default=None, description="number of items in the results array")
    items: Optional[List[OnPageMicrodataItem]] = Field(default=None, description="items array")
    __properties: ClassVar[List[str]] = ["crawl_progress", "crawl_status", "test_summary", "items_count", "items"]

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
        """Create an instance of OnPageMicrodataResultInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of crawl_status
        if self.crawl_status:
            _dict['crawl_status'] = self.crawl_status.to_dict()
        # override the default output from pydantic by calling `to_dict()` of test_summary
        if self.test_summary:
            _dict['test_summary'] = self.test_summary.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in items (list)
        _items = []
        if self.items:
            for _item in self.items:
                if _item:
                    _items.append(_item.to_dict())
            _dict['items'] = _items
        # set to None if crawl_progress (nullable) is None
        # and model_fields_set contains the field
        if self.crawl_progress is None and "crawl_progress" in self.model_fields_set:
            _dict['crawl_progress'] = None

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
        """Create an instance of OnPageMicrodataResultInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "crawl_progress": obj.get("crawl_progress"),
            "crawl_status": CrawlStatusInfo.from_dict(obj["crawl_status"]) if obj.get("crawl_status") is not None else None,
            "test_summary": TestSummary.from_dict(obj["test_summary"]) if obj.get("test_summary") is not None else None,
            "items_count": obj.get("items_count"),
            "items": [OnPageMicrodataItem.from_dict(_item) for _item in obj["items"]] if obj.get("items") is not None else None
        })
        return _obj


