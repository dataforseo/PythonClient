from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.appendix_info import AppendixInfo
from dataforseo_client.models.appendix_content_generation_day_limits_rates_data_info import AppendixContentGenerationDayLimitsRatesDataInfo



class AppendixContentGenerationLimitsRatesDataInfo(BaseModel):
    """
    AppendixContentGenerationLimitsRatesDataInfo
    """ # noqa: E501
    generate: Optional[AppendixInfo] = Field(default=None, description="")
    generate_meta_tags: Optional[AppendixInfo] = Field(default=None, description="")
    generate_text: Optional[AppendixInfo] = Field(default=None, description="")
    paraphrase: Optional[AppendixInfo] = Field(default=None, description="")
    check_grammar: Optional[AppendixContentGenerationDayLimitsRatesDataInfo] = Field(default=None, description="")
    text_summary: Optional[AppendixContentGenerationDayLimitsRatesDataInfo] = Field(default=None, description="")
    generate_sub_topics: Optional[AppendixInfo] = Field(default=None, description="")
    __properties: ClassVar[List[str]] = [
        "generate", 
        "generate_meta_tags", 
        "generate_text", 
        "paraphrase", 
        "check_grammar", 
        "text_summary", 
        "generate_sub_topics", 
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

        _dict['generate'] = self.generate.to_dict() if self.generate else None
        _dict['generate_meta_tags'] = self.generate_meta_tags.to_dict() if self.generate_meta_tags else None
        _dict['generate_text'] = self.generate_text.to_dict() if self.generate_text else None
        _dict['paraphrase'] = self.paraphrase.to_dict() if self.paraphrase else None
        _dict['check_grammar'] = self.check_grammar.to_dict() if self.check_grammar else None
        _dict['text_summary'] = self.text_summary.to_dict() if self.text_summary else None
        _dict['generate_sub_topics'] = self.generate_sub_topics.to_dict() if self.generate_sub_topics else None
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
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
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj