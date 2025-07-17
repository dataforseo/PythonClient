from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.keyword_info import KeywordInfo
from dataforseo_client.models.keyword_info_normalized_with_info import KeywordInfoNormalizedWithInfo
from dataforseo_client.models.clickstream_keyword_info import ClickstreamKeywordInfo
from dataforseo_client.models.keyword_properties import KeywordProperties
from dataforseo_client.models.serp_info import SerpInfo
from dataforseo_client.models.avg_backlinks_info import AvgBacklinksInfo
from dataforseo_client.models.search_intent_info import SearchIntentInfo



class KeywordDataInfo(BaseModel):
    """
    KeywordDataInfo
    """ # noqa: E501
    se_type: Optional[StrictStr] = Field(default=None, description="search engine type")
    keyword: Optional[StrictStr] = Field(default=None, description="returned keyword idea")
    location_code: Optional[StrictInt] = Field(default=None, description="location code in a POST array")
    language_code: Optional[StrictStr] = Field(default=None, description="language code in a POST array")
    keyword_info: Optional[KeywordInfo] = Field(default=None, description="keyword data for the returned keyword idea")
    keyword_info_normalized_with_bing: Optional[KeywordInfoNormalizedWithInfo] = Field(default=None, description="contains keyword search volume normalized with Bing search volume")
    keyword_info_normalized_with_clickstream: Optional[KeywordInfoNormalizedWithInfo] = Field(default=None, description="contains keyword search volume normalized with clickstream data")
    clickstream_keyword_info: Optional[ClickstreamKeywordInfo] = Field(default=None, description="clickstream data for the returned keyword. to retrieve results for this field, the parameter include_clickstream_data must be set to true")
    keyword_properties: Optional[KeywordProperties] = Field(default=None, description="additional information about the keyword")
    serp_info: Optional[SerpInfo] = Field(default=None, description="SERP data. the value will be null if you didn’t set the field include_serp_info to true in the POST array or if there is no SERP data for this keyword in our database")
    avg_backlinks_info: Optional[AvgBacklinksInfo] = Field(default=None, description="backlink data for the returned keyword. this object provides the average number of backlinks, referring pages and domains, as well as the average rank values among the top-10 webpages ranking organically for the keyword")
    search_intent_info: Optional[SearchIntentInfo] = Field(default=None, description="search intent info for the returned keyword. learn about search intent in this help center article")
    __properties: ClassVar[List[str]] = [
        "se_type", 
        "keyword", 
        "location_code", 
        "language_code", 
        "keyword_info", 
        "keyword_info_normalized_with_bing", 
        "keyword_info_normalized_with_clickstream", 
        "clickstream_keyword_info", 
        "keyword_properties", 
        "serp_info", 
        "avg_backlinks_info", 
        "search_intent_info", 
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

        _dict['se_type'] = self.se_type
        _dict['keyword'] = self.keyword
        _dict['location_code'] = self.location_code
        _dict['language_code'] = self.language_code
        _dict['keyword_info'] = self.keyword_info.to_dict() if self.keyword_info else None
        _dict['keyword_info_normalized_with_bing'] = self.keyword_info_normalized_with_bing.to_dict() if self.keyword_info_normalized_with_bing else None
        _dict['keyword_info_normalized_with_clickstream'] = self.keyword_info_normalized_with_clickstream.to_dict() if self.keyword_info_normalized_with_clickstream else None
        _dict['clickstream_keyword_info'] = self.clickstream_keyword_info.to_dict() if self.clickstream_keyword_info else None
        _dict['keyword_properties'] = self.keyword_properties.to_dict() if self.keyword_properties else None
        _dict['serp_info'] = self.serp_info.to_dict() if self.serp_info else None
        _dict['avg_backlinks_info'] = self.avg_backlinks_info.to_dict() if self.avg_backlinks_info else None
        _dict['search_intent_info'] = self.search_intent_info.to_dict() if self.search_intent_info else None
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "se_type": obj.get("se_type"),
            "keyword": obj.get("keyword"),
            "location_code": obj.get("location_code"),
            "language_code": obj.get("language_code"),
            "keyword_info": KeywordInfo.from_dict(obj["keyword_info"]) if obj.get("keyword_info") is not None else None,
            "keyword_info_normalized_with_bing": KeywordInfoNormalizedWithInfo.from_dict(obj["keyword_info_normalized_with_bing"]) if obj.get("keyword_info_normalized_with_bing") is not None else None,
            "keyword_info_normalized_with_clickstream": KeywordInfoNormalizedWithInfo.from_dict(obj["keyword_info_normalized_with_clickstream"]) if obj.get("keyword_info_normalized_with_clickstream") is not None else None,
            "clickstream_keyword_info": ClickstreamKeywordInfo.from_dict(obj["clickstream_keyword_info"]) if obj.get("clickstream_keyword_info") is not None else None,
            "keyword_properties": KeywordProperties.from_dict(obj["keyword_properties"]) if obj.get("keyword_properties") is not None else None,
            "serp_info": SerpInfo.from_dict(obj["serp_info"]) if obj.get("serp_info") is not None else None,
            "avg_backlinks_info": AvgBacklinksInfo.from_dict(obj["avg_backlinks_info"]) if obj.get("avg_backlinks_info") is not None else None,
            "search_intent_info": SearchIntentInfo.from_dict(obj["search_intent_info"]) if obj.get("search_intent_info") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj