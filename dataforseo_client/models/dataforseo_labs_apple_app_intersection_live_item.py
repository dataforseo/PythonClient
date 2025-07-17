from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.keyword_data_info import KeywordDataInfo
from dataforseo_client.models.app_store_search_organic import AppStoreSearchOrganic



class DataforseoLabsAppleAppIntersectionLiveItem(BaseModel):
    """
    DataforseoLabsAppleAppIntersectionLiveItem
    """ # noqa: E501
    se_type: Optional[StrictStr] = Field(default=None, description="search engine type")
    keyword_data: Optional[KeywordDataInfo] = Field(default=None, description="keyword data for the returned keyword")
    intersection_result: Optional[Dict[str, Optional[AppStoreSearchOrganic]]] = Field(default=None, description="contains SERP data for the returned keyword. data will be provided in separate arrays for each app ID you specified in the app_ids object when setting a task;. depending on the number of specified app IDs, it can contain from 1 to 20 arrays named respectively")
    __properties: ClassVar[List[str]] = [
        "se_type", 
        "keyword_data", 
        "intersection_result", 
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
        _dict['keyword_data'] = self.keyword_data.to_dict() if self.keyword_data else None
        _dict['intersection_result'] = self.intersection_result
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "se_type": obj.get("se_type"),
            "keyword_data": KeywordDataInfo.from_dict(obj["keyword_data"]) if obj.get("keyword_data") is not None else None,
            "intersection_result": obj.get("intersection_result"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj