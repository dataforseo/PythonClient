from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.demography import Demography
from dataforseo_client.models.demography_comparison_info import DemographyComparisonInfo
from dataforseo_client.models.base_keyword_data_dataforseo_trends_item import BaseKeywordDataDataforseoTrendsItem



class DataforseoTrendsDemographyElementItem(BaseKeywordDataDataforseoTrendsItem):
    """
    DataforseoTrendsDemographyElementItem
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    position: Optional[StrictInt] = Field(default=None, description="the alignment of the element. can take the following values: 1, 2, 3, 4, etc.")
    keywords: Optional[List[Optional[StrictStr]]] = Field(default=None, description="relevant keywords. the data included in the dataforseo_trends_graph element is based on the keywords listed in this array")
    demography: Optional[Demography] = Field(default=None, description="demographic breakdown of keyword popularity data per each specified term. conains keyword popularity data by age and gender")
    demography_comparison: Optional[DemographyComparisonInfo] = Field(default=None, description="comparison of demographic data on keyword popularity for the specified parameters. conains keyword popularity data by age and gender. if you specified a single keyword, the value will be null")
    __properties: ClassVar[List[str]] = [
        "type", 
        "position", 
        "keywords", 
        "demography", 
        "demography_comparison", 
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
        _dict['demography'] = self.demography.to_dict() if self.demography else None
        _dict['demography_comparison'] = self.demography_comparison.to_dict() if self.demography_comparison else None
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
            "demography": Demography.from_dict(obj["demography"]) if obj.get("demography") is not None else None,
            "demography_comparison": DemographyComparisonInfo.from_dict(obj["demography_comparison"]) if obj.get("demography_comparison") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj