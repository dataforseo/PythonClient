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
    from dataforseo_client.models.serp_api_people_also_ask_expanded_ai_overview_element_item import SerpApiPeopleAlsoAskExpandedAiOverviewElementItem;
    from dataforseo_client.models.serp_api_people_also_ask_expanded_ai_overview_expanded_element_item import SerpApiPeopleAlsoAskExpandedAiOverviewExpandedElementItem;
    from dataforseo_client.models.serp_api_people_also_ask_expanded_ai_overview_video_element_item import SerpApiPeopleAlsoAskExpandedAiOverviewVideoElementItem;
    from dataforseo_client.models.serp_api_people_also_ask_expanded_ai_overview_table_element_item import SerpApiPeopleAlsoAskExpandedAiOverviewTableElementItem;



class BaseSerpApiPeopleAlsoAskAiOverviewElementItem(BaseModel):
    """
    BaseSerpApiPeopleAlsoAskAiOverviewElementItem
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    position: Optional[StrictStr] = Field(default=None, description="the alignment of the element in SERP. can take the following values:. left, right")
    __properties: ClassVar[List[str]] = [
        "type", 
        "position", 
        ]
    __discriminator_property_name: ClassVar[str] = 'type'
    __discriminator_value_class_map: ClassVar[Dict[str, str]] = {
        'ai_overview_element': 'SerpApiPeopleAlsoAskExpandedAiOverviewElementItem',
        'ai_overview_expanded_element': 'SerpApiPeopleAlsoAskExpandedAiOverviewExpandedElementItem',
        'ai_overview_video_element': 'SerpApiPeopleAlsoAskExpandedAiOverviewVideoElementItem',
        'ai_overview_table_element': 'SerpApiPeopleAlsoAskExpandedAiOverviewTableElementItem',
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

        _dict['type'] = self.type
        _dict['position'] = self.position
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
        SerpApiPeopleAlsoAskExpandedAiOverviewElementItem, 
        SerpApiPeopleAlsoAskExpandedAiOverviewExpandedElementItem, 
        SerpApiPeopleAlsoAskExpandedAiOverviewVideoElementItem, 
        SerpApiPeopleAlsoAskExpandedAiOverviewTableElementItem
    ]]:
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        
        if object_type == 'SerpApiPeopleAlsoAskExpandedAiOverviewElementItem':
            return import_module("dataforseo_client.models.serp_api_people_also_ask_expanded_ai_overview_element_item").SerpApiPeopleAlsoAskExpandedAiOverviewElementItem.from_dict(obj)
        if object_type == 'SerpApiPeopleAlsoAskExpandedAiOverviewExpandedElementItem':
            return import_module("dataforseo_client.models.serp_api_people_also_ask_expanded_ai_overview_expanded_element_item").SerpApiPeopleAlsoAskExpandedAiOverviewExpandedElementItem.from_dict(obj)
        if object_type == 'SerpApiPeopleAlsoAskExpandedAiOverviewVideoElementItem':
            return import_module("dataforseo_client.models.serp_api_people_also_ask_expanded_ai_overview_video_element_item").SerpApiPeopleAlsoAskExpandedAiOverviewVideoElementItem.from_dict(obj)
        if object_type == 'SerpApiPeopleAlsoAskExpandedAiOverviewTableElementItem':
            return import_module("dataforseo_client.models.serp_api_people_also_ask_expanded_ai_overview_table_element_item").SerpApiPeopleAlsoAskExpandedAiOverviewTableElementItem.from_dict(obj)

        raise ValueError("BaseSerpElementItem failed to lookup discriminator value from " +
                         json.dumps(obj) + ". Discriminator property name: " + cls.__discriminator_property_name +
                         ", mapping: " + json.dumps(cls.__discriminator_value_class_map))