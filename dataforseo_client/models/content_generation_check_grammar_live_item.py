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
from typing import Optional, Set
from typing_extensions import Self

class ContentGenerationCheckGrammarLiveItem(BaseModel):
    """
    ContentGenerationCheckGrammarLiveItem
    """ # noqa: E501
    message: Optional[StrictStr] = Field(default=None, description="message of the grammar or spelling error")
    description: Optional[StrictStr] = Field(default=None, description="description of the grammar or spelling error")
    suggestions: Optional[List[Optional[StrictStr]]] = Field(default=None, description="suggested corrections")
    offset: Optional[StrictInt] = Field(default=None, description="offset token for subsequent requests")
    length: Optional[StrictInt] = Field(default=None, description="offset token for subsequent requests")
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    rule_id: Optional[StrictStr] = Field(default=None, description="id of the grammar or spelling rule see the List of Grammar Rules for Content Generation API")
    rule_description: Optional[StrictStr] = Field(default=None, description="description of the grammar or spelling rule")
    rule_issue_type: Optional[StrictStr] = Field(default=None, description="type of the issue found by the relevant rule")
    rule_category_id: Optional[StrictStr] = Field(default=None, description="id of the rule category")
    rule_category_name: Optional[StrictStr] = Field(default=None, description="name of the rule category")
    __properties: ClassVar[List[str]] = ["message", "description", "suggestions", "offset", "length", "type", "rule_id", "rule_description", "rule_issue_type", "rule_category_id", "rule_category_name"]

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
        """Create an instance of ContentGenerationCheckGrammarLiveItem from a JSON string"""
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
        # set to None if message (nullable) is None
        # and model_fields_set contains the field
        if self.message is None and "message" in self.model_fields_set:
            _dict['message'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if suggestions (nullable) is None
        # and model_fields_set contains the field
        if self.suggestions is None and "suggestions" in self.model_fields_set:
            _dict['suggestions'] = None

        # set to None if offset (nullable) is None
        # and model_fields_set contains the field
        if self.offset is None and "offset" in self.model_fields_set:
            _dict['offset'] = None

        # set to None if length (nullable) is None
        # and model_fields_set contains the field
        if self.length is None and "length" in self.model_fields_set:
            _dict['length'] = None

        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        # set to None if rule_id (nullable) is None
        # and model_fields_set contains the field
        if self.rule_id is None and "rule_id" in self.model_fields_set:
            _dict['rule_id'] = None

        # set to None if rule_description (nullable) is None
        # and model_fields_set contains the field
        if self.rule_description is None and "rule_description" in self.model_fields_set:
            _dict['rule_description'] = None

        # set to None if rule_issue_type (nullable) is None
        # and model_fields_set contains the field
        if self.rule_issue_type is None and "rule_issue_type" in self.model_fields_set:
            _dict['rule_issue_type'] = None

        # set to None if rule_category_id (nullable) is None
        # and model_fields_set contains the field
        if self.rule_category_id is None and "rule_category_id" in self.model_fields_set:
            _dict['rule_category_id'] = None

        # set to None if rule_category_name (nullable) is None
        # and model_fields_set contains the field
        if self.rule_category_name is None and "rule_category_name" in self.model_fields_set:
            _dict['rule_category_name'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ContentGenerationCheckGrammarLiveItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "message": obj.get("message"),
            "description": obj.get("description"),
            "suggestions": obj.get("suggestions"),
            "offset": obj.get("offset"),
            "length": obj.get("length"),
            "type": obj.get("type"),
            "rule_id": obj.get("rule_id"),
            "rule_description": obj.get("rule_description"),
            "rule_issue_type": obj.get("rule_issue_type"),
            "rule_category_id": obj.get("rule_category_id"),
            "rule_category_name": obj.get("rule_category_name")
        })
        return _obj


