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
    from dataforseo_client.models.google_shopping_serp_element_item import GoogleShoppingSerpElementItem;
    from dataforseo_client.models.google_shopping_paid_element_item import GoogleShoppingPaidElementItem;
    from dataforseo_client.models.google_shopping_sponsored_carousel_element_item import GoogleShoppingSponsoredCarouselElementItem;
    from dataforseo_client.models.related_searches_element_item import RelatedSearchesElementItem;



class BaseMerchantGoogleShoppingProductsElementItem(BaseModel):
    """
    BaseMerchantGoogleShoppingProductsElementItem
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    rank_group: Optional[StrictInt] = Field(default=None, description="position within a group of elements with identical type values. positions of elements with different type values are omitted from rank_group")
    rank_absolute: Optional[StrictInt] = Field(default=None, description="absolute rank in SERP. absolute position among all the elements found in Google Shopping SERP")
    position: Optional[StrictStr] = Field(default=None, description="alignment of the element in SERP. can take the following values:. left, right")
    xpath: Optional[StrictStr] = Field(default=None, description="XPath of the element")
    __properties: ClassVar[List[str]] = [
        "type", 
        "rank_group", 
        "rank_absolute", 
        "position", 
        "xpath", 
        ]
    __discriminator_property_name: ClassVar[str] = 'type'
    __discriminator_value_class_map: ClassVar[Dict[str, str]] = {
        'google_shopping_serp': 'GoogleShoppingSerpElementItem',
        'google_shopping_paid': 'GoogleShoppingPaidElementItem',
        'google_shopping_sponsored_carousel': 'GoogleShoppingSponsoredCarouselElementItem',
        'related_searches': 'RelatedSearchesElementItem',
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
        GoogleShoppingSerpElementItem, 
        GoogleShoppingPaidElementItem, 
        GoogleShoppingSponsoredCarouselElementItem, 
        RelatedSearchesElementItem
    ]]:
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        
        if object_type == 'GoogleShoppingSerpElementItem':
            return import_module("dataforseo_client.models.google_shopping_serp_element_item").GoogleShoppingSerpElementItem.from_dict(obj)
        if object_type == 'GoogleShoppingPaidElementItem':
            return import_module("dataforseo_client.models.google_shopping_paid_element_item").GoogleShoppingPaidElementItem.from_dict(obj)
        if object_type == 'GoogleShoppingSponsoredCarouselElementItem':
            return import_module("dataforseo_client.models.google_shopping_sponsored_carousel_element_item").GoogleShoppingSponsoredCarouselElementItem.from_dict(obj)
        if object_type == 'RelatedSearchesElementItem':
            return import_module("dataforseo_client.models.related_searches_element_item").RelatedSearchesElementItem.from_dict(obj)

        raise ValueError("BaseSerpElementItem failed to lookup discriminator value from " +
                         json.dumps(obj) + ". Discriminator property name: " + cls.__discriminator_property_name +
                         ", mapping: " + json.dumps(cls.__discriminator_value_class_map))