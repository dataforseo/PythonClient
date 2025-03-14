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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from dataforseo_client.models.keyword_intent_info import KeywordIntentInfo
from typing import Optional, Set
from typing_extensions import Self

class DataforseoLabsGoogleSearchIntentLiveItem(BaseModel):
    """
    DataforseoLabsGoogleSearchIntentLiveItem
    """ # noqa: E501
    keyword: Optional[StrictStr] = Field(default=None, description="target keyword in a POST array")
    keyword_intent: Optional[KeywordIntentInfo] = None
    secondary_keyword_intents: Optional[List[KeywordIntentInfo]] = Field(default=None, description="contains objects with other possible search intents for the specified keyword")
    __properties: ClassVar[List[str]] = ["keyword", "keyword_intent", "secondary_keyword_intents"]

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
        """Create an instance of DataforseoLabsGoogleSearchIntentLiveItem from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of keyword_intent
        if self.keyword_intent:
            _dict['keyword_intent'] = self.keyword_intent.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in secondary_keyword_intents (list)
        _items = []
        if self.secondary_keyword_intents:
            for _item_secondary_keyword_intents in self.secondary_keyword_intents:
                if _item_secondary_keyword_intents:
                    _items.append(_item_secondary_keyword_intents.to_dict())
            _dict['secondary_keyword_intents'] = _items
        # set to None if keyword (nullable) is None
        # and model_fields_set contains the field
        if self.keyword is None and "keyword" in self.model_fields_set:
            _dict['keyword'] = None

        # set to None if secondary_keyword_intents (nullable) is None
        # and model_fields_set contains the field
        if self.secondary_keyword_intents is None and "secondary_keyword_intents" in self.model_fields_set:
            _dict['secondary_keyword_intents'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DataforseoLabsGoogleSearchIntentLiveItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "keyword": obj.get("keyword"),
            "keyword_intent": KeywordIntentInfo.from_dict(obj["keyword_intent"]) if obj.get("keyword_intent") is not None else None,
            "secondary_keyword_intents": [KeywordIntentInfo.from_dict(_item) for _item in obj["secondary_keyword_intents"]] if obj.get("secondary_keyword_intents") is not None else None
        })
        return _obj


