from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.google_finance_market_trends_element import GoogleFinanceMarketTrendsElement



class SerpGoogleFinanceExploreAdvancedItem(BaseModel):
    """
    SerpGoogleFinanceExploreAdvancedItem
    """ # noqa: E501
    most_active: Optional[List[Optional[GoogleFinanceMarketTrendsElement]]] = Field(default=None, description="array of items. this array can take the following names: most_active, gainers, losers")
    gainers: Optional[List[Optional[GoogleFinanceMarketTrendsElement]]] = Field(default=None, description="")
    losers: Optional[List[Optional[GoogleFinanceMarketTrendsElement]]] = Field(default=None, description="")
    __properties: ClassVar[List[str]] = [
        "most_active", 
        "gainers", 
        "losers", 
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

        most_active_items = []
        if self.most_active:
            for _item in self.most_active:
                if _item:
                    most_active_items.append(_item.to_dict())
            _dict['most_active'] = most_active_items
        gainers_items = []
        if self.gainers:
            for _item in self.gainers:
                if _item:
                    gainers_items.append(_item.to_dict())
            _dict['gainers'] = gainers_items
        losers_items = []
        if self.losers:
            for _item in self.losers:
                if _item:
                    losers_items.append(_item.to_dict())
            _dict['losers'] = losers_items
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "most_active": [GoogleFinanceMarketTrendsElement.from_dict(_item) for _item in obj["most_active"]] if obj.get("most_active") is not None else None,
            "gainers": [GoogleFinanceMarketTrendsElement.from_dict(_item) for _item in obj["gainers"]] if obj.get("gainers") is not None else None,
            "losers": [GoogleFinanceMarketTrendsElement.from_dict(_item) for _item in obj["losers"]] if obj.get("losers") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj