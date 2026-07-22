from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.base_ai_optimization_l_lm_mentions_target_element import BaseAiOptimizationLLmMentionsTargetElement



class AiOptimizationLlmMentionsHistoricalLiveRequestInfo(BaseModel):
    """
    AiOptimizationLlmMentionsHistoricalLiveRequestInfo
    """ # noqa: E501
    target: Optional[List[Optional[BaseAiOptimizationLLmMentionsTargetElement]]] = Field(default=None, description=r"array of objects containing target entities. required field. you can specify up to 10 entities (objects) in the target field. one target entity can contain either one domain or one keyword and related parameters. examples:. . target array with a domain entity")
    date_from: Optional[StrictStr] = Field(default=None, description=r"start date of the time range. optional field. minimal value 2025-08-01. date format 'yyyy-mm-dd'")
    date_to: Optional[StrictStr] = Field(default=None, description=r"end date of the time range. optional field. Note value specified in date_from cannot exceed the value in date_to. date format 'yyyy-mm-dd'")
    location_name: Optional[StrictStr] = Field(default=None, description=r"full name of search location. optional field. if you use this field, you don't need to specify location_code. if you don't specify this field, the location_code with 2840 value will be used by default;. you can receive the list of available locations of the search engine with their location_name by making a separate request to the https://api.dataforseo.com/v3/ai_optimization/llm_mentions/locations_and_languages. Note: chat_gpt data is available for United States only")
    location_code: Optional[StrictInt] = Field(default=None, description=r"search location code. optional field. if you use this field, you don't need to specify location_name. you can receive the list of available locations of the search engine with their location_code by making a separate request to the https://api.dataforseo.com/v3/ai_optimization/llm_mentions/locations_and_languages. default value: 2840. Note: chat_gpt data is available for 2840 only")
    language_name: Optional[StrictStr] = Field(default=None, description=r"full name of search language. optional field. if you use this field, you don't need to specify language_code;. if you don't specify this field, the language_code with en value will be used by default;. you can receive the list of available languages of the search engine with their language_name by making a separate request to the https://api.dataforseo.com/v3/ai_optimization/llm_mentions/locations_and_languages. Note: chat_gpt data is available for English only")
    language_code: Optional[StrictStr] = Field(default=None, description=r"search language code. optional field. if you use this field, you don't need to specify language_name;. you can receive the list of available languages of the search engine with their language_code by making a separate request to the https://api.dataforseo.com/v3/ai_optimization/llm_mentions/locations_and_languages. default value: en. Note: chat_gpt data is available for en only")
    platform: Optional[StrictStr] = Field(default=None, description=r"target platform. optional field. possible values:. chat_gpt, google. Note: if the platform is not specified, the data is returned for both platforms. Note #2:chat_gpt data is available for the United States and English only")
    tag: Optional[StrictStr] = Field(default=None, description=r"user-defined task identifier. optional field. the character limit is 255. you can use this parameter to identify the task and match it with the result. you will find the specified tag value in the data object of the response")
    __properties: ClassVar[List[str]] = [
        "target", 
        "date_from", 
        "date_to", 
        "location_name", 
        "location_code", 
        "language_name", 
        "language_code", 
        "platform", 
        "tag", 
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

        target_items = []
        if self.target:
            for _item in self.target:
                if _item:
                    target_items.append(_item.to_dict())
            _dict['target'] = target_items
        _dict['date_from'] = self.date_from
        _dict['date_to'] = self.date_to
        _dict['location_name'] = self.location_name
        _dict['location_code'] = self.location_code
        _dict['language_name'] = self.language_name
        _dict['language_code'] = self.language_code
        _dict['platform'] = self.platform
        _dict['tag'] = self.tag
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "target": [BaseAiOptimizationLLmMentionsTargetElement.from_dict(_item) for _item in obj["target"]] if obj.get("target") is not None else None,
            "date_from": obj.get("date_from"),
            "date_to": obj.get("date_to"),
            "location_name": obj.get("location_name"),
            "location_code": obj.get("location_code"),
            "language_name": obj.get("language_name"),
            "language_code": obj.get("language_code"),
            "platform": obj.get("platform"),
            "tag": obj.get("tag"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj