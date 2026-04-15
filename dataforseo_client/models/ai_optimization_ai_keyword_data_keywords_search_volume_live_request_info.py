from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class AiOptimizationAiKeywordDataKeywordsSearchVolumeLiveRequestInfo(BaseModel):
    """
    AiOptimizationAiKeywordDataKeywordsSearchVolumeLiveRequestInfo
    """ # noqa: E501
    keywords: Optional[List[Optional[StrictStr]]] = Field(default=None, description=r"keywordsrequired fieldUTF-8 encodingThe maximum number of keywords you can specify: 1000;The maximum number of characters in a single keyword: 250;The keywords will be converted to lowercase format;learn more about rules and limitations of keyword and keywords fields in DataForSEO APIs in this Help Center article")
    location_name: Optional[StrictStr] = Field(default=None, description=r"full name of the locationrequired field if you don't specify location_codeNote: it is required to specify either location_name or location_codeyou can receive the list of available locations with their location_name by making a separate request to thehttps://api.dataforseo.com/v3/ai_optimization/ai_keyword_data/locations_and_languagesexample:United Kingdom")
    location_code: Optional[StrictInt] = Field(default=None, description=r"unique location identifierrequired field if you don't specify location_nameNote: it is required to specify either location_name or location_codeyou can receive the list of available locations with their location_code by making a separate request to the https://api.dataforseo.com/v3/ai_optimization/ai_keyword_data/locations_and_languagesexample:2840")
    language_name: Optional[StrictStr] = Field(default=None, description=r"full name of the languagerequired field if you don't specify language_codeif you use this field, you don't need to specify language_codeyou can receive the list of available languages with their language_name by making a separate request to thehttps://api.dataforseo.com/v3/ai_optimization/ai_keyword_data/locations_and_languagesexample:English")
    language_code: Optional[StrictStr] = Field(default=None, description=r"language coderequired field if you don't specify language_nameif you use this field, you don't need to specify language_nameyou can receive the list of available languages with their language_code by making a separate request to thehttps://api.dataforseo.com/v3/ai_optimization/ai_keyword_data/locations_and_languagesexample:en")
    tag: Optional[StrictStr] = Field(default=None, description=r"user-defined task identifieroptional fieldthe character limit is 255you can use this parameter to identify the task and match it with the resultyou will find the specified tag value in the data object of the response")
    __properties: ClassVar[List[str]] = [
        "keywords", 
        "location_name", 
        "location_code", 
        "language_name", 
        "language_code", 
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

        _dict['keywords'] = self.keywords
        _dict['location_name'] = self.location_name
        _dict['location_code'] = self.location_code
        _dict['language_name'] = self.language_name
        _dict['language_code'] = self.language_code
        _dict['tag'] = self.tag
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "keywords": obj.get("keywords"),
            "location_name": obj.get("location_name"),
            "location_code": obj.get("location_code"),
            "language_name": obj.get("language_name"),
            "language_code": obj.get("language_code"),
            "tag": obj.get("tag"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj