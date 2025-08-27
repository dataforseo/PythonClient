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
    from dataforseo_client.models.merchant_amazon_paid_serp_element_item import MerchantAmazonPaidSerpElementItem;
    from dataforseo_client.models.merchant_amazon_serp_serp_element_item import MerchantAmazonSerpSerpElementItem;
    from dataforseo_client.models.merchant_editorial_recommendations_serp_element_item import MerchantEditorialRecommendationsSerpElementItem;
    from dataforseo_client.models.merchant_related_searches_serp_element_item import MerchantRelatedSearchesSerpElementItem;
    from dataforseo_client.models.merchant_top_rated_from_our_brands_serp_element_item import MerchantTopRatedFromOurBrandsSerpElementItem;



class BaseMerchantAmazonElementItem(BaseModel):
    """
    BaseMerchantAmazonElementItem
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    rank_group: Optional[StrictInt] = Field(default=None, description="position within a group of elements with identical type values. positions of elements with different type values are omitted from rank_group")
    rank_absolute: Optional[StrictInt] = Field(default=None, description="absolute rank in SERP. absolute position among all the elements found in Amazon SERP")
    xpath: Optional[StrictStr] = Field(default=None, description="the XPath of the element")
    __properties: ClassVar[List[str]] = [
        "type", 
        "rank_group", 
        "rank_absolute", 
        "xpath", 
        ]
    __discriminator_property_name: ClassVar[str] = 'type'
    __discriminator_value_class_map: ClassVar[Dict[str, str]] = {
        'amazon_paid': 'MerchantAmazonPaidSerpElementItem',
        'amazon_serp': 'MerchantAmazonSerpSerpElementItem',
        'editorial_recommendations': 'MerchantEditorialRecommendationsSerpElementItem',
        'related_searches': 'MerchantRelatedSearchesSerpElementItem',
        'top_rated_from_our_brands': 'MerchantTopRatedFromOurBrandsSerpElementItem',
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
        MerchantAmazonPaidSerpElementItem, 
        MerchantAmazonSerpSerpElementItem, 
        MerchantEditorialRecommendationsSerpElementItem, 
        MerchantRelatedSearchesSerpElementItem, 
        MerchantTopRatedFromOurBrandsSerpElementItem
    ]]:
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        
        if object_type == 'MerchantAmazonPaidSerpElementItem':
            return import_module("dataforseo_client.models.merchant_amazon_paid_serp_element_item").MerchantAmazonPaidSerpElementItem.from_dict(obj)
        if object_type == 'MerchantAmazonSerpSerpElementItem':
            return import_module("dataforseo_client.models.merchant_amazon_serp_serp_element_item").MerchantAmazonSerpSerpElementItem.from_dict(obj)
        if object_type == 'MerchantEditorialRecommendationsSerpElementItem':
            return import_module("dataforseo_client.models.merchant_editorial_recommendations_serp_element_item").MerchantEditorialRecommendationsSerpElementItem.from_dict(obj)
        if object_type == 'MerchantRelatedSearchesSerpElementItem':
            return import_module("dataforseo_client.models.merchant_related_searches_serp_element_item").MerchantRelatedSearchesSerpElementItem.from_dict(obj)
        if object_type == 'MerchantTopRatedFromOurBrandsSerpElementItem':
            return import_module("dataforseo_client.models.merchant_top_rated_from_our_brands_serp_element_item").MerchantTopRatedFromOurBrandsSerpElementItem.from_dict(obj)

        return None