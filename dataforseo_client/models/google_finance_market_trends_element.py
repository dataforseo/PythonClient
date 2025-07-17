from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.base_serp_api_google_finance_element_item import BaseSerpApiGoogleFinanceElementItem
from dataforseo_client.models.google_finance_news_element import GoogleFinanceNewsElement



class GoogleFinanceMarketTrendsElement(BaseModel):
    """
    GoogleFinanceMarketTrendsElement
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    quote: Optional[BaseSerpApiGoogleFinanceElementItem] = Field(default=None, description="object of items. array contains the following type of items: google_finance_asset_pair_element, google_finance_market_instrument_element, google_finance_market_index_element")
    news: Optional[List[Optional[GoogleFinanceNewsElement]]] = Field(default=None, description="array of items. array contains the following type of items: google_finance_news_element")
    __properties: ClassVar[List[str]] = [
        "type", 
        "quote", 
        "news", 
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

        _dict['type'] = self.type
        _dict['quote'] = self.quote.to_dict() if self.quote else None
        news_items = []
        if self.news:
            for _item in self.news:
                if _item:
                    news_items.append(_item.to_dict())
            _dict['news'] = news_items
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "quote": BaseSerpApiGoogleFinanceElementItem.from_dict(obj["quote"]) if obj.get("quote") is not None else None,
            "news": [GoogleFinanceNewsElement.from_dict(_item) for _item in obj["news"]] if obj.get("news") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj