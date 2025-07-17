from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.base_serp_api_google_finance_element_item import BaseSerpApiGoogleFinanceElementItem



class GoogleFinanceNewsElement(BaseModel):
    """
    GoogleFinanceNewsElement
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    title: Optional[StrictStr] = Field(default=None, description="title of the news article")
    url: Optional[StrictStr] = Field(default=None, description="URL to the page of the market index on Google Finance")
    source: Optional[StrictStr] = Field(default=None, description="name of the news source. name of the website where the news article is published")
    image_url: Optional[StrictStr] = Field(default=None, description="featured image URL. URL of the news article’s featured image")
    timestamp: Optional[StrictStr] = Field(default=None, description="date and time of the value readout. in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”. example:. 2025-02-10 09:40:00 +00:00")
    quotes: Optional[List[Optional[BaseSerpApiGoogleFinanceElementItem]]] = Field(default=None, description="market indexes quoted in the news article. information about market indexes quoted in the google_finance_news_element")
    __properties: ClassVar[List[str]] = [
        "type", 
        "title", 
        "url", 
        "source", 
        "image_url", 
        "timestamp", 
        "quotes", 
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
        _dict['title'] = self.title
        _dict['url'] = self.url
        _dict['source'] = self.source
        _dict['image_url'] = self.image_url
        _dict['timestamp'] = self.timestamp
        quotes_items = []
        if self.quotes:
            for _item in self.quotes:
                if _item:
                    quotes_items.append(_item.to_dict())
            _dict['quotes'] = quotes_items
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "title": obj.get("title"),
            "url": obj.get("url"),
            "source": obj.get("source"),
            "image_url": obj.get("image_url"),
            "timestamp": obj.get("timestamp"),
            "quotes": [BaseSerpApiGoogleFinanceElementItem.from_dict(_item) for _item in obj["quotes"]] if obj.get("quotes") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj