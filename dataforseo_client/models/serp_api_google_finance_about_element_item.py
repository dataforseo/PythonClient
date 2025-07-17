from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.base_serp_api_google_finance_element_item import BaseSerpApiGoogleFinanceElementItem



class SerpApiGoogleFinanceAboutElementItem(BaseSerpApiGoogleFinanceElementItem):
    """
    SerpApiGoogleFinanceAboutElementItem
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    rank_group: Optional[StrictInt] = Field(default=None, description="group rank in SERP. position within a group of elements with identical type values. positions of elements with different type values are omitted from rank_group")
    rank_absolute: Optional[StrictInt] = Field(default=None, description="absolute rank in SERP. absolute position among all the elements in SERP")
    displayed_name: Optional[StrictStr] = Field(default=None, description="displayed name of the market index. example: E-mini Dow ($5)")
    description: Optional[StrictStr] = Field(default=None, description="company description")
    description_source_url: Optional[StrictStr] = Field(default=None, description="source of information provided in description")
    ceo: Optional[StrictStr] = Field(default=None, description="Chief Executive Officer of the company")
    founded: Optional[StrictStr] = Field(default=None, description="date when the company was founded. in the format: “yyyy-mm-ddThh-mm-ssZ”. example:. 1993-04-05T00:00:00Z")
    headquarters: Optional[StrictStr] = Field(default=None, description="company headquarters")
    website: Optional[StrictStr] = Field(default=None, description="company website")
    employees: Optional[StrictInt] = Field(default=None, description="number of company employees")
    __properties: ClassVar[List[str]] = [
        "type", 
        "rank_group", 
        "rank_absolute", 
        "displayed_name", 
        "description", 
        "description_source_url", 
        "ceo", 
        "founded", 
        "headquarters", 
        "website", 
        "employees", 
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
        _dict['rank_group'] = self.rank_group
        _dict['rank_absolute'] = self.rank_absolute
        _dict['displayed_name'] = self.displayed_name
        _dict['description'] = self.description
        _dict['description_source_url'] = self.description_source_url
        _dict['ceo'] = self.ceo
        _dict['founded'] = self.founded
        _dict['headquarters'] = self.headquarters
        _dict['website'] = self.website
        _dict['employees'] = self.employees
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "rank_group": obj.get("rank_group"),
            "rank_absolute": obj.get("rank_absolute"),
            "displayed_name": obj.get("displayed_name"),
            "description": obj.get("description"),
            "description_source_url": obj.get("description_source_url"),
            "ceo": obj.get("ceo"),
            "founded": obj.get("founded"),
            "headquarters": obj.get("headquarters"),
            "website": obj.get("website"),
            "employees": obj.get("employees"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj