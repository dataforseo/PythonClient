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
    from dataforseo_client.models.chat_gpt_text_element_item import ChatGptTextElementItem;
    from dataforseo_client.models.chat_gpt_table_element_item import ChatGptTableElementItem;
    from dataforseo_client.models.chat_gpt_navigation_list_element_item import ChatGptNavigationListElementItem;
    from dataforseo_client.models.chat_gpt_images_element_item import ChatGptImagesElementItem;
    from dataforseo_client.models.chat_gpt_products_element_item import ChatGptProductsElementItem;
    from dataforseo_client.models.chat_gpt_local_businesses_element_item import ChatGptLocalBusinessesElementItem;



class BaseChatGptLlmScraperElementItem(BaseModel):
    """
    BaseChatGptLlmScraperElementItem
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description=r"type of element")
    rank_group: Optional[StrictInt] = Field(default=None, description=r"group rank in SERP. position within a group of elements with identical type values. positions of elements with different type values are omitted from rank_group")
    rank_absolute: Optional[StrictInt] = Field(default=None, description=r"absolute rank in SERP. absolute position among all the elements")
    __properties: ClassVar[List[str]] = [
        "type", 
        "rank_group", 
        "rank_absolute", 
        ]
    __discriminator_property_name: ClassVar[str] = 'type'
    __discriminator_value_class_map: ClassVar[Dict[str, str]] = {
        'chat_gpt_text': 'ChatGptTextElementItem',
        'chat_gpt_table': 'ChatGptTableElementItem',
        'chat_gpt_navigation_list': 'ChatGptNavigationListElementItem',
        'chat_gpt_images': 'ChatGptImagesElementItem',
        'chat_gpt_products': 'ChatGptProductsElementItem',
        'chat_gpt_local_businesses': 'ChatGptLocalBusinessesElementItem',
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
        ChatGptTextElementItem, 
        ChatGptTableElementItem, 
        ChatGptNavigationListElementItem, 
        ChatGptImagesElementItem, 
        ChatGptProductsElementItem, 
        ChatGptLocalBusinessesElementItem
    ]]:
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        
        if object_type == 'ChatGptTextElementItem':
            return import_module("dataforseo_client.models.chat_gpt_text_element_item").ChatGptTextElementItem.from_dict(obj)
        if object_type == 'ChatGptTableElementItem':
            return import_module("dataforseo_client.models.chat_gpt_table_element_item").ChatGptTableElementItem.from_dict(obj)
        if object_type == 'ChatGptNavigationListElementItem':
            return import_module("dataforseo_client.models.chat_gpt_navigation_list_element_item").ChatGptNavigationListElementItem.from_dict(obj)
        if object_type == 'ChatGptImagesElementItem':
            return import_module("dataforseo_client.models.chat_gpt_images_element_item").ChatGptImagesElementItem.from_dict(obj)
        if object_type == 'ChatGptProductsElementItem':
            return import_module("dataforseo_client.models.chat_gpt_products_element_item").ChatGptProductsElementItem.from_dict(obj)
        if object_type == 'ChatGptLocalBusinessesElementItem':
            return import_module("dataforseo_client.models.chat_gpt_local_businesses_element_item").ChatGptLocalBusinessesElementItem.from_dict(obj)

        return None