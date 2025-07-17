from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class DataforseoLabsSerpCompetitorsLiveItem(BaseModel):
    """
    DataforseoLabsSerpCompetitorsLiveItem
    """ # noqa: E501
    se_type: Optional[StrictStr] = Field(default=None, description="search engine type")
    domain: Optional[StrictStr] = Field(default=None, description="domain name of the detected SERP competitor")
    avg_position: Optional[StrictFloat] = Field(default=None, description="the average position of the domain for the specified keywords. the arithmetic mean of values in the keywords_positions array")
    median_position: Optional[StrictFloat] = Field(default=None, description="the median position of the domain for the specified keywords. the median of the values in the keywords_positions array")
    rating: Optional[StrictFloat] = Field(default=None, description="the margin between the greatest possible and actual keyword positions. represents the relative visibility rate of the domain in SERP for the specified keywords. calculated as sum(100-keywords_positions)")
    etv: Optional[StrictFloat] = Field(default=None, description="estimated traffic volume. represents the estimated monthly traffic that specified keywords are driving to the website. calculated as the sum of the products of the specified keywords’ search volume values and CTR (click-through-rate) rates at certain positions in SERP. learn more about how the metric is calculated in this help center article")
    keywords_count: Optional[StrictInt] = Field(default=None, description="the number of specified keywords the domain has positions for in SERPs")
    visibility: Optional[StrictFloat] = Field(default=None, description="SERP visibility rate. represents the website visibility rate based on the SERP positions of the specified keywords. Keywords with positions in the range from 1 to 10 are assigned the visibility index from 1 to 0.1, respectively. Keywords with positions in the range from 11 to 20 have the fixed visibility index of 0.05. keywords with positions from 20 to 100 have the visibility index equal to 0")
    relevant_serp_items: Optional[StrictInt] = Field(default=None, description="the number of SERP elements relevant to the domain. represents the number of search results in SERP relevant to the domain for the specified keywords")
    keywords_positions: Optional[Dict[str, Optional[List[Optional[StrictInt]]]]] = Field(default=None, description="keyword positions. SERP positions the related domain holds in SERP for the specified keywords")
    __properties: ClassVar[List[str]] = [
        "se_type", 
        "domain", 
        "avg_position", 
        "median_position", 
        "rating", 
        "etv", 
        "keywords_count", 
        "visibility", 
        "relevant_serp_items", 
        "keywords_positions", 
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
        _dict['domain'] = self.domain
        _dict['avg_position'] = self.avg_position
        _dict['median_position'] = self.median_position
        _dict['rating'] = self.rating
        _dict['etv'] = self.etv
        _dict['keywords_count'] = self.keywords_count
        _dict['visibility'] = self.visibility
        _dict['relevant_serp_items'] = self.relevant_serp_items
        _dict['keywords_positions'] = self.keywords_positions
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "se_type": obj.get("se_type"),
            "domain": obj.get("domain"),
            "avg_position": obj.get("avg_position"),
            "median_position": obj.get("median_position"),
            "rating": obj.get("rating"),
            "etv": obj.get("etv"),
            "keywords_count": obj.get("keywords_count"),
            "visibility": obj.get("visibility"),
            "relevant_serp_items": obj.get("relevant_serp_items"),
            "keywords_positions": obj.get("keywords_positions"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj