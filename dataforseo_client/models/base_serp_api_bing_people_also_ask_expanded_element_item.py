from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.ai_mode_images_element_info import AiModeImagesElementInfo
from dataforseo_client.models.table import Table

from importlib import import_module
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from dataforseo_client.models.serp_api_bing_people_also_ask_expanded_element_item import SerpApiBingPeopleAlsoAskExpandedElementItem;



class BaseSerpApiBingPeopleAlsoAskExpandedElementItem(BaseModel):
    """
    BaseSerpApiBingPeopleAlsoAskExpandedElementItem
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description=r"type of element")
    featured_title: Optional[StrictStr] = Field(default=None, description=r"title")
    url: Optional[StrictStr] = Field(default=None, description=r"URL")
    domain: Optional[StrictStr] = Field(default=None, description=r"domain in SERP")
    title: Optional[StrictStr] = Field(default=None, description=r"title of the result in SERP")
    description: Optional[StrictStr] = Field(default=None, description=r"description of the results element in SERP")
    images: Optional[List[Optional[AiModeImagesElementInfo]]] = Field(default=None, description=r"images of the element")
    timestamp: Optional[StrictStr] = Field(default=None, description=r"date and time when the video was published. in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”. example: 2009-01-01 00:00:00 +00:00")
    table: Optional[Table] = Field(default=None, description=r"results table. if there are none, equals null")
    __properties: ClassVar[List[str]] = [
        "type", 
        "featured_title", 
        "url", 
        "domain", 
        "title", 
        "description", 
        "images", 
        "timestamp", 
        "table", 
        ]
    __discriminator_property_name: ClassVar[str] = 'type'
    __discriminator_value_class_map: ClassVar[Dict[str, str]] = {
        'people_also_ask_expanded_element': 'SerpApiBingPeopleAlsoAskExpandedElementItem',
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
        _dict['featured_title'] = self.featured_title
        _dict['url'] = self.url
        _dict['domain'] = self.domain
        _dict['title'] = self.title
        _dict['description'] = self.description
        images_items = []
        if self.images:
            for _item in self.images:
                if _item:
                    images_items.append(_item.to_dict())
            _dict['images'] = images_items
        _dict['timestamp'] = self.timestamp
        _dict['table'] = self.table.to_dict() if self.table else None
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
        SerpApiBingPeopleAlsoAskExpandedElementItem
    ]]:
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        
        if object_type == 'SerpApiBingPeopleAlsoAskExpandedElementItem':
            return import_module("dataforseo_client.models.serp_api_bing_people_also_ask_expanded_element_item").SerpApiBingPeopleAlsoAskExpandedElementItem.from_dict(obj)

        return None