from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class DataforseoLabsAvailableFiltersAmazonInfo(BaseModel):
    """
    DataforseoLabsAvailableFiltersAmazonInfo
    """ # noqa: E501
    keyword_data_keyword: Optional[StrictStr] = Field(default=None, description=r"")
    keyword_data_keyword_info_last_updated_time: Optional[StrictStr] = Field(default=None, description=r"")
    keyword_data_keyword_info_search_volume: Optional[StrictStr] = Field(default=None, description=r"")
    ranked_serp_element_serp_item_type: Optional[StrictStr] = Field(default=None, description=r"type of element")
    ranked_serp_element_serp_item_rank_group: Optional[StrictStr] = Field(default=None, description=r"")
    ranked_serp_element_serp_item_rank_absolute: Optional[StrictStr] = Field(default=None, description=r"")
    ranked_serp_element_serp_item_xpath: Optional[StrictStr] = Field(default=None, description=r"")
    ranked_serp_element_serp_item_domain: Optional[StrictStr] = Field(default=None, description=r"")
    ranked_serp_element_serp_item_title: Optional[StrictStr] = Field(default=None, description=r"")
    ranked_serp_element_serp_item_url: Optional[StrictStr] = Field(default=None, description=r"")
    ranked_serp_element_serp_item_asin: Optional[StrictStr] = Field(default=None, description=r"")
    ranked_serp_element_serp_item_image_url: Optional[StrictStr] = Field(default=None, description=r"")
    ranked_serp_element_serp_item_price_from: Optional[StrictStr] = Field(default=None, description=r"")
    ranked_serp_element_serp_item_price_to: Optional[StrictStr] = Field(default=None, description=r"")
    ranked_serp_element_serp_item_currency: Optional[StrictStr] = Field(default=None, description=r"")
    ranked_serp_element_serp_item_is_best_seller: Optional[StrictStr] = Field(default=None, description=r"")
    ranked_serp_element_serp_item_is_amazon_choice: Optional[StrictStr] = Field(default=None, description=r"")
    ranked_serp_element_serp_item_rating_rating_type: Optional[StrictStr] = Field(default=None, description=r"")
    ranked_serp_element_serp_item_rating_value: Optional[StrictStr] = Field(default=None, description=r"")
    ranked_serp_element_serp_item_rating_votes_count: Optional[StrictStr] = Field(default=None, description=r"")
    ranked_serp_element_serp_item_rating_rating_max: Optional[StrictInt] = Field(default=None, description=r"the maximum value for a rating_type")
    ranked_serp_element_serp_item_delivery_info_delivery_date_from: Optional[StrictStr] = Field(default=None, description=r"")
    ranked_serp_element_serp_item_delivery_info_delivery_date_to: Optional[StrictStr] = Field(default=None, description=r"")
    ranked_serp_element_serp_item_delivery_info_fastest_delivery_date_from: Optional[StrictStr] = Field(default=None, description=r"")
    ranked_serp_element_serp_item_delivery_info_fastest_delivery_date_to: Optional[StrictStr] = Field(default=None, description=r"")
    ranked_serp_element_serp_item_delivery_info_delivery_message: Optional[StrictStr] = Field(default=None, description=r"")
    ranked_serp_element_serp_item_delivery_info_delivery_price_current: Optional[StrictStr] = Field(default=None, description=r"")
    ranked_serp_element_serp_item_delivery_info_delivery_price_regular: Optional[StrictStr] = Field(default=None, description=r"")
    ranked_serp_element_serp_item_delivery_info_delivery_price_max_value: Optional[StrictStr] = Field(default=None, description=r"")
    ranked_serp_element_serp_item_delivery_info_delivery_price_currency: Optional[StrictStr] = Field(default=None, description=r"")
    ranked_serp_element_serp_item_delivery_info_delivery_price_is_price_range: Optional[StrictStr] = Field(default=None, description=r"")
    ranked_serp_element_serp_item_delivery_info_delivery_price_displayed_price: Optional[StrictStr] = Field(default=None, description=r"")
    ranked_serp_element_check_url: Optional[StrictStr] = Field(default=None, description=r"")
    ranked_serp_element_serp_item_types: Optional[StrictStr] = Field(default=None, description=r"")
    ranked_serp_element_se_results_count: Optional[StrictStr] = Field(default=None, description=r"")
    ranked_serp_element_last_updated_time: Optional[StrictStr] = Field(default=None, description=r"")
    ranked_serp_element_previous_updated_time: Optional[StrictStr] = Field(default=None, description=r"")
    __properties: ClassVar[List[str]] = [
        "keyword_data.keyword", 
        "keyword_data.keyword_info.last_updated_time", 
        "keyword_data.keyword_info.search_volume", 
        "ranked_serp_element.serp_item.type", 
        "ranked_serp_element.serp_item.rank_group", 
        "ranked_serp_element.serp_item.rank_absolute", 
        "ranked_serp_element.serp_item.xpath", 
        "ranked_serp_element.serp_item.domain", 
        "ranked_serp_element.serp_item.title", 
        "ranked_serp_element.serp_item.url", 
        "ranked_serp_element.serp_item.asin", 
        "ranked_serp_element.serp_item.image_url", 
        "ranked_serp_element.serp_item.price_from", 
        "ranked_serp_element.serp_item.price_to", 
        "ranked_serp_element.serp_item.currency", 
        "ranked_serp_element.serp_item.is_best_seller", 
        "ranked_serp_element.serp_item.is_amazon_choice", 
        "ranked_serp_element.serp_item.rating.rating_type", 
        "ranked_serp_element.serp_item.rating.value", 
        "ranked_serp_element.serp_item.rating.votes_count", 
        "ranked_serp_element.serp_item.rating.rating_max", 
        "ranked_serp_element.serp_item.delivery_info.delivery_date_from", 
        "ranked_serp_element.serp_item.delivery_info.delivery_date_to", 
        "ranked_serp_element.serp_item.delivery_info.fastest_delivery_date_from", 
        "ranked_serp_element.serp_item.delivery_info.fastest_delivery_date_to", 
        "ranked_serp_element.serp_item.delivery_info.delivery_message", 
        "ranked_serp_element.serp_item.delivery_info.delivery_price.current", 
        "ranked_serp_element.serp_item.delivery_info.delivery_price.regular", 
        "ranked_serp_element.serp_item.delivery_info.delivery_price.max_value", 
        "ranked_serp_element.serp_item.delivery_info.delivery_price.currency", 
        "ranked_serp_element.serp_item.delivery_info.delivery_price.is_price_range", 
        "ranked_serp_element.serp_item.delivery_info.delivery_price.displayed_price", 
        "ranked_serp_element.check_url", 
        "ranked_serp_element.serp_item_types", 
        "ranked_serp_element.se_results_count", 
        "ranked_serp_element.last_updated_time", 
        "ranked_serp_element.previous_updated_time", 
        ]

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

        _dict['keyword_data.keyword'] = self.keyword_data_keyword
        _dict['keyword_data.keyword_info.last_updated_time'] = self.keyword_data_keyword_info_last_updated_time
        _dict['keyword_data.keyword_info.search_volume'] = self.keyword_data_keyword_info_search_volume
        _dict['ranked_serp_element.serp_item.type'] = self.ranked_serp_element_serp_item_type
        _dict['ranked_serp_element.serp_item.rank_group'] = self.ranked_serp_element_serp_item_rank_group
        _dict['ranked_serp_element.serp_item.rank_absolute'] = self.ranked_serp_element_serp_item_rank_absolute
        _dict['ranked_serp_element.serp_item.xpath'] = self.ranked_serp_element_serp_item_xpath
        _dict['ranked_serp_element.serp_item.domain'] = self.ranked_serp_element_serp_item_domain
        _dict['ranked_serp_element.serp_item.title'] = self.ranked_serp_element_serp_item_title
        _dict['ranked_serp_element.serp_item.url'] = self.ranked_serp_element_serp_item_url
        _dict['ranked_serp_element.serp_item.asin'] = self.ranked_serp_element_serp_item_asin
        _dict['ranked_serp_element.serp_item.image_url'] = self.ranked_serp_element_serp_item_image_url
        _dict['ranked_serp_element.serp_item.price_from'] = self.ranked_serp_element_serp_item_price_from
        _dict['ranked_serp_element.serp_item.price_to'] = self.ranked_serp_element_serp_item_price_to
        _dict['ranked_serp_element.serp_item.currency'] = self.ranked_serp_element_serp_item_currency
        _dict['ranked_serp_element.serp_item.is_best_seller'] = self.ranked_serp_element_serp_item_is_best_seller
        _dict['ranked_serp_element.serp_item.is_amazon_choice'] = self.ranked_serp_element_serp_item_is_amazon_choice
        _dict['ranked_serp_element.serp_item.rating.rating_type'] = self.ranked_serp_element_serp_item_rating_rating_type
        _dict['ranked_serp_element.serp_item.rating.value'] = self.ranked_serp_element_serp_item_rating_value
        _dict['ranked_serp_element.serp_item.rating.votes_count'] = self.ranked_serp_element_serp_item_rating_votes_count
        _dict['ranked_serp_element.serp_item.rating.rating_max'] = self.ranked_serp_element_serp_item_rating_rating_max
        _dict['ranked_serp_element.serp_item.delivery_info.delivery_date_from'] = self.ranked_serp_element_serp_item_delivery_info_delivery_date_from
        _dict['ranked_serp_element.serp_item.delivery_info.delivery_date_to'] = self.ranked_serp_element_serp_item_delivery_info_delivery_date_to
        _dict['ranked_serp_element.serp_item.delivery_info.fastest_delivery_date_from'] = self.ranked_serp_element_serp_item_delivery_info_fastest_delivery_date_from
        _dict['ranked_serp_element.serp_item.delivery_info.fastest_delivery_date_to'] = self.ranked_serp_element_serp_item_delivery_info_fastest_delivery_date_to
        _dict['ranked_serp_element.serp_item.delivery_info.delivery_message'] = self.ranked_serp_element_serp_item_delivery_info_delivery_message
        _dict['ranked_serp_element.serp_item.delivery_info.delivery_price.current'] = self.ranked_serp_element_serp_item_delivery_info_delivery_price_current
        _dict['ranked_serp_element.serp_item.delivery_info.delivery_price.regular'] = self.ranked_serp_element_serp_item_delivery_info_delivery_price_regular
        _dict['ranked_serp_element.serp_item.delivery_info.delivery_price.max_value'] = self.ranked_serp_element_serp_item_delivery_info_delivery_price_max_value
        _dict['ranked_serp_element.serp_item.delivery_info.delivery_price.currency'] = self.ranked_serp_element_serp_item_delivery_info_delivery_price_currency
        _dict['ranked_serp_element.serp_item.delivery_info.delivery_price.is_price_range'] = self.ranked_serp_element_serp_item_delivery_info_delivery_price_is_price_range
        _dict['ranked_serp_element.serp_item.delivery_info.delivery_price.displayed_price'] = self.ranked_serp_element_serp_item_delivery_info_delivery_price_displayed_price
        _dict['ranked_serp_element.check_url'] = self.ranked_serp_element_check_url
        _dict['ranked_serp_element.serp_item_types'] = self.ranked_serp_element_serp_item_types
        _dict['ranked_serp_element.se_results_count'] = self.ranked_serp_element_se_results_count
        _dict['ranked_serp_element.last_updated_time'] = self.ranked_serp_element_last_updated_time
        _dict['ranked_serp_element.previous_updated_time'] = self.ranked_serp_element_previous_updated_time
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "keyword_data_keyword": obj.get("keyword_data.keyword"),
            "keyword_data_keyword_info_last_updated_time": obj.get("keyword_data.keyword_info.last_updated_time"),
            "keyword_data_keyword_info_search_volume": obj.get("keyword_data.keyword_info.search_volume"),
            "ranked_serp_element_serp_item_type": obj.get("ranked_serp_element.serp_item.type"),
            "ranked_serp_element_serp_item_rank_group": obj.get("ranked_serp_element.serp_item.rank_group"),
            "ranked_serp_element_serp_item_rank_absolute": obj.get("ranked_serp_element.serp_item.rank_absolute"),
            "ranked_serp_element_serp_item_xpath": obj.get("ranked_serp_element.serp_item.xpath"),
            "ranked_serp_element_serp_item_domain": obj.get("ranked_serp_element.serp_item.domain"),
            "ranked_serp_element_serp_item_title": obj.get("ranked_serp_element.serp_item.title"),
            "ranked_serp_element_serp_item_url": obj.get("ranked_serp_element.serp_item.url"),
            "ranked_serp_element_serp_item_asin": obj.get("ranked_serp_element.serp_item.asin"),
            "ranked_serp_element_serp_item_image_url": obj.get("ranked_serp_element.serp_item.image_url"),
            "ranked_serp_element_serp_item_price_from": obj.get("ranked_serp_element.serp_item.price_from"),
            "ranked_serp_element_serp_item_price_to": obj.get("ranked_serp_element.serp_item.price_to"),
            "ranked_serp_element_serp_item_currency": obj.get("ranked_serp_element.serp_item.currency"),
            "ranked_serp_element_serp_item_is_best_seller": obj.get("ranked_serp_element.serp_item.is_best_seller"),
            "ranked_serp_element_serp_item_is_amazon_choice": obj.get("ranked_serp_element.serp_item.is_amazon_choice"),
            "ranked_serp_element_serp_item_rating_rating_type": obj.get("ranked_serp_element.serp_item.rating.rating_type"),
            "ranked_serp_element_serp_item_rating_value": obj.get("ranked_serp_element.serp_item.rating.value"),
            "ranked_serp_element_serp_item_rating_votes_count": obj.get("ranked_serp_element.serp_item.rating.votes_count"),
            "ranked_serp_element_serp_item_rating_rating_max": obj.get("ranked_serp_element.serp_item.rating.rating_max"),
            "ranked_serp_element_serp_item_delivery_info_delivery_date_from": obj.get("ranked_serp_element.serp_item.delivery_info.delivery_date_from"),
            "ranked_serp_element_serp_item_delivery_info_delivery_date_to": obj.get("ranked_serp_element.serp_item.delivery_info.delivery_date_to"),
            "ranked_serp_element_serp_item_delivery_info_fastest_delivery_date_from": obj.get("ranked_serp_element.serp_item.delivery_info.fastest_delivery_date_from"),
            "ranked_serp_element_serp_item_delivery_info_fastest_delivery_date_to": obj.get("ranked_serp_element.serp_item.delivery_info.fastest_delivery_date_to"),
            "ranked_serp_element_serp_item_delivery_info_delivery_message": obj.get("ranked_serp_element.serp_item.delivery_info.delivery_message"),
            "ranked_serp_element_serp_item_delivery_info_delivery_price_current": obj.get("ranked_serp_element.serp_item.delivery_info.delivery_price.current"),
            "ranked_serp_element_serp_item_delivery_info_delivery_price_regular": obj.get("ranked_serp_element.serp_item.delivery_info.delivery_price.regular"),
            "ranked_serp_element_serp_item_delivery_info_delivery_price_max_value": obj.get("ranked_serp_element.serp_item.delivery_info.delivery_price.max_value"),
            "ranked_serp_element_serp_item_delivery_info_delivery_price_currency": obj.get("ranked_serp_element.serp_item.delivery_info.delivery_price.currency"),
            "ranked_serp_element_serp_item_delivery_info_delivery_price_is_price_range": obj.get("ranked_serp_element.serp_item.delivery_info.delivery_price.is_price_range"),
            "ranked_serp_element_serp_item_delivery_info_delivery_price_displayed_price": obj.get("ranked_serp_element.serp_item.delivery_info.delivery_price.displayed_price"),
            "ranked_serp_element_check_url": obj.get("ranked_serp_element.check_url"),
            "ranked_serp_element_serp_item_types": obj.get("ranked_serp_element.serp_item_types"),
            "ranked_serp_element_se_results_count": obj.get("ranked_serp_element.se_results_count"),
            "ranked_serp_element_last_updated_time": obj.get("ranked_serp_element.last_updated_time"),
            "ranked_serp_element_previous_updated_time": obj.get("ranked_serp_element.previous_updated_time"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj