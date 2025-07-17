from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.dataforseo_trendsinterests_values_info import DataforseoTrendsinterestsValuesInfo



class DataforseoTrendsinterestsInfo(BaseModel):
    """
    DataforseoTrendsinterestsInfo
    """ # noqa: E501
    keyword: Optional[StrictStr] = Field(default=None, description="relevant keyword. the data included in the values element is based on this keyword")
    values: Optional[List[Optional[DataforseoTrendsinterestsValuesInfo]]] = Field(default=None, description="contains data on relative keyword popularity by country or region")
    __properties: ClassVar[List[str]] = [
        "keyword", 
        "values", 
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
        values_items = []
        if self.values:
            for _item in self.values:
                if _item:
                    values_items.append(_item.to_dict())
            _dict['values'] = values_items
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "keyword": obj.get("keyword"),
            "values": [DataforseoTrendsinterestsValuesInfo.from_dict(_item) for _item in obj["values"]] if obj.get("values") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj