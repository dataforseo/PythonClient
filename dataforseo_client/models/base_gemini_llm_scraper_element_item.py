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
    from dataforseo_client.models.gemini_text_element_item import GeminiTextElementItem;
    from dataforseo_client.models.gemini_table_element_item import GeminiTableElementItem;
    from dataforseo_client.models.gemini_images_element_item import GeminiImagesElementItem;



class BaseGeminiLlmScraperElementItem(BaseModel):
    """
    BaseGeminiLlmScraperElementItem
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description=r"type of element")
    rank_group: Optional[StrictInt] = Field(default=None, description=r"group rank in SERP. position within a group of elements with identical type values. positions of elements with different type values are omitted from rank_group")
    rank_absolute: Optional[StrictInt] = Field(default=None, description=r"absolute rank in SERP. absolute position among all the elements in SERP")
    markdown: Optional[StrictStr] = Field(default=None, description=r"content of the element in markdown format. content of the result formatted in the markdown markup language")
    __properties: ClassVar[List[str]] = [
        "type", 
        "rank_group", 
        "rank_absolute", 
        "markdown", 
        ]
    __discriminator_property_name: ClassVar[str] = 'type'
    __discriminator_value_class_map: ClassVar[Dict[str, str]] = {
        'gemini_text': 'GeminiTextElementItem',
        'gemini_table': 'GeminiTableElementItem',
        'gemini_images': 'GeminiImagesElementItem',
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
        _dict['markdown'] = self.markdown
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
        GeminiTextElementItem, 
        GeminiTableElementItem, 
        GeminiImagesElementItem
    ]]:
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        
        if object_type == 'GeminiTextElementItem':
            return import_module("dataforseo_client.models.gemini_text_element_item").GeminiTextElementItem.from_dict(obj)
        if object_type == 'GeminiTableElementItem':
            return import_module("dataforseo_client.models.gemini_table_element_item").GeminiTableElementItem.from_dict(obj)
        if object_type == 'GeminiImagesElementItem':
            return import_module("dataforseo_client.models.gemini_images_element_item").GeminiImagesElementItem.from_dict(obj)

        return None