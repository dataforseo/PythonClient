from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.dataforseo_trends_graph_data_trends_graph_data_info import DataforseoTrendsGraphDataTrendsGraphDataInfo
from dataforseo_client.models.base_keyword_data_dataforseo_trends_item import BaseKeywordDataDataforseoTrendsItem



class DataforseoTrendsDataforseoTrendsGraphElementItem(BaseKeywordDataDataforseoTrendsItem):
    """
    DataforseoTrendsDataforseoTrendsGraphElementItem
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    position: Optional[StrictInt] = Field(default=None, description="the alignment of the element. can take the following values: 1, 2, 3, 4, etc.")
    keywords: Optional[List[Optional[StrictStr]]] = Field(default=None, description="relevant keywords. the data included in the dataforseo_trends_graph element is based on the keywords listed in this array")
    data: Optional[List[Optional[DataforseoTrendsGraphDataTrendsGraphDataInfo]]] = Field(default=None, description="DataForSEO Trends data for the specified parameters")
    averages: Optional[List[Optional[StrictInt]]] = Field(default=None, description="keyword popularity values averaged over the whole time range")
    __properties: ClassVar[List[str]] = [
        "type", 
        "position", 
        "keywords", 
        "data", 
        "averages", 
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
        _dict['keywords'] = self.keywords
        data_items = []
        if self.data:
            for _item in self.data:
                if _item:
                    data_items.append(_item.to_dict())
            _dict['data'] = data_items
        _dict['averages'] = self.averages
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
            "keywords": obj.get("keywords"),
            "data": [DataforseoTrendsGraphDataTrendsGraphDataInfo.from_dict(_item) for _item in obj["data"]] if obj.get("data") is not None else None,
            "averages": obj.get("averages"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj