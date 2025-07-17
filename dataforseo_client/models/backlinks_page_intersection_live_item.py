from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.intersection_summary_info import IntersectionSummaryInfo
from dataforseo_client.models.backlinks_page_intersection import BacklinksPageIntersection



class BacklinksPageIntersectionLiveItem(BaseModel):
    """
    BacklinksPageIntersectionLiveItem
    """ # noqa: E501
    page_intersection: Optional[Dict[str, Optional[List[Optional[BacklinksPageIntersection]]]]] = Field(default=None, description="contains data on pages that link to the corresponding targets specified in the POST array. data is provided in separate objects corresponding to pages specified in the targets object")
    summary: Optional[IntersectionSummaryInfo] = Field(default=None, description="contains the page intersections summary")
    __properties: ClassVar[List[str]] = [
        "page_intersection", 
        "summary", 
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

        _dict['page_intersection'] = self.page_intersection
        _dict['summary'] = self.summary.to_dict() if self.summary else None
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "page_intersection": obj.get("page_intersection"),
            "summary": IntersectionSummaryInfo.from_dict(obj["summary"]) if obj.get("summary") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj