from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self


from importlib import import_module
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from dataforseo_client.models.ai_optimization_l_lm_mentions_domain_element import AiOptimizationLLmMentionsDomainElement;
    from dataforseo_client.models.ai_optimization_l_lm_mentions_keyword_element import AiOptimizationLLmMentionsKeywordElement;



class BaseAiOptimizationLLmMentionsTargetElement(BaseModel):
    """
    BaseAiOptimizationLLmMentionsTargetElement
    """ # noqa: E501
    search_scope: Optional[List[Optional[StrictStr]]] = Field(default=None, description=r"target domain search scope. optional field. possible values:. any, sources, search_results. default value: any")
    search_filter: Optional[StrictStr] = Field(default=None, description=r"target domain search filter. optional field. possible values:. include, exclude. default value: include")
    __properties: ClassVar[List[str]] = [
        "search_scope", 
        "search_filter", 
        ]
    __discriminator_property_name: ClassVar[str] = 'type'
    __discriminator_value_class_map: ClassVar[Dict[str, str]] = {
        'domain': 'AiOptimizationLLmMentionsDomainElement',
        'keyword': 'AiOptimizationLLmMentionsKeywordElement',
    }

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
        return _dict


    @classmethod
    def get_discriminator_value(cls, obj: Dict[str, Any]) -> Optional[str]:
        discriminator_value = obj[cls.__discriminator_property_name]
        if discriminator_value:
            return cls.__discriminator_value_class_map.get(discriminator_value)
        else:
            return None
    
    @classmethod
    def from_dict(cls, obj: Dict[str, Any]) -> Optional[Union[
        AiOptimizationLLmMentionsDomainElement, 
        AiOptimizationLLmMentionsKeywordElement
    ]]:
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        
        if object_type == 'AiOptimizationLLmMentionsDomainElement':
            return import_module("dataforseo_client.models.ai_optimization_l_lm_mentions_domain_element").AiOptimizationLLmMentionsDomainElement.from_dict(obj)
        if object_type == 'AiOptimizationLLmMentionsKeywordElement':
            return import_module("dataforseo_client.models.ai_optimization_l_lm_mentions_keyword_element").AiOptimizationLLmMentionsKeywordElement.from_dict(obj)

        return None