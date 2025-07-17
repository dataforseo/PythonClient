from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.appendix_info import AppendixInfo



class AppendixGoogleAdsKeywordsDataLimitsRatesDataInfo(BaseModel):
    """
    AppendixGoogleAdsKeywordsDataLimitsRatesDataInfo
    """ # noqa: E501
    status: Optional[StrictFloat] = Field(default=None, description="")
    search_volume: Optional[AppendixInfo] = Field(default=None, description="")
    keywords_for_keywords: Optional[AppendixInfo] = Field(default=None, description="")
    keywords_for_site: Optional[AppendixInfo] = Field(default=None, description="")
    ad_traffic_by_keywords: Optional[AppendixInfo] = Field(default=None, description="")
    __properties: ClassVar[List[str]] = [
        "status", 
        "search_volume", 
        "keywords_for_keywords", 
        "keywords_for_site", 
        "ad_traffic_by_keywords", 
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

        _dict['status'] = self.status
        _dict['search_volume'] = self.search_volume.to_dict() if self.search_volume else None
        _dict['keywords_for_keywords'] = self.keywords_for_keywords.to_dict() if self.keywords_for_keywords else None
        _dict['keywords_for_site'] = self.keywords_for_site.to_dict() if self.keywords_for_site else None
        _dict['ad_traffic_by_keywords'] = self.ad_traffic_by_keywords.to_dict() if self.ad_traffic_by_keywords else None
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "status": obj.get("status"),
            "search_volume": AppendixInfo.from_dict(obj["search_volume"]) if obj.get("search_volume") is not None else None,
            "keywords_for_keywords": AppendixInfo.from_dict(obj["keywords_for_keywords"]) if obj.get("keywords_for_keywords") is not None else None,
            "keywords_for_site": AppendixInfo.from_dict(obj["keywords_for_site"]) if obj.get("keywords_for_site") is not None else None,
            "ad_traffic_by_keywords": AppendixInfo.from_dict(obj["ad_traffic_by_keywords"]) if obj.get("ad_traffic_by_keywords") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj