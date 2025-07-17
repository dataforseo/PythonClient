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
    from dataforseo_client.models.serp_api_google_finance_asset_pair_element_item import SerpApiGoogleFinanceAssetPairElementItem;
    from dataforseo_client.models.serp_api_google_finance_market_instrument_element_item import SerpApiGoogleFinanceMarketInstrumentElementItem;
    from dataforseo_client.models.serp_api_google_finance_market_index_element_item import SerpApiGoogleFinanceMarketIndexElementItem;



class BaseSerpApiGoogleFinanceTickerSearchElementItem(BaseModel):
    """
    BaseSerpApiGoogleFinanceTickerSearchElementItem
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    rank_group: Optional[StrictInt] = Field(default=None, description="group rank in SERP. position within a group of elements with identical type values. positions of elements with different type values are omitted from rank_group")
    rank_absolute: Optional[StrictInt] = Field(default=None, description="absolute rank in SERP. absolute position among all the elements in SERP")
    identifier: Optional[StrictStr] = Field(default=None, description="identifier of the element. full identifier of the element that consists from ticker and market_identifier. example: PX1:INDEXDB")
    displayed_name: Optional[StrictStr] = Field(default=None, description="name of the market index as displayed on Google Finance. example: CAC 40")
    url: Optional[StrictStr] = Field(default=None, description="URL to the page of the market index on Google Finance")
    location: Optional[StrictStr] = Field(default=None, description="location of the market index. example: Europe/Paris")
    trend: Optional[StrictStr] = Field(default=None, description="growth trend of the market index. possible values: up, down, stable")
    timestamp: Optional[StrictStr] = Field(default=None, description="date and time of the value readout. in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”. example:. 2025-02-10 09:40:00 +00:00")
    percentage_delta: Optional[StrictFloat] = Field(default=None, description="percentage of change in value of the market index")
    __properties: ClassVar[List[str]] = [
        "type", 
        "rank_group", 
        "rank_absolute", 
        "identifier", 
        "displayed_name", 
        "url", 
        "location", 
        "trend", 
        "timestamp", 
        "percentage_delta", 
        ]
    __discriminator_property_name: ClassVar[str] = 'type'
    __discriminator_value_class_map: ClassVar[Dict[str, str]] = {
        'google_finance_asset_pair': 'SerpApiGoogleFinanceAssetPairElementItem',
        'google_finance_market_instrument': 'SerpApiGoogleFinanceMarketInstrumentElementItem',
        'google_finance_market_index': 'SerpApiGoogleFinanceMarketIndexElementItem',
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
        _dict['identifier'] = self.identifier
        _dict['displayed_name'] = self.displayed_name
        _dict['url'] = self.url
        _dict['location'] = self.location
        _dict['trend'] = self.trend
        _dict['timestamp'] = self.timestamp
        _dict['percentage_delta'] = self.percentage_delta
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
        SerpApiGoogleFinanceAssetPairElementItem, 
        SerpApiGoogleFinanceMarketInstrumentElementItem, 
        SerpApiGoogleFinanceMarketIndexElementItem
    ]]:
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        
        if object_type == 'SerpApiGoogleFinanceAssetPairElementItem':
            return import_module("dataforseo_client.models.serp_api_google_finance_asset_pair_element_item").SerpApiGoogleFinanceAssetPairElementItem.from_dict(obj)
        if object_type == 'SerpApiGoogleFinanceMarketInstrumentElementItem':
            return import_module("dataforseo_client.models.serp_api_google_finance_market_instrument_element_item").SerpApiGoogleFinanceMarketInstrumentElementItem.from_dict(obj)
        if object_type == 'SerpApiGoogleFinanceMarketIndexElementItem':
            return import_module("dataforseo_client.models.serp_api_google_finance_market_index_element_item").SerpApiGoogleFinanceMarketIndexElementItem.from_dict(obj)

        raise ValueError("BaseSerpElementItem failed to lookup discriminator value from " +
                         json.dumps(obj) + ". Discriminator property name: " + cls.__discriminator_property_name +
                         ", mapping: " + json.dumps(cls.__discriminator_value_class_map))