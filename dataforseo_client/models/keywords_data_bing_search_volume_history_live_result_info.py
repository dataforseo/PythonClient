from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.search_volume_history_search_info import SearchVolumeHistorySearchInfo



class KeywordsDataBingSearchVolumeHistoryLiveResultInfo(BaseModel):
    """
    KeywordsDataBingSearchVolumeHistoryLiveResultInfo
    """ # noqa: E501
    keyword: Optional[StrictStr] = Field(default=None, description="keyword in a POST array")
    location_code: Optional[StrictInt] = Field(default=None, description="location code in a POST array. if there is no data, then the value is null")
    language_code: Optional[StrictStr] = Field(default=None, description="language code in a POST array. if there is no data, then the value is null")
    device: Optional[List[Optional[StrictStr]]] = Field(default=None, description="")
    period: Optional[StrictStr] = Field(default=None, description="time period. indicates if returned data is aggregated to a certain time period. default value monthly")
    searches: Optional[SearchVolumeHistorySearchInfo] = Field(default=None, description="contains results distributed by device type. if the device parameter is not specified, the data will be returned for all available device types")
    __properties: ClassVar[List[str]] = [
        "keyword", 
        "location_code", 
        "language_code", 
        "device", 
        "period", 
        "searches", 
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

        _dict['keyword'] = self.keyword
        _dict['location_code'] = self.location_code
        _dict['language_code'] = self.language_code
        _dict['device'] = self.device
        _dict['period'] = self.period
        _dict['searches'] = self.searches.to_dict() if self.searches else None
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "keyword": obj.get("keyword"),
            "location_code": obj.get("location_code"),
            "language_code": obj.get("language_code"),
            "device": obj.get("device"),
            "period": obj.get("period"),
            "searches": SearchVolumeHistorySearchInfo.from_dict(obj["searches"]) if obj.get("searches") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj