from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.appendix_bing_keywords_data_price_data_info import AppendixBingKeywordsDataPriceDataInfo
from dataforseo_client.models.appendix_task_keywords_data_price_data_info import AppendixTaskKeywordsDataPriceDataInfo



class AppendixClickstreamDataKeywordsDataPriceData(BaseModel):
    """
    AppendixClickstreamDataKeywordsDataPriceData
    """ # noqa: E501
    bulk_search_volume: Optional[AppendixBingKeywordsDataPriceDataInfo] = Field(default=None, description="")
    dataforseo_search_volume: Optional[AppendixBingKeywordsDataPriceDataInfo] = Field(default=None, description="")
    global_search_volume: Optional[AppendixBingKeywordsDataPriceDataInfo] = Field(default=None, description="")
    locations_and_languages: Optional[AppendixTaskKeywordsDataPriceDataInfo] = Field(default=None, description="")
    __properties: ClassVar[List[str]] = [
        "bulk_search_volume", 
        "dataforseo_search_volume", 
        "global_search_volume", 
        "locations_and_languages", 
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

        _dict['bulk_search_volume'] = self.bulk_search_volume.to_dict() if self.bulk_search_volume else None
        _dict['dataforseo_search_volume'] = self.dataforseo_search_volume.to_dict() if self.dataforseo_search_volume else None
        _dict['global_search_volume'] = self.global_search_volume.to_dict() if self.global_search_volume else None
        _dict['locations_and_languages'] = self.locations_and_languages.to_dict() if self.locations_and_languages else None
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "bulk_search_volume": AppendixBingKeywordsDataPriceDataInfo.from_dict(obj["bulk_search_volume"]) if obj.get("bulk_search_volume") is not None else None,
            "dataforseo_search_volume": AppendixBingKeywordsDataPriceDataInfo.from_dict(obj["dataforseo_search_volume"]) if obj.get("dataforseo_search_volume") is not None else None,
            "global_search_volume": AppendixBingKeywordsDataPriceDataInfo.from_dict(obj["global_search_volume"]) if obj.get("global_search_volume") is not None else None,
            "locations_and_languages": AppendixTaskKeywordsDataPriceDataInfo.from_dict(obj["locations_and_languages"]) if obj.get("locations_and_languages") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj