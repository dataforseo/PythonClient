from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.top_domain_info import TopDomainInfo
from dataforseo_client.models.content_analysis_categories_info import ContentAnalysisCategoriesInfo



class ContentAnalysisPhraseTrendsLiveResultInfo(BaseModel):
    """
    ContentAnalysisPhraseTrendsLiveResultInfo
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    date: Optional[StrictStr] = Field(default=None, description="date for which the data is provided")
    total_count: Optional[StrictInt] = Field(default=None, description="total number of results in our database relevant to your request")
    rank: Optional[StrictInt] = Field(default=None, description="rank of all URLs citing the keyword. normalized sum of ranks of all URLs citing the target keyword for the given date")
    top_domains: Optional[List[Optional[TopDomainInfo]]] = Field(default=None, description="top domains citing the target keyword. contains objects with top domains citing the target keyword and citation count per each domain")
    sentiment_connotations: Optional[Dict[str, Optional[StrictInt]]] = Field(default=None, description="sentiment connotations. contains sentiments (emotional reactions) related to the target keyword citation and the number of citations per each sentiment. possible connotations: 'anger', 'happiness', 'love', 'sadness', 'share', 'fun'")
    connotation_types: Optional[Dict[str, Optional[StrictInt]]] = Field(default=None, description="connotation types. contains types of sentiments (sentiment polarity) related to the keyword citation and citation count per each sentiment type. possible connotation types: 'positive', 'negative', 'neutral'")
    text_categories: Optional[List[Optional[ContentAnalysisCategoriesInfo]]] = Field(default=None, description="text categories. contains objects with text categories and citation count in each text category. to obtain a full list of available categories, refer to the Categories endpoint")
    page_categories: Optional[List[Optional[ContentAnalysisCategoriesInfo]]] = Field(default=None, description="page categories. contains objects with page categories and citation count in each page category. to obtain a full list of available categories, refer to the Categories endpoint")
    page_types: Optional[Dict[str, Optional[StrictInt]]] = Field(default=None, description="page types. contains page types and citation count per each page type")
    countries: Optional[Dict[str, Optional[StrictInt]]] = Field(default=None, description="countries. contains countries and citation count in each country. to obtain a full list of available countries, refer to the Locations endpoint")
    languages: Optional[Dict[str, Optional[StrictInt]]] = Field(default=None, description="languages. contains languages and citation count in each language. to obtain a full list of available languages, refer to the Languages endpoint")
    __properties: ClassVar[List[str]] = [
        "type", 
        "date", 
        "total_count", 
        "rank", 
        "top_domains", 
        "sentiment_connotations", 
        "connotation_types", 
        "text_categories", 
        "page_categories", 
        "page_types", 
        "countries", 
        "languages", 
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
        _dict['date'] = self.date
        _dict['total_count'] = self.total_count
        _dict['rank'] = self.rank
        top_domains_items = []
        if self.top_domains:
            for _item in self.top_domains:
                if _item:
                    top_domains_items.append(_item.to_dict())
            _dict['top_domains'] = top_domains_items
        _dict['sentiment_connotations'] = self.sentiment_connotations
        _dict['connotation_types'] = self.connotation_types
        text_categories_items = []
        if self.text_categories:
            for _item in self.text_categories:
                if _item:
                    text_categories_items.append(_item.to_dict())
            _dict['text_categories'] = text_categories_items
        page_categories_items = []
        if self.page_categories:
            for _item in self.page_categories:
                if _item:
                    page_categories_items.append(_item.to_dict())
            _dict['page_categories'] = page_categories_items
        _dict['page_types'] = self.page_types
        _dict['countries'] = self.countries
        _dict['languages'] = self.languages
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "date": obj.get("date"),
            "total_count": obj.get("total_count"),
            "rank": obj.get("rank"),
            "top_domains": [TopDomainInfo.from_dict(_item) for _item in obj["top_domains"]] if obj.get("top_domains") is not None else None,
            "sentiment_connotations": obj.get("sentiment_connotations"),
            "connotation_types": obj.get("connotation_types"),
            "text_categories": [ContentAnalysisCategoriesInfo.from_dict(_item) for _item in obj["text_categories"]] if obj.get("text_categories") is not None else None,
            "page_categories": [ContentAnalysisCategoriesInfo.from_dict(_item) for _item in obj["page_categories"]] if obj.get("page_categories") is not None else None,
            "page_types": obj.get("page_types"),
            "countries": obj.get("countries"),
            "languages": obj.get("languages"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj