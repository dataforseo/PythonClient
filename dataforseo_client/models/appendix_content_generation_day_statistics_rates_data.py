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

from pydantic import BaseModel, ConfigDict, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Optional, Union
from dataforseo_client.models.appendix_content_generation_day_limits_rates_data_info import AppendixContentGenerationDayLimitsRatesDataInfo
from dataforseo_client.models.appendix_info import AppendixInfo
from typing import Optional, Set
from typing_extensions import Self

class AppendixContentGenerationDayStatisticsRatesData(BaseModel):
    """
    AppendixContentGenerationDayStatisticsRatesData
    """ # noqa: E501
    generate: Optional[AppendixInfo] = None
    generate_meta_tags: Optional[AppendixInfo] = None
    generate_text: Optional[AppendixInfo] = None
    paraphrase: Optional[AppendixInfo] = None
    check_grammar: Optional[AppendixContentGenerationDayLimitsRatesDataInfo] = None
    text_summary: Optional[AppendixContentGenerationDayLimitsRatesDataInfo] = None
    generate_sub_topics: Optional[AppendixInfo] = None
    grammar_rules: Optional[Union[StrictFloat, StrictInt]] = None
    __properties: ClassVar[List[str]] = ["generate", "generate_meta_tags", "generate_text", "paraphrase", "check_grammar", "text_summary", "generate_sub_topics", "grammar_rules"]

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
        """Create an instance of AppendixContentGenerationDayStatisticsRatesData from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of generate
        if self.generate:
            _dict['generate'] = self.generate.to_dict()
        # override the default output from pydantic by calling `to_dict()` of generate_meta_tags
        if self.generate_meta_tags:
            _dict['generate_meta_tags'] = self.generate_meta_tags.to_dict()
        # override the default output from pydantic by calling `to_dict()` of generate_text
        if self.generate_text:
            _dict['generate_text'] = self.generate_text.to_dict()
        # override the default output from pydantic by calling `to_dict()` of paraphrase
        if self.paraphrase:
            _dict['paraphrase'] = self.paraphrase.to_dict()
        # override the default output from pydantic by calling `to_dict()` of check_grammar
        if self.check_grammar:
            _dict['check_grammar'] = self.check_grammar.to_dict()
        # override the default output from pydantic by calling `to_dict()` of text_summary
        if self.text_summary:
            _dict['text_summary'] = self.text_summary.to_dict()
        # override the default output from pydantic by calling `to_dict()` of generate_sub_topics
        if self.generate_sub_topics:
            _dict['generate_sub_topics'] = self.generate_sub_topics.to_dict()
        # set to None if grammar_rules (nullable) is None
        # and model_fields_set contains the field
        if self.grammar_rules is None and "grammar_rules" in self.model_fields_set:
            _dict['grammar_rules'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AppendixContentGenerationDayStatisticsRatesData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "generate": AppendixInfo.from_dict(obj["generate"]) if obj.get("generate") is not None else None,
            "generate_meta_tags": AppendixInfo.from_dict(obj["generate_meta_tags"]) if obj.get("generate_meta_tags") is not None else None,
            "generate_text": AppendixInfo.from_dict(obj["generate_text"]) if obj.get("generate_text") is not None else None,
            "paraphrase": AppendixInfo.from_dict(obj["paraphrase"]) if obj.get("paraphrase") is not None else None,
            "check_grammar": AppendixContentGenerationDayLimitsRatesDataInfo.from_dict(obj["check_grammar"]) if obj.get("check_grammar") is not None else None,
            "text_summary": AppendixContentGenerationDayLimitsRatesDataInfo.from_dict(obj["text_summary"]) if obj.get("text_summary") is not None else None,
            "generate_sub_topics": AppendixInfo.from_dict(obj["generate_sub_topics"]) if obj.get("generate_sub_topics") is not None else None,
            "grammar_rules": obj.get("grammar_rules")
        })
        return _obj


