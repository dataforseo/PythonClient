from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class HtmlContentInfo(BaseModel):
    """
    HtmlContentInfo
    """ # noqa: E501
    plain_text_size: Optional[StrictInt] = Field(default=None, description="total size of the text on the page measured in bytes")
    plain_text_rate: Optional[StrictFloat] = Field(default=None, description="plaintext rate value. plain_text_size to size ratio")
    plain_text_word_count: Optional[StrictInt] = Field(default=None, description="number of words on the page")
    automated_readability_index: Optional[StrictFloat] = Field(default=None, description="Automated Readability Index")
    coleman_liau_readability_index: Optional[StrictFloat] = Field(default=None, description="Coleman–Liau Index")
    dale_chall_readability_index: Optional[StrictFloat] = Field(default=None, description="Dale–Chall Readability Index")
    flesch_kincaid_readability_index: Optional[StrictFloat] = Field(default=None, description="Flesch–Kincaid Readability Index")
    smog_readability_index: Optional[StrictFloat] = Field(default=None, description="SMOG Readability Index")
    description_to_content_consistency: Optional[StrictFloat] = Field(default=None, description="consistency of the meta description tag with the page content. measured from 0 to 1")
    title_to_content_consistency: Optional[StrictFloat] = Field(default=None, description="consistency of the meta title tag with the page content. measured from 0 to 1")
    meta_keywords_to_content_consistency: Optional[StrictFloat] = Field(default=None, description="consistency of meta keywordstag with the page content. measured from 0 to 1")
    __properties: ClassVar[List[str]] = [
        "plain_text_size", 
        "plain_text_rate", 
        "plain_text_word_count", 
        "automated_readability_index", 
        "coleman_liau_readability_index", 
        "dale_chall_readability_index", 
        "flesch_kincaid_readability_index", 
        "smog_readability_index", 
        "description_to_content_consistency", 
        "title_to_content_consistency", 
        "meta_keywords_to_content_consistency", 
        ]

    additional_properties: Dict[str, Any] = Field(default_factory=dict)

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )

    def to_str(self) -> str:
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        excluded_fields: Set[str] = set([
        ])

        _dict = {}

        _dict['plain_text_size'] = self.plain_text_size
        _dict['plain_text_rate'] = self.plain_text_rate
        _dict['plain_text_word_count'] = self.plain_text_word_count
        _dict['automated_readability_index'] = self.automated_readability_index
        _dict['coleman_liau_readability_index'] = self.coleman_liau_readability_index
        _dict['dale_chall_readability_index'] = self.dale_chall_readability_index
        _dict['flesch_kincaid_readability_index'] = self.flesch_kincaid_readability_index
        _dict['smog_readability_index'] = self.smog_readability_index
        _dict['description_to_content_consistency'] = self.description_to_content_consistency
        _dict['title_to_content_consistency'] = self.title_to_content_consistency
        _dict['meta_keywords_to_content_consistency'] = self.meta_keywords_to_content_consistency
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "plain_text_size": obj.get("plain_text_size"),
            "plain_text_rate": obj.get("plain_text_rate"),
            "plain_text_word_count": obj.get("plain_text_word_count"),
            "automated_readability_index": obj.get("automated_readability_index"),
            "coleman_liau_readability_index": obj.get("coleman_liau_readability_index"),
            "dale_chall_readability_index": obj.get("dale_chall_readability_index"),
            "flesch_kincaid_readability_index": obj.get("flesch_kincaid_readability_index"),
            "smog_readability_index": obj.get("smog_readability_index"),
            "description_to_content_consistency": obj.get("description_to_content_consistency"),
            "title_to_content_consistency": obj.get("title_to_content_consistency"),
            "meta_keywords_to_content_consistency": obj.get("meta_keywords_to_content_consistency"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj