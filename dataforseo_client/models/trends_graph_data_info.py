from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class TrendsGraphDataInfo(BaseModel):
    """
    TrendsGraphDataInfo
    """ # noqa: E501
    date_from: Optional[StrictStr] = Field(default=None, description="start date of the corresponding time range. in the UTC format: “yyyy-mm-dd”")
    date_to: Optional[StrictStr] = Field(default=None, description="end date of the corresponding time range. in the UTC format: “yyyy-mm-dd”")
    timestamp: Optional[StrictInt] = Field(default=None, description="a point in time in the Unix time format")
    missing_data: Optional[StrictBool] = Field(default=None, description="indicates whether the data is unavailable. if true the data on the graph in the Google Trends interface is missing and thus labelled with a dotted line")
    values: Optional[List[Optional[StrictFloat]]] = Field(default=None, description="relative keyword popularity rate at a specific timestamp. represents the keyword popularity rate over the given time range. if you specify more than one keyword, the values will be averaged to the highest value across all specified keywords. a value of 100 is the peak popularity for the term. A value of 50 means that the term is half as popular. A score of 0 means there was not enough data for this term")
    __properties: ClassVar[List[str]] = [
        "date_from", 
        "date_to", 
        "timestamp", 
        "missing_data", 
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

        _dict['date_from'] = self.date_from
        _dict['date_to'] = self.date_to
        _dict['timestamp'] = self.timestamp
        _dict['missing_data'] = self.missing_data
        _dict['values'] = self.values
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "date_from": obj.get("date_from"),
            "date_to": obj.get("date_to"),
            "timestamp": obj.get("timestamp"),
            "missing_data": obj.get("missing_data"),
            "values": obj.get("values"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj