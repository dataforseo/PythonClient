from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.ai_mode_rectangle_info import AiModeRectangleInfo

from importlib import import_module
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from dataforseo_client.models.serp_api_knowledge_graph_carousel_item_element_item import SerpApiKnowledgeGraphCarouselItemElementItem;
    from dataforseo_client.models.serp_api_knowledge_graph_description_item_element_item import SerpApiKnowledgeGraphDescriptionItemElementItem;
    from dataforseo_client.models.serp_api_knowledge_graph_images_item_element_item import SerpApiKnowledgeGraphImagesItemElementItem;
    from dataforseo_client.models.serp_api_knowledge_graph_list_item_element_item import SerpApiKnowledgeGraphListItemElementItem;
    from dataforseo_client.models.serp_api_knowledge_graph_row_item_element_item import SerpApiKnowledgeGraphRowItemElementItem;
    from dataforseo_client.models.serp_api_knowledge_graph_expanded_item_element_item import SerpApiKnowledgeGraphExpandedItemElementItem;
    from dataforseo_client.models.serp_api_knowledge_graph_part_item_element_item import SerpApiKnowledgeGraphPartItemElementItem;
    from dataforseo_client.models.serp_api_knowledge_graph_shopping_item_element_item import SerpApiKnowledgeGraphShoppingItemElementItem;
    from dataforseo_client.models.serp_api_knowledge_graph_hotels_booking_item_element_item import SerpApiKnowledgeGraphHotelsBookingItemElementItem;
    from dataforseo_client.models.serp_api_knowledge_graph_ai_overview_item_element_item import SerpApiKnowledgeGraphAiOverviewItemElementItem;



class BaseSerpApiKnowledgeGraphElementItem(BaseModel):
    """
    BaseSerpApiKnowledgeGraphElementItem
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    position: Optional[StrictStr] = Field(default=None, description="the alignment of the element in SERP. can take the following values:. left, right")
    xpath: Optional[StrictStr] = Field(default=None, description="the XPath of the element")
    rectangle: Optional[AiModeRectangleInfo] = Field(default=None, description="rectangle parameters. contains cartesian coordinates and pixel dimensions of the result’s snippet in SERP. equals null if calculate_rectangles in the POST request is not set to true")
    __properties: ClassVar[List[str]] = [
        "type", 
        "position", 
        "xpath", 
        "rectangle", 
        ]
    __discriminator_property_name: ClassVar[str] = 'type'
    __discriminator_value_class_map: ClassVar[Dict[str, str]] = {
        'knowledge_graph_carousel_item': 'SerpApiKnowledgeGraphCarouselItemElementItem',
        'knowledge_graph_description_item': 'SerpApiKnowledgeGraphDescriptionItemElementItem',
        'knowledge_graph_images_item': 'SerpApiKnowledgeGraphImagesItemElementItem',
        'knowledge_graph_list_item': 'SerpApiKnowledgeGraphListItemElementItem',
        'knowledge_graph_row_item': 'SerpApiKnowledgeGraphRowItemElementItem',
        'knowledge_graph_expanded_item': 'SerpApiKnowledgeGraphExpandedItemElementItem',
        'knowledge_graph_part_item': 'SerpApiKnowledgeGraphPartItemElementItem',
        'knowledge_graph_shopping_item': 'SerpApiKnowledgeGraphShoppingItemElementItem',
        'knowledge_graph_hotels_booking_item': 'SerpApiKnowledgeGraphHotelsBookingItemElementItem',
        'knowledge_graph_ai_overview_item': 'SerpApiKnowledgeGraphAiOverviewItemElementItem',
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
        _dict['xpath'] = self.xpath
        _dict['rectangle'] = self.rectangle.to_dict() if self.rectangle else None
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
        SerpApiKnowledgeGraphCarouselItemElementItem, 
        SerpApiKnowledgeGraphDescriptionItemElementItem, 
        SerpApiKnowledgeGraphImagesItemElementItem, 
        SerpApiKnowledgeGraphListItemElementItem, 
        SerpApiKnowledgeGraphRowItemElementItem, 
        SerpApiKnowledgeGraphExpandedItemElementItem, 
        SerpApiKnowledgeGraphPartItemElementItem, 
        SerpApiKnowledgeGraphShoppingItemElementItem, 
        SerpApiKnowledgeGraphHotelsBookingItemElementItem, 
        SerpApiKnowledgeGraphAiOverviewItemElementItem
    ]]:
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        
        if object_type == 'SerpApiKnowledgeGraphCarouselItemElementItem':
            return import_module("dataforseo_client.models.serp_api_knowledge_graph_carousel_item_element_item").SerpApiKnowledgeGraphCarouselItemElementItem.from_dict(obj)
        if object_type == 'SerpApiKnowledgeGraphDescriptionItemElementItem':
            return import_module("dataforseo_client.models.serp_api_knowledge_graph_description_item_element_item").SerpApiKnowledgeGraphDescriptionItemElementItem.from_dict(obj)
        if object_type == 'SerpApiKnowledgeGraphImagesItemElementItem':
            return import_module("dataforseo_client.models.serp_api_knowledge_graph_images_item_element_item").SerpApiKnowledgeGraphImagesItemElementItem.from_dict(obj)
        if object_type == 'SerpApiKnowledgeGraphListItemElementItem':
            return import_module("dataforseo_client.models.serp_api_knowledge_graph_list_item_element_item").SerpApiKnowledgeGraphListItemElementItem.from_dict(obj)
        if object_type == 'SerpApiKnowledgeGraphRowItemElementItem':
            return import_module("dataforseo_client.models.serp_api_knowledge_graph_row_item_element_item").SerpApiKnowledgeGraphRowItemElementItem.from_dict(obj)
        if object_type == 'SerpApiKnowledgeGraphExpandedItemElementItem':
            return import_module("dataforseo_client.models.serp_api_knowledge_graph_expanded_item_element_item").SerpApiKnowledgeGraphExpandedItemElementItem.from_dict(obj)
        if object_type == 'SerpApiKnowledgeGraphPartItemElementItem':
            return import_module("dataforseo_client.models.serp_api_knowledge_graph_part_item_element_item").SerpApiKnowledgeGraphPartItemElementItem.from_dict(obj)
        if object_type == 'SerpApiKnowledgeGraphShoppingItemElementItem':
            return import_module("dataforseo_client.models.serp_api_knowledge_graph_shopping_item_element_item").SerpApiKnowledgeGraphShoppingItemElementItem.from_dict(obj)
        if object_type == 'SerpApiKnowledgeGraphHotelsBookingItemElementItem':
            return import_module("dataforseo_client.models.serp_api_knowledge_graph_hotels_booking_item_element_item").SerpApiKnowledgeGraphHotelsBookingItemElementItem.from_dict(obj)
        if object_type == 'SerpApiKnowledgeGraphAiOverviewItemElementItem':
            return import_module("dataforseo_client.models.serp_api_knowledge_graph_ai_overview_item_element_item").SerpApiKnowledgeGraphAiOverviewItemElementItem.from_dict(obj)

        raise ValueError("BaseSerpElementItem failed to lookup discriminator value from " +
                         json.dumps(obj) + ". Discriminator property name: " + cls.__discriminator_property_name +
                         ", mapping: " + json.dumps(cls.__discriminator_value_class_map))