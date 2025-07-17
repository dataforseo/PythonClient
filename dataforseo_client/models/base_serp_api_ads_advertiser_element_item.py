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
    from dataforseo_client.models.serp_api_ads_multi_account_advertiser_element_item import SerpApiAdsMultiAccountAdvertiserElementItem;
    from dataforseo_client.models.serp_api_ads_advertiser_element_item import SerpApiAdsAdvertiserElementItem;
    from dataforseo_client.models.serp_api_ads_domain_element_item import SerpApiAdsDomainElementItem;



class BaseSerpApiAdsAdvertiserElementItem(BaseModel):
    """
    BaseSerpApiAdsAdvertiserElementItem
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    rank_group: Optional[StrictInt] = Field(default=None, description="group rank in SERP. position within a group of elements with identical type values. positions of elements with different type values are omitted from rank_group")
    rank_absolute: Optional[StrictInt] = Field(default=None, description="absolute rank in SERP. absolute position among all the elements in SERP")
    __properties: ClassVar[List[str]] = [
        "type", 
        "rank_group", 
        "rank_absolute", 
        ]
    __discriminator_property_name: ClassVar[str] = 'type'
    __discriminator_value_class_map: ClassVar[Dict[str, str]] = {
        'ads_multi_account_advertiser': 'SerpApiAdsMultiAccountAdvertiserElementItem',
        'ads_advertiser': 'SerpApiAdsAdvertiserElementItem',
        'ads_domain': 'SerpApiAdsDomainElementItem',
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
        SerpApiAdsMultiAccountAdvertiserElementItem, 
        SerpApiAdsAdvertiserElementItem, 
        SerpApiAdsDomainElementItem
    ]]:
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        
        if object_type == 'SerpApiAdsMultiAccountAdvertiserElementItem':
            return import_module("dataforseo_client.models.serp_api_ads_multi_account_advertiser_element_item").SerpApiAdsMultiAccountAdvertiserElementItem.from_dict(obj)
        if object_type == 'SerpApiAdsAdvertiserElementItem':
            return import_module("dataforseo_client.models.serp_api_ads_advertiser_element_item").SerpApiAdsAdvertiserElementItem.from_dict(obj)
        if object_type == 'SerpApiAdsDomainElementItem':
            return import_module("dataforseo_client.models.serp_api_ads_domain_element_item").SerpApiAdsDomainElementItem.from_dict(obj)

        raise ValueError("BaseSerpElementItem failed to lookup discriminator value from " +
                         json.dumps(obj) + ". Discriminator property name: " + cls.__discriminator_property_name +
                         ", mapping: " + json.dumps(cls.__discriminator_value_class_map))