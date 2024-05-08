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
from typing import Optional, Set
from typing_extensions import Self

class ItemsWithoutAnswers(BaseModel):
    """
    ItemsWithoutAnswers
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    rank_group: Optional[StrictInt] = Field(default=None, description="position within a group of elements with identical type values positions of elements with different type values are omitted from rank_group")
    rank_absolute: Optional[StrictInt] = Field(default=None, description="absolute rank among all the elements")
    question_id: Optional[StrictStr] = Field(default=None, description="ID of the question")
    url: Optional[StrictStr] = Field(default=None, description="URL of the question")
    profile_image_url: Optional[StrictStr] = Field(default=None, description="URL of the user’s profile image")
    profile_url: Optional[StrictStr] = Field(default=None, description="URL of the user’s profile")
    profile_name: Optional[StrictStr] = Field(default=None, description="displayed name of the user")
    question_text: Optional[StrictStr] = Field(default=None, description="current text of the question")
    original_question_text: Optional[StrictStr] = Field(default=None, description="original text of the question")
    time_ago: Optional[StrictStr] = Field(default=None, description="estimated time when the question was posted")
    timestamp: Optional[StrictStr] = Field(default=None, description="exact time when the question was posted")
    items: Optional[Dict[str, Any]] = Field(default=None, description="array of items items within google_business_question_item")
    __properties: ClassVar[List[str]] = ["type", "rank_group", "rank_absolute", "question_id", "url", "profile_image_url", "profile_url", "profile_name", "question_text", "original_question_text", "time_ago", "timestamp", "items"]

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
        """Create an instance of ItemsWithoutAnswers from a JSON string"""
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

        # set to None if question_id (nullable) is None
        # and model_fields_set contains the field
        if self.question_id is None and "question_id" in self.model_fields_set:
            _dict['question_id'] = None

        # set to None if url (nullable) is None
        # and model_fields_set contains the field
        if self.url is None and "url" in self.model_fields_set:
            _dict['url'] = None

        # set to None if profile_image_url (nullable) is None
        # and model_fields_set contains the field
        if self.profile_image_url is None and "profile_image_url" in self.model_fields_set:
            _dict['profile_image_url'] = None

        # set to None if profile_url (nullable) is None
        # and model_fields_set contains the field
        if self.profile_url is None and "profile_url" in self.model_fields_set:
            _dict['profile_url'] = None

        # set to None if profile_name (nullable) is None
        # and model_fields_set contains the field
        if self.profile_name is None and "profile_name" in self.model_fields_set:
            _dict['profile_name'] = None

        # set to None if question_text (nullable) is None
        # and model_fields_set contains the field
        if self.question_text is None and "question_text" in self.model_fields_set:
            _dict['question_text'] = None

        # set to None if original_question_text (nullable) is None
        # and model_fields_set contains the field
        if self.original_question_text is None and "original_question_text" in self.model_fields_set:
            _dict['original_question_text'] = None

        # set to None if time_ago (nullable) is None
        # and model_fields_set contains the field
        if self.time_ago is None and "time_ago" in self.model_fields_set:
            _dict['time_ago'] = None

        # set to None if timestamp (nullable) is None
        # and model_fields_set contains the field
        if self.timestamp is None and "timestamp" in self.model_fields_set:
            _dict['timestamp'] = None

        # set to None if items (nullable) is None
        # and model_fields_set contains the field
        if self.items is None and "items" in self.model_fields_set:
            _dict['items'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ItemsWithoutAnswers from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "rank_group": obj.get("rank_group"),
            "rank_absolute": obj.get("rank_absolute"),
            "question_id": obj.get("question_id"),
            "url": obj.get("url"),
            "profile_image_url": obj.get("profile_image_url"),
            "profile_url": obj.get("profile_url"),
            "profile_name": obj.get("profile_name"),
            "question_text": obj.get("question_text"),
            "original_question_text": obj.get("original_question_text"),
            "time_ago": obj.get("time_ago"),
            "timestamp": obj.get("timestamp"),
            "items": obj.get("items")
        })
        return _obj


