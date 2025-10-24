from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class ProductKeywordIntersectionsAmazonDataforseoLabsAvailableFiltersAmazonInfo(BaseModel):
    """
    ProductKeywordIntersectionsAmazonDataforseoLabsAvailableFiltersAmazonInfo
    """ # noqa: E501
    keyword_data_keyword: Optional[StrictStr] = Field(default=None, description=r"")
    keyword_data_location_code: Optional[StrictStr] = Field(default=None, description=r"")
    keyword_data_language_code: Optional[StrictStr] = Field(default=None, description=r"")
    keyword_data_keyword_info_last_updated_time: Optional[StrictStr] = Field(default=None, description=r"")
    keyword_data_keyword_info_search_volume: Optional[StrictStr] = Field(default=None, description=r"")
    intersection_result_key_type: Optional[StrictStr] = Field(default=None, description=r"type of element")
    intersection_result_key_rank_group: Optional[StrictStr] = Field(default=None, description=r"")
    intersection_result_key_rank_absolute: Optional[StrictStr] = Field(default=None, description=r"")
    intersection_result_key_xpath: Optional[StrictStr] = Field(default=None, description=r"")
    intersection_result_key_domain: Optional[StrictStr] = Field(default=None, description=r"")
    intersection_result_key_title: Optional[StrictStr] = Field(default=None, description=r"")
    intersection_result_key_url: Optional[StrictStr] = Field(default=None, description=r"")
    intersection_result_key_asin: Optional[StrictStr] = Field(default=None, description=r"")
    intersection_result_key_image_url: Optional[StrictStr] = Field(default=None, description=r"")
    intersection_result_key_price_from: Optional[StrictStr] = Field(default=None, description=r"")
    intersection_result_key_price_to: Optional[StrictStr] = Field(default=None, description=r"")
    intersection_result_key_currency: Optional[StrictStr] = Field(default=None, description=r"")
    intersection_result_key_is_best_seller: Optional[StrictStr] = Field(default=None, description=r"")
    intersection_result_key_is_amazon_choice: Optional[StrictStr] = Field(default=None, description=r"")
    intersection_result_key_rating_rating_type: Optional[StrictStr] = Field(default=None, description=r"")
    intersection_result_key_rating_value: Optional[StrictStr] = Field(default=None, description=r"")
    intersection_result_key_rating_votes_count: Optional[StrictStr] = Field(default=None, description=r"")
    intersection_result_key_rating_rating_max: Optional[StrictInt] = Field(default=None, description=r"the maximum value for a rating_type")
    intersection_result_key_delivery_info_delivery_message: Optional[StrictStr] = Field(default=None, description=r"")
    intersection_result_key_delivery_info_delivery_price_current: Optional[StrictStr] = Field(default=None, description=r"")
    intersection_result_key_delivery_info_delivery_price_regular: Optional[StrictStr] = Field(default=None, description=r"")
    intersection_result_key_delivery_info_delivery_price_max_value: Optional[StrictStr] = Field(default=None, description=r"")
    intersection_result_key_delivery_info_delivery_price_currency: Optional[StrictStr] = Field(default=None, description=r"")
    intersection_result_key_delivery_info_delivery_price_is_price_range: Optional[StrictStr] = Field(default=None, description=r"")
    intersection_result_key_delivery_info_delivery_price_displayed_price: Optional[StrictStr] = Field(default=None, description=r"")
    __properties: ClassVar[List[str]] = [
        "keyword_data.keyword", 
        "keyword_data.location_code", 
        "keyword_data.language_code", 
        "keyword_data.keyword_info.last_updated_time", 
        "keyword_data.keyword_info.search_volume", 
        "intersection_result.$key.type", 
        "intersection_result.$key.rank_group", 
        "intersection_result.$key.rank_absolute", 
        "intersection_result.$key.xpath", 
        "intersection_result.$key.domain", 
        "intersection_result.$key.title", 
        "intersection_result.$key.url", 
        "intersection_result.$key.asin", 
        "intersection_result.$key.image_url", 
        "intersection_result.$key.price_from", 
        "intersection_result.$key.price_to", 
        "intersection_result.$key.currency", 
        "intersection_result.$key.is_best_seller", 
        "intersection_result.$key.is_amazon_choice", 
        "intersection_result.$key.rating.rating_type", 
        "intersection_result.$key.rating.value", 
        "intersection_result.$key.rating.votes_count", 
        "intersection_result.$key.rating.rating_max", 
        "intersection_result.$key.delivery_info.delivery_message", 
        "intersection_result.$key.delivery_info.delivery_price.current", 
        "intersection_result.$key.delivery_info.delivery_price.regular", 
        "intersection_result.$key.delivery_info.delivery_price.max_value", 
        "intersection_result.$key.delivery_info.delivery_price.currency", 
        "intersection_result.$key.delivery_info.delivery_price.is_price_range", 
        "intersection_result.$key.delivery_info.delivery_price.displayed_price", 
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
        _dict['keyword_data.location_code'] = self.keyword_data_location_code
        _dict['keyword_data.language_code'] = self.keyword_data_language_code
        _dict['keyword_data.keyword_info.last_updated_time'] = self.keyword_data_keyword_info_last_updated_time
        _dict['keyword_data.keyword_info.search_volume'] = self.keyword_data_keyword_info_search_volume
        _dict['intersection_result.$key.type'] = self.intersection_result_key_type
        _dict['intersection_result.$key.rank_group'] = self.intersection_result_key_rank_group
        _dict['intersection_result.$key.rank_absolute'] = self.intersection_result_key_rank_absolute
        _dict['intersection_result.$key.xpath'] = self.intersection_result_key_xpath
        _dict['intersection_result.$key.domain'] = self.intersection_result_key_domain
        _dict['intersection_result.$key.title'] = self.intersection_result_key_title
        _dict['intersection_result.$key.url'] = self.intersection_result_key_url
        _dict['intersection_result.$key.asin'] = self.intersection_result_key_asin
        _dict['intersection_result.$key.image_url'] = self.intersection_result_key_image_url
        _dict['intersection_result.$key.price_from'] = self.intersection_result_key_price_from
        _dict['intersection_result.$key.price_to'] = self.intersection_result_key_price_to
        _dict['intersection_result.$key.currency'] = self.intersection_result_key_currency
        _dict['intersection_result.$key.is_best_seller'] = self.intersection_result_key_is_best_seller
        _dict['intersection_result.$key.is_amazon_choice'] = self.intersection_result_key_is_amazon_choice
        _dict['intersection_result.$key.rating.rating_type'] = self.intersection_result_key_rating_rating_type
        _dict['intersection_result.$key.rating.value'] = self.intersection_result_key_rating_value
        _dict['intersection_result.$key.rating.votes_count'] = self.intersection_result_key_rating_votes_count
        _dict['intersection_result.$key.rating.rating_max'] = self.intersection_result_key_rating_rating_max
        _dict['intersection_result.$key.delivery_info.delivery_message'] = self.intersection_result_key_delivery_info_delivery_message
        _dict['intersection_result.$key.delivery_info.delivery_price.current'] = self.intersection_result_key_delivery_info_delivery_price_current
        _dict['intersection_result.$key.delivery_info.delivery_price.regular'] = self.intersection_result_key_delivery_info_delivery_price_regular
        _dict['intersection_result.$key.delivery_info.delivery_price.max_value'] = self.intersection_result_key_delivery_info_delivery_price_max_value
        _dict['intersection_result.$key.delivery_info.delivery_price.currency'] = self.intersection_result_key_delivery_info_delivery_price_currency
        _dict['intersection_result.$key.delivery_info.delivery_price.is_price_range'] = self.intersection_result_key_delivery_info_delivery_price_is_price_range
        _dict['intersection_result.$key.delivery_info.delivery_price.displayed_price'] = self.intersection_result_key_delivery_info_delivery_price_displayed_price
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "keyword_data_keyword": obj.get("keyword_data.keyword"),
            "keyword_data_location_code": obj.get("keyword_data.location_code"),
            "keyword_data_language_code": obj.get("keyword_data.language_code"),
            "keyword_data_keyword_info_last_updated_time": obj.get("keyword_data.keyword_info.last_updated_time"),
            "keyword_data_keyword_info_search_volume": obj.get("keyword_data.keyword_info.search_volume"),
            "intersection_result_key_type": obj.get("intersection_result.$key.type"),
            "intersection_result_key_rank_group": obj.get("intersection_result.$key.rank_group"),
            "intersection_result_key_rank_absolute": obj.get("intersection_result.$key.rank_absolute"),
            "intersection_result_key_xpath": obj.get("intersection_result.$key.xpath"),
            "intersection_result_key_domain": obj.get("intersection_result.$key.domain"),
            "intersection_result_key_title": obj.get("intersection_result.$key.title"),
            "intersection_result_key_url": obj.get("intersection_result.$key.url"),
            "intersection_result_key_asin": obj.get("intersection_result.$key.asin"),
            "intersection_result_key_image_url": obj.get("intersection_result.$key.image_url"),
            "intersection_result_key_price_from": obj.get("intersection_result.$key.price_from"),
            "intersection_result_key_price_to": obj.get("intersection_result.$key.price_to"),
            "intersection_result_key_currency": obj.get("intersection_result.$key.currency"),
            "intersection_result_key_is_best_seller": obj.get("intersection_result.$key.is_best_seller"),
            "intersection_result_key_is_amazon_choice": obj.get("intersection_result.$key.is_amazon_choice"),
            "intersection_result_key_rating_rating_type": obj.get("intersection_result.$key.rating.rating_type"),
            "intersection_result_key_rating_value": obj.get("intersection_result.$key.rating.value"),
            "intersection_result_key_rating_votes_count": obj.get("intersection_result.$key.rating.votes_count"),
            "intersection_result_key_rating_rating_max": obj.get("intersection_result.$key.rating.rating_max"),
            "intersection_result_key_delivery_info_delivery_message": obj.get("intersection_result.$key.delivery_info.delivery_message"),
            "intersection_result_key_delivery_info_delivery_price_current": obj.get("intersection_result.$key.delivery_info.delivery_price.current"),
            "intersection_result_key_delivery_info_delivery_price_regular": obj.get("intersection_result.$key.delivery_info.delivery_price.regular"),
            "intersection_result_key_delivery_info_delivery_price_max_value": obj.get("intersection_result.$key.delivery_info.delivery_price.max_value"),
            "intersection_result_key_delivery_info_delivery_price_currency": obj.get("intersection_result.$key.delivery_info.delivery_price.currency"),
            "intersection_result_key_delivery_info_delivery_price_is_price_range": obj.get("intersection_result.$key.delivery_info.delivery_price.is_price_range"),
            "intersection_result_key_delivery_info_delivery_price_displayed_price": obj.get("intersection_result.$key.delivery_info.delivery_price.displayed_price"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj