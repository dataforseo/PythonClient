from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.appendix_bing_keywords_data_price_data_info import AppendixBingKeywordsDataPriceDataInfo



class AppendixDataforseoTrendsKeywordsDataPriceData(BaseModel):
    """
    AppendixDataforseoTrendsKeywordsDataPriceData
    """ # noqa: E501
    demography: Optional[AppendixBingKeywordsDataPriceDataInfo] = Field(default=None, description="")
    explore: Optional[AppendixBingKeywordsDataPriceDataInfo] = Field(default=None, description="")
    merged_data: Optional[AppendixBingKeywordsDataPriceDataInfo] = Field(default=None, description="")
    subregion_interests: Optional[AppendixBingKeywordsDataPriceDataInfo] = Field(default=None, description="")
    __properties: ClassVar[List[str]] = [
        "demography", 
        "explore", 
        "merged_data", 
        "subregion_interests", 
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

        _dict['demography'] = self.demography.to_dict() if self.demography else None
        _dict['explore'] = self.explore.to_dict() if self.explore else None
        _dict['merged_data'] = self.merged_data.to_dict() if self.merged_data else None
        _dict['subregion_interests'] = self.subregion_interests.to_dict() if self.subregion_interests else None
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "demography": AppendixBingKeywordsDataPriceDataInfo.from_dict(obj["demography"]) if obj.get("demography") is not None else None,
            "explore": AppendixBingKeywordsDataPriceDataInfo.from_dict(obj["explore"]) if obj.get("explore") is not None else None,
            "merged_data": AppendixBingKeywordsDataPriceDataInfo.from_dict(obj["merged_data"]) if obj.get("merged_data") is not None else None,
            "subregion_interests": AppendixBingKeywordsDataPriceDataInfo.from_dict(obj["subregion_interests"]) if obj.get("subregion_interests") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj