from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.base_ai_optimization_l_lm_mentions_target_element import BaseAiOptimizationLLmMentionsTargetElement



class AiOptimizationLLmMentionsDomainElement(BaseAiOptimizationLLmMentionsTargetElement):
    """
    AiOptimizationLLmMentionsDomainElement
    """ # noqa: E501
    search_scope: Optional[List[Optional[StrictStr]]] = Field(default=None, description=r"target domain search scope. optional field. possible values:. any, sources, search_results. default value: any")
    search_filter: Optional[StrictStr] = Field(default=None, description=r"target domain search filter. optional field. possible values:. include, exclude. default value: include")
    domain: Optional[StrictStr] = Field(default=None, description=r"target domain. required field if you don’t specify keyword. a domain should be specified without https:// and www.")
    include_subdomains: Optional[StrictBool] = Field(default=None, description=r"indicates if the subdomains of the target domain will be included in the search. optional field. if set to true, the subdomains will be included in the search. default value: false")
    search_scope: Optional[List[Optional[StrictStr]]] = Field(default=None, description=r"target domain search scope. optional field. possible values:. any, sources, search_results. default value: any")
    search_filter: Optional[StrictStr] = Field(default=None, description=r"target domain search filter. optional field. possible values:. include, exclude. default value: include")
    __properties: ClassVar[List[str]] = [
        "search_scope", 
        "search_filter", 
        "domain", 
        "include_subdomains", 
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
        _dict['domain'] = self.domain
        _dict['include_subdomains'] = self.include_subdomains
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
            "domain": obj.get("domain"),
            "include_subdomains": obj.get("include_subdomains"),
            "search_scope": obj.get("search_scope"),
            "search_filter": obj.get("search_filter"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj