from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.list_data_info import ListDataInfo
from dataforseo_client.models.base_keyword_data_google_trends_item import BaseKeywordDataGoogleTrendsItem



class GoogleTrendsGoogleTrendsTopicsListElementItem(BaseKeywordDataGoogleTrendsItem):
    """
    GoogleTrendsGoogleTrendsTopicsListElementItem
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    position: Optional[StrictInt] = Field(default=None, description="the alignment of the element in Google Trends. can take the following values: 1, 2, 3, 4, etc.")
    title: Optional[StrictStr] = Field(default=None, description="title of the element in Google Trends")
    keywords: Optional[List[Optional[StrictStr]]] = Field(default=None, description="relevant keywords. the data included in the google_trends_graph element is based on the keywords listed in this array")
    data: Optional[ListDataInfo] = Field(default=None, description="Google Trends data from the corresponding item")
    __properties: ClassVar[List[str]] = [
        "type", 
        "position", 
        "title", 
        "keywords", 
        "data", 
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
        _dict['position'] = self.position
        _dict['title'] = self.title
        _dict['keywords'] = self.keywords
        _dict['data'] = self.data.to_dict() if self.data else None
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "position": obj.get("position"),
            "title": obj.get("title"),
            "keywords": obj.get("keywords"),
            "data": ListDataInfo.from_dict(obj["data"]) if obj.get("data") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj