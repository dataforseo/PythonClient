from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.keyword_data_info import KeywordDataInfo
from dataforseo_client.models.base_dataforseo_labs_api_element_item import BaseDataforseoLabsApiElementItem



class DataforseoLabsDomainIntersectionLiveItem(BaseModel):
    """
    DataforseoLabsDomainIntersectionLiveItem
    """ # noqa: E501
    se_type: Optional[StrictStr] = Field(default=None, description="search engine type")
    keyword_data: Optional[KeywordDataInfo] = Field(default=None, description="keyword data for the returned keyword")
    first_domain_serp_element: Optional[BaseDataforseoLabsApiElementItem] = Field(default=None, description="contains data on the first domain’s SERP element found for the returned keyword. the list of supported SERP elements can be found below")
    second_domain_serp_element: Optional[BaseDataforseoLabsApiElementItem] = Field(default=None, description="contains data on the second domain’s SERP element found for the returned keyword. the list of supported SERP elements can be found below")
    __properties: ClassVar[List[str]] = [
        "se_type", 
        "keyword_data", 
        "first_domain_serp_element", 
        "second_domain_serp_element", 
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
        _dict['first_domain_serp_element'] = self.first_domain_serp_element.to_dict() if self.first_domain_serp_element else None
        _dict['second_domain_serp_element'] = self.second_domain_serp_element.to_dict() if self.second_domain_serp_element else None
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
            "first_domain_serp_element": BaseDataforseoLabsApiElementItem.from_dict(obj["first_domain_serp_element"]) if obj.get("first_domain_serp_element") is not None else None,
            "second_domain_serp_element": BaseDataforseoLabsApiElementItem.from_dict(obj["second_domain_serp_element"]) if obj.get("second_domain_serp_element") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj