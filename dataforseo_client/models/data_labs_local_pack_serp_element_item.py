from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.rating_element import RatingElement
from dataforseo_client.models.rank_changes import RankChanges
from dataforseo_client.models.backlinks_info import BacklinksInfo
from dataforseo_client.models.rank_info import RankInfo
from dataforseo_client.models.base_dataforseo_labs_api_element_item import BaseDataforseoLabsApiElementItem



class DataLabsLocalPackSerpElementItem(BaseDataforseoLabsApiElementItem):
    """
    DataLabsLocalPackSerpElementItem
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    se_type: Optional[StrictStr] = Field(default=None, description="search engine type")
    rank_group: Optional[StrictInt] = Field(default=None, description="position within a group of elements with identical type values. positions of elements with different type values are omitted from rank_group")
    rank_absolute: Optional[StrictInt] = Field(default=None, description="absolute rank in SERP. absolute position among all the elements in SERP")
    position: Optional[StrictStr] = Field(default=None, description="the alignment of the element in SERP. can take the following values:. left, right")
    xpath: Optional[StrictStr] = Field(default=None, description="the XPath of the element")
    title: Optional[StrictStr] = Field(default=None, description="title of the result in SERP")
    description: Optional[StrictStr] = Field(default=None, description="description of the results element in SERP")
    domain: Optional[StrictStr] = Field(default=None, description="domain in SERP")
    phone: Optional[StrictStr] = Field(default=None, description="phone number")
    url: Optional[StrictStr] = Field(default=None, description="sitelink URL")
    is_paid: Optional[StrictBool] = Field(default=None, description="indicates whether the element is an ad")
    rating: Optional[RatingElement] = Field(default=None, description="the item’s rating . the popularity rate based on reviews and displayed in SERP")
    main_domain: Optional[StrictStr] = Field(default=None, description="primary domain name in SERP")
    relative_url: Optional[StrictStr] = Field(default=None, description="URL in SERP that does not specify the HTTPs protocol and domain name")
    etv: Optional[StrictFloat] = Field(default=None, description="estimated traffic volume. estimated organic monthly traffic a featured URL delivers to the domain. calculated as the product of CTR (click-through-rate) and search volume values of the returned keyword. learn more about how the metric is calculated in this help center article")
    estimated_paid_traffic_cost: Optional[StrictFloat] = Field(default=None, description="estimated cost of converting organic search traffic into paid. represents the estimated monthly cost of running ads for the returned keyword. the metric is calculated as the product of organic etv and paid cpc values and indicates the cost of driving the estimated volume of monthly organic traffic through PPC advertising in Google Search. learn more about how the metric is calculated in this help center article")
    clickstream_etv: Optional[StrictFloat] = Field(default=None, description="")
    rank_changes: Optional[RankChanges] = Field(default=None, description="changes in rankings. ranking changes of the SERP element compared to the preceding month;. Note: the changes are calculated even if the preceding month is not included in a POST request")
    backlinks_info: Optional[BacklinksInfo] = Field(default=None, description="backlinks information for the ranked website")
    rank_info: Optional[RankInfo] = Field(default=None, description="page and domain rank information")
    __properties: ClassVar[List[str]] = [
        "type", 
        "se_type", 
        "rank_group", 
        "rank_absolute", 
        "position", 
        "xpath", 
        "title", 
        "description", 
        "domain", 
        "phone", 
        "url", 
        "is_paid", 
        "rating", 
        "main_domain", 
        "relative_url", 
        "etv", 
        "estimated_paid_traffic_cost", 
        "clickstream_etv", 
        "rank_changes", 
        "backlinks_info", 
        "rank_info", 
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
        _dict['se_type'] = self.se_type
        _dict['rank_group'] = self.rank_group
        _dict['rank_absolute'] = self.rank_absolute
        _dict['position'] = self.position
        _dict['xpath'] = self.xpath
        _dict['title'] = self.title
        _dict['description'] = self.description
        _dict['domain'] = self.domain
        _dict['phone'] = self.phone
        _dict['url'] = self.url
        _dict['is_paid'] = self.is_paid
        _dict['rating'] = self.rating.to_dict() if self.rating else None
        _dict['main_domain'] = self.main_domain
        _dict['relative_url'] = self.relative_url
        _dict['etv'] = self.etv
        _dict['estimated_paid_traffic_cost'] = self.estimated_paid_traffic_cost
        _dict['clickstream_etv'] = self.clickstream_etv
        _dict['rank_changes'] = self.rank_changes.to_dict() if self.rank_changes else None
        _dict['backlinks_info'] = self.backlinks_info.to_dict() if self.backlinks_info else None
        _dict['rank_info'] = self.rank_info.to_dict() if self.rank_info else None
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "se_type": obj.get("se_type"),
            "rank_group": obj.get("rank_group"),
            "rank_absolute": obj.get("rank_absolute"),
            "position": obj.get("position"),
            "xpath": obj.get("xpath"),
            "title": obj.get("title"),
            "description": obj.get("description"),
            "domain": obj.get("domain"),
            "phone": obj.get("phone"),
            "url": obj.get("url"),
            "is_paid": obj.get("is_paid"),
            "rating": RatingElement.from_dict(obj["rating"]) if obj.get("rating") is not None else None,
            "main_domain": obj.get("main_domain"),
            "relative_url": obj.get("relative_url"),
            "etv": obj.get("etv"),
            "estimated_paid_traffic_cost": obj.get("estimated_paid_traffic_cost"),
            "clickstream_etv": obj.get("clickstream_etv"),
            "rank_changes": RankChanges.from_dict(obj["rank_changes"]) if obj.get("rank_changes") is not None else None,
            "backlinks_info": BacklinksInfo.from_dict(obj["backlinks_info"]) if obj.get("backlinks_info") is not None else None,
            "rank_info": RankInfo.from_dict(obj["rank_info"]) if obj.get("rank_info") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj