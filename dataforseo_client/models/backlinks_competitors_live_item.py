from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class BacklinksCompetitorsLiveItem(BaseModel):
    """
    BacklinksCompetitorsLiveItem
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    target: Optional[StrictStr] = Field(default=None, description="competitor domain")
    rank: Optional[StrictInt] = Field(default=None, description="domain rank. domain rank across all domains in the database. rank is calculated based on the method for node ranking in a linked database – a principle used in the original Google PageRank algorithm. learn more about the metric and how it is calculated in this help center article")
    intersections: Optional[StrictInt] = Field(default=None, description="indicates the number of backlink intersections with the target specified in the POST array")
    __properties: ClassVar[List[str]] = [
        "type", 
        "target", 
        "rank", 
        "intersections", 
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
        _dict['target'] = self.target
        _dict['rank'] = self.rank
        _dict['intersections'] = self.intersections
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "target": obj.get("target"),
            "rank": obj.get("rank"),
            "intersections": obj.get("intersections"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj