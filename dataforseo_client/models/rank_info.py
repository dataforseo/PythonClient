from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class RankInfo(BaseModel):
    """
    RankInfo
    """ # noqa: E501
    page_rank: Optional[StrictInt] = Field(default=None, description="page rank. page_rank is calculated based on the method for node ranking in a linked database – a principle used in the original Google PageRank algorithm;. learn more about the metric and how it is calculated in this help center article")
    main_domain_rank: Optional[StrictInt] = Field(default=None, description="main domain rank. main_domain_rank is calculated based on the method for node ranking in a linked database – a principle used in the original Google PageRank algorithm. learn more about the metric and how it is calculated in this help center article")
    __properties: ClassVar[List[str]] = [
        "page_rank", 
        "main_domain_rank", 
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

        _dict['page_rank'] = self.page_rank
        _dict['main_domain_rank'] = self.main_domain_rank
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "page_rank": obj.get("page_rank"),
            "main_domain_rank": obj.get("main_domain_rank"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj