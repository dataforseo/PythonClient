from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.base_ai_optimization_l_lm_mentions_target_element import BaseAiOptimizationLLmMentionsTargetElement



class AiOptimizationLLmMentionsKeywordElement(BaseAiOptimizationLLmMentionsTargetElement):
    """
    AiOptimizationLLmMentionsKeywordElement
    """ # noqa: E501
    search_scope: Optional[List[Optional[StrictStr]]] = Field(default=None, description=r"target domain search scope. optional field. possible values:. any, sources, search_results. default value: any")
    search_filter: Optional[StrictStr] = Field(default=None, description=r"target domain search filter. optional field. possible values:. include, exclude. default value: include")
    keyword: Optional[StrictStr] = Field(default=None, description=r"target keyword. required field if you don’t specify domain. you can specify up to 2000 characters in the keyword field. all %## will be decoded (plus character ‘+’ will be decoded to a space character). if you need to use the “%” character for your keyword, please specify it as “%25”;. if you need to use the “+” character for your keyword, please specify it as “%2B”. learn more about rules and limitations of keyword and keywords fields in")
    match_type: Optional[StrictStr] = Field(default=None, description=r"target keyword match type. defines how the specified keyword is matched. optional field. possible values:. word_match – full-text search for terms that match the specified seed keyword with additional words included before, after, or within the key phrase (e.g., search for “light” will return results with “light bulb”, “light switch”);. partial_match – substring search that finds all instances containing the specified sequence of characters, even if it appears inside a longer word (e.g., search for “light” will return results with “lighting”, “highlight”);. default value: word_match")
    search_scope: Optional[List[Optional[StrictStr]]] = Field(default=None, description=r"target domain search scope. optional field. possible values:. any, sources, search_results. default value: any")
    search_filter: Optional[StrictStr] = Field(default=None, description=r"target domain search filter. optional field. possible values:. include, exclude. default value: include")
    __properties: ClassVar[List[str]] = [
        "search_scope", 
        "search_filter", 
        "keyword", 
        "match_type", 
        "search_scope", 
        "search_filter", 
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

        _dict['search_scope'] = self.search_scope
        _dict['search_filter'] = self.search_filter
        _dict['keyword'] = self.keyword
        _dict['match_type'] = self.match_type
        _dict['search_scope'] = self.search_scope
        _dict['search_filter'] = self.search_filter
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "search_scope": obj.get("search_scope"),
            "search_filter": obj.get("search_filter"),
            "keyword": obj.get("keyword"),
            "match_type": obj.get("match_type"),
            "search_scope": obj.get("search_scope"),
            "search_filter": obj.get("search_filter"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj