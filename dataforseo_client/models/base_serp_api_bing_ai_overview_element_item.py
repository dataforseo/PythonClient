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
    from dataforseo_client.models.serp_api_bing_ai_overview_element_item import SerpApiBingAiOverviewElementItem;
    from dataforseo_client.models.serp_api_bing_ai_overview_video_element_item import SerpApiBingAiOverviewVideoElementItem;
    from dataforseo_client.models.serp_api_bing_ai_overview_videos_element_item import SerpApiBingAiOverviewVideosElementItem;
    from dataforseo_client.models.serp_api_bing_ai_overview_images_element_item import SerpApiBingAiOverviewImagesElementItem;
    from dataforseo_client.models.serp_api_bing_ai_overview_organic_element_item import SerpApiBingAiOverviewOrganicElementItem;
    from dataforseo_client.models.serp_api_bing_ai_overview_shopping_item import SerpApiBingAiOverviewShoppingItem;



class BaseSerpApiBingAiOverviewElementItem(BaseModel):
    """
    BaseSerpApiBingAiOverviewElementItem
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description=r"type of element")
    __properties: ClassVar[List[str]] = [
        "type", 
        ]
    __discriminator_property_name: ClassVar[str] = 'type'
    __discriminator_value_class_map: ClassVar[Dict[str, str]] = {
        'ai_overview_element': 'SerpApiBingAiOverviewElementItem',
        'ai_overview_video_element': 'SerpApiBingAiOverviewVideoElementItem',
        'ai_overview_videos_element': 'SerpApiBingAiOverviewVideosElementItem',
        'ai_overview_images_element': 'SerpApiBingAiOverviewImagesElementItem',
        'ai_overview_organic_element': 'SerpApiBingAiOverviewOrganicElementItem',
        'ai_overview_shopping': 'SerpApiBingAiOverviewShoppingItem',
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
        SerpApiBingAiOverviewElementItem, 
        SerpApiBingAiOverviewVideoElementItem, 
        SerpApiBingAiOverviewVideosElementItem, 
        SerpApiBingAiOverviewImagesElementItem, 
        SerpApiBingAiOverviewOrganicElementItem, 
        SerpApiBingAiOverviewShoppingItem
    ]]:
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        
        if object_type == 'SerpApiBingAiOverviewElementItem':
            return import_module("dataforseo_client.models.serp_api_bing_ai_overview_element_item").SerpApiBingAiOverviewElementItem.from_dict(obj)
        if object_type == 'SerpApiBingAiOverviewVideoElementItem':
            return import_module("dataforseo_client.models.serp_api_bing_ai_overview_video_element_item").SerpApiBingAiOverviewVideoElementItem.from_dict(obj)
        if object_type == 'SerpApiBingAiOverviewVideosElementItem':
            return import_module("dataforseo_client.models.serp_api_bing_ai_overview_videos_element_item").SerpApiBingAiOverviewVideosElementItem.from_dict(obj)
        if object_type == 'SerpApiBingAiOverviewImagesElementItem':
            return import_module("dataforseo_client.models.serp_api_bing_ai_overview_images_element_item").SerpApiBingAiOverviewImagesElementItem.from_dict(obj)
        if object_type == 'SerpApiBingAiOverviewOrganicElementItem':
            return import_module("dataforseo_client.models.serp_api_bing_ai_overview_organic_element_item").SerpApiBingAiOverviewOrganicElementItem.from_dict(obj)
        if object_type == 'SerpApiBingAiOverviewShoppingItem':
            return import_module("dataforseo_client.models.serp_api_bing_ai_overview_shopping_item").SerpApiBingAiOverviewShoppingItem.from_dict(obj)

        return None