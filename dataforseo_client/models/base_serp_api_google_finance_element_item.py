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
    from dataforseo_client.models.serp_api_google_finance_asset_pair_element_element_item import SerpApiGoogleFinanceAssetPairElementElementItem;
    from dataforseo_client.models.serp_api_google_finance_market_index_element_element_item import SerpApiGoogleFinanceMarketIndexElementElementItem;
    from dataforseo_client.models.serp_api_google_finance_market_instrument_element_element_item import SerpApiGoogleFinanceMarketInstrumentElementElementItem;
    from dataforseo_client.models.serp_api_google_finance_hero_groups_element_item import SerpApiGoogleFinanceHeroGroupsElementItem;
    from dataforseo_client.models.serp_api_google_finance_interested_element_item import SerpApiGoogleFinanceInterestedElementItem;
    from dataforseo_client.models.serp_api_google_finance_news_element_item import SerpApiGoogleFinanceNewsElementItem;
    from dataforseo_client.models.serp_api_google_finance_earnings_calendar_element_item import SerpApiGoogleFinanceEarningsCalendarElementItem;
    from dataforseo_client.models.serp_api_google_finance_most_followed_element_item import SerpApiGoogleFinanceMostFollowedElementItem;
    from dataforseo_client.models.serp_api_google_finance_market_trends_element_item import SerpApiGoogleFinanceMarketTrendsElementItem;
    from dataforseo_client.models.serp_api_google_finance_people_also_search_element_item import SerpApiGoogleFinancePeopleAlsoSearchElementItem;
    from dataforseo_client.models.serp_api_google_finance_explore_market_trends_element_item import SerpApiGoogleFinanceExploreMarketTrendsElementItem;
    from dataforseo_client.models.serp_api_google_finance_quote_element_item import SerpApiGoogleFinanceQuoteElementItem;
    from dataforseo_client.models.serp_api_google_finance_compare_to_element_item import SerpApiGoogleFinanceCompareToElementItem;
    from dataforseo_client.models.serp_api_google_finance_financial_element_item import SerpApiGoogleFinanceFinancialElementItem;
    from dataforseo_client.models.serp_api_google_finance_futures_chain_element_item import SerpApiGoogleFinanceFuturesChainElementItem;
    from dataforseo_client.models.serp_api_google_finance_details_element_item import SerpApiGoogleFinanceDetailsElementItem;
    from dataforseo_client.models.serp_api_google_finance_about_element_item import SerpApiGoogleFinanceAboutElementItem;



class BaseSerpApiGoogleFinanceElementItem(BaseModel):
    """
    BaseSerpApiGoogleFinanceElementItem
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    __properties: ClassVar[List[str]] = [
        "type", 
        ]
    __discriminator_property_name: ClassVar[str] = 'type'
    __discriminator_value_class_map: ClassVar[Dict[str, str]] = {
        'google_finance_asset_pair_element': 'SerpApiGoogleFinanceAssetPairElementElementItem',
        'google_finance_market_index_element': 'SerpApiGoogleFinanceMarketIndexElementElementItem',
        'google_finance_market_instrument_element': 'SerpApiGoogleFinanceMarketInstrumentElementElementItem',
        'google_finance_hero_groups': 'SerpApiGoogleFinanceHeroGroupsElementItem',
        'google_finance_interested': 'SerpApiGoogleFinanceInterestedElementItem',
        'google_finance_news': 'SerpApiGoogleFinanceNewsElementItem',
        'google_finance_earnings_calendar': 'SerpApiGoogleFinanceEarningsCalendarElementItem',
        'google_finance_most_followed': 'SerpApiGoogleFinanceMostFollowedElementItem',
        'google_finance_market_trends': 'SerpApiGoogleFinanceMarketTrendsElementItem',
        'google_finance_people_also_search': 'SerpApiGoogleFinancePeopleAlsoSearchElementItem',
        'google_finance_explore_market_trends': 'SerpApiGoogleFinanceExploreMarketTrendsElementItem',
        'google_finance_quote': 'SerpApiGoogleFinanceQuoteElementItem',
        'google_finance_compare_to': 'SerpApiGoogleFinanceCompareToElementItem',
        'google_finance_financial': 'SerpApiGoogleFinanceFinancialElementItem',
        'google_finance_futures_chain': 'SerpApiGoogleFinanceFuturesChainElementItem',
        'google_finance_details': 'SerpApiGoogleFinanceDetailsElementItem',
        'google_finance_about': 'SerpApiGoogleFinanceAboutElementItem',
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
        SerpApiGoogleFinanceAssetPairElementElementItem, 
        SerpApiGoogleFinanceMarketIndexElementElementItem, 
        SerpApiGoogleFinanceMarketInstrumentElementElementItem, 
        SerpApiGoogleFinanceHeroGroupsElementItem, 
        SerpApiGoogleFinanceInterestedElementItem, 
        SerpApiGoogleFinanceNewsElementItem, 
        SerpApiGoogleFinanceEarningsCalendarElementItem, 
        SerpApiGoogleFinanceMostFollowedElementItem, 
        SerpApiGoogleFinanceMarketTrendsElementItem, 
        SerpApiGoogleFinancePeopleAlsoSearchElementItem, 
        SerpApiGoogleFinanceExploreMarketTrendsElementItem, 
        SerpApiGoogleFinanceQuoteElementItem, 
        SerpApiGoogleFinanceCompareToElementItem, 
        SerpApiGoogleFinanceFinancialElementItem, 
        SerpApiGoogleFinanceFuturesChainElementItem, 
        SerpApiGoogleFinanceDetailsElementItem, 
        SerpApiGoogleFinanceAboutElementItem
    ]]:
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        
        if object_type == 'SerpApiGoogleFinanceAssetPairElementElementItem':
            return import_module("dataforseo_client.models.serp_api_google_finance_asset_pair_element_element_item").SerpApiGoogleFinanceAssetPairElementElementItem.from_dict(obj)
        if object_type == 'SerpApiGoogleFinanceMarketIndexElementElementItem':
            return import_module("dataforseo_client.models.serp_api_google_finance_market_index_element_element_item").SerpApiGoogleFinanceMarketIndexElementElementItem.from_dict(obj)
        if object_type == 'SerpApiGoogleFinanceMarketInstrumentElementElementItem':
            return import_module("dataforseo_client.models.serp_api_google_finance_market_instrument_element_element_item").SerpApiGoogleFinanceMarketInstrumentElementElementItem.from_dict(obj)
        if object_type == 'SerpApiGoogleFinanceHeroGroupsElementItem':
            return import_module("dataforseo_client.models.serp_api_google_finance_hero_groups_element_item").SerpApiGoogleFinanceHeroGroupsElementItem.from_dict(obj)
        if object_type == 'SerpApiGoogleFinanceInterestedElementItem':
            return import_module("dataforseo_client.models.serp_api_google_finance_interested_element_item").SerpApiGoogleFinanceInterestedElementItem.from_dict(obj)
        if object_type == 'SerpApiGoogleFinanceNewsElementItem':
            return import_module("dataforseo_client.models.serp_api_google_finance_news_element_item").SerpApiGoogleFinanceNewsElementItem.from_dict(obj)
        if object_type == 'SerpApiGoogleFinanceEarningsCalendarElementItem':
            return import_module("dataforseo_client.models.serp_api_google_finance_earnings_calendar_element_item").SerpApiGoogleFinanceEarningsCalendarElementItem.from_dict(obj)
        if object_type == 'SerpApiGoogleFinanceMostFollowedElementItem':
            return import_module("dataforseo_client.models.serp_api_google_finance_most_followed_element_item").SerpApiGoogleFinanceMostFollowedElementItem.from_dict(obj)
        if object_type == 'SerpApiGoogleFinanceMarketTrendsElementItem':
            return import_module("dataforseo_client.models.serp_api_google_finance_market_trends_element_item").SerpApiGoogleFinanceMarketTrendsElementItem.from_dict(obj)
        if object_type == 'SerpApiGoogleFinancePeopleAlsoSearchElementItem':
            return import_module("dataforseo_client.models.serp_api_google_finance_people_also_search_element_item").SerpApiGoogleFinancePeopleAlsoSearchElementItem.from_dict(obj)
        if object_type == 'SerpApiGoogleFinanceExploreMarketTrendsElementItem':
            return import_module("dataforseo_client.models.serp_api_google_finance_explore_market_trends_element_item").SerpApiGoogleFinanceExploreMarketTrendsElementItem.from_dict(obj)
        if object_type == 'SerpApiGoogleFinanceQuoteElementItem':
            return import_module("dataforseo_client.models.serp_api_google_finance_quote_element_item").SerpApiGoogleFinanceQuoteElementItem.from_dict(obj)
        if object_type == 'SerpApiGoogleFinanceCompareToElementItem':
            return import_module("dataforseo_client.models.serp_api_google_finance_compare_to_element_item").SerpApiGoogleFinanceCompareToElementItem.from_dict(obj)
        if object_type == 'SerpApiGoogleFinanceFinancialElementItem':
            return import_module("dataforseo_client.models.serp_api_google_finance_financial_element_item").SerpApiGoogleFinanceFinancialElementItem.from_dict(obj)
        if object_type == 'SerpApiGoogleFinanceFuturesChainElementItem':
            return import_module("dataforseo_client.models.serp_api_google_finance_futures_chain_element_item").SerpApiGoogleFinanceFuturesChainElementItem.from_dict(obj)
        if object_type == 'SerpApiGoogleFinanceDetailsElementItem':
            return import_module("dataforseo_client.models.serp_api_google_finance_details_element_item").SerpApiGoogleFinanceDetailsElementItem.from_dict(obj)
        if object_type == 'SerpApiGoogleFinanceAboutElementItem':
            return import_module("dataforseo_client.models.serp_api_google_finance_about_element_item").SerpApiGoogleFinanceAboutElementItem.from_dict(obj)

        return None