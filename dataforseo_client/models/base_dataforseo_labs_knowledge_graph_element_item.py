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
    from dataforseo_client.models.dataforseo_labs_knowledge_graph_images_item_element_item import DataforseoLabsKnowledgeGraphImagesItemElementItem;
    from dataforseo_client.models.dataforseo_labs_knowledge_graph_carousel_item_element_item import DataforseoLabsKnowledgeGraphCarouselItemElementItem;
    from dataforseo_client.models.dataforseo_labs_knowledge_graph_description_item_element_item import DataforseoLabsKnowledgeGraphDescriptionItemElementItem;
    from dataforseo_client.models.dataforseo_labs_knowledge_graph_list_item_element_item import DataforseoLabsKnowledgeGraphListItemElementItem;
    from dataforseo_client.models.dataforseo_labs_knowledge_graph_part_item_element_item import DataforseoLabsKnowledgeGraphPartItemElementItem;
    from dataforseo_client.models.dataforseo_labs_knowledge_graph_expanded_item_element_item import DataforseoLabsKnowledgeGraphExpandedItemElementItem;
    from dataforseo_client.models.dataforseo_labs_knowledge_graph_row_item_element_item import DataforseoLabsKnowledgeGraphRowItemElementItem;
    from dataforseo_client.models.dataforseo_labs_knowledge_graph_shopping_item_element_item import DataforseoLabsKnowledgeGraphShoppingItemElementItem;



class BaseDataforseoLabsKnowledgeGraphElementItem(BaseModel):
    """
    BaseDataforseoLabsKnowledgeGraphElementItem
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    rank_group: Optional[StrictInt] = Field(default=None, description="position within a group of elements with identical type values. positions of elements with different type values are omitted from rank_group")
    rank_absolute: Optional[StrictInt] = Field(default=None, description="absolute rank in SERP. absolute position among all the elements in SERP")
    position: Optional[StrictStr] = Field(default=None, description="the alignment of the element in SERP. can take the following values:. left, right")
    xpath: Optional[StrictStr] = Field(default=None, description="the XPath of the element")
    __properties: ClassVar[List[str]] = [
        "type", 
        "rank_group", 
        "rank_absolute", 
        "position", 
        "xpath", 
        ]
    __discriminator_property_name: ClassVar[str] = 'type'
    __discriminator_value_class_map: ClassVar[Dict[str, str]] = {
        'knowledge_graph_images_item': 'DataforseoLabsKnowledgeGraphImagesItemElementItem',
        'knowledge_graph_carousel_item': 'DataforseoLabsKnowledgeGraphCarouselItemElementItem',
        'knowledge_graph_description_item': 'DataforseoLabsKnowledgeGraphDescriptionItemElementItem',
        'knowledge_graph_list_item': 'DataforseoLabsKnowledgeGraphListItemElementItem',
        'knowledge_graph_part_item': 'DataforseoLabsKnowledgeGraphPartItemElementItem',
        'knowledge_graph_expanded_item': 'DataforseoLabsKnowledgeGraphExpandedItemElementItem',
        'knowledge_graph_row_item': 'DataforseoLabsKnowledgeGraphRowItemElementItem',
        'knowledge_graph_shopping_item': 'DataforseoLabsKnowledgeGraphShoppingItemElementItem',
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
        _dict['rank_group'] = self.rank_group
        _dict['rank_absolute'] = self.rank_absolute
        _dict['position'] = self.position
        _dict['xpath'] = self.xpath
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
        DataforseoLabsKnowledgeGraphImagesItemElementItem, 
        DataforseoLabsKnowledgeGraphCarouselItemElementItem, 
        DataforseoLabsKnowledgeGraphDescriptionItemElementItem, 
        DataforseoLabsKnowledgeGraphListItemElementItem, 
        DataforseoLabsKnowledgeGraphPartItemElementItem, 
        DataforseoLabsKnowledgeGraphExpandedItemElementItem, 
        DataforseoLabsKnowledgeGraphRowItemElementItem, 
        DataforseoLabsKnowledgeGraphShoppingItemElementItem
    ]]:
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        
        if object_type == 'DataforseoLabsKnowledgeGraphImagesItemElementItem':
            return import_module("dataforseo_client.models.dataforseo_labs_knowledge_graph_images_item_element_item").DataforseoLabsKnowledgeGraphImagesItemElementItem.from_dict(obj)
        if object_type == 'DataforseoLabsKnowledgeGraphCarouselItemElementItem':
            return import_module("dataforseo_client.models.dataforseo_labs_knowledge_graph_carousel_item_element_item").DataforseoLabsKnowledgeGraphCarouselItemElementItem.from_dict(obj)
        if object_type == 'DataforseoLabsKnowledgeGraphDescriptionItemElementItem':
            return import_module("dataforseo_client.models.dataforseo_labs_knowledge_graph_description_item_element_item").DataforseoLabsKnowledgeGraphDescriptionItemElementItem.from_dict(obj)
        if object_type == 'DataforseoLabsKnowledgeGraphListItemElementItem':
            return import_module("dataforseo_client.models.dataforseo_labs_knowledge_graph_list_item_element_item").DataforseoLabsKnowledgeGraphListItemElementItem.from_dict(obj)
        if object_type == 'DataforseoLabsKnowledgeGraphPartItemElementItem':
            return import_module("dataforseo_client.models.dataforseo_labs_knowledge_graph_part_item_element_item").DataforseoLabsKnowledgeGraphPartItemElementItem.from_dict(obj)
        if object_type == 'DataforseoLabsKnowledgeGraphExpandedItemElementItem':
            return import_module("dataforseo_client.models.dataforseo_labs_knowledge_graph_expanded_item_element_item").DataforseoLabsKnowledgeGraphExpandedItemElementItem.from_dict(obj)
        if object_type == 'DataforseoLabsKnowledgeGraphRowItemElementItem':
            return import_module("dataforseo_client.models.dataforseo_labs_knowledge_graph_row_item_element_item").DataforseoLabsKnowledgeGraphRowItemElementItem.from_dict(obj)
        if object_type == 'DataforseoLabsKnowledgeGraphShoppingItemElementItem':
            return import_module("dataforseo_client.models.dataforseo_labs_knowledge_graph_shopping_item_element_item").DataforseoLabsKnowledgeGraphShoppingItemElementItem.from_dict(obj)

        return None