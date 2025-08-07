from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.rating_element import RatingElement
from dataforseo_client.models.link_element import LinkElement
from dataforseo_client.models.about_this_result_element import AboutThisResultElement
from dataforseo_client.models.rank_changes import RankChanges
from dataforseo_client.models.backlinks_info import BacklinksInfo
from dataforseo_client.models.rank_info import RankInfo
from dataforseo_client.models.base_dataforseo_labs_api_element_item import BaseDataforseoLabsApiElementItem



class DataLabsOrganicSerpElementItem(BaseDataforseoLabsApiElementItem):
    """
    DataLabsOrganicSerpElementItem
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    se_type: Optional[StrictStr] = Field(default=None, description="search engine type")
    rank_group: Optional[StrictInt] = Field(default=None, description="position within a group of elements with identical type values. positions of elements with different type values are omitted from rank_group")
    rank_absolute: Optional[StrictInt] = Field(default=None, description="absolute rank in SERP. absolute position among all the elements in SERP")
    position: Optional[StrictStr] = Field(default=None, description="the alignment of the element in SERP. can take the following values:. left, right")
    xpath: Optional[StrictStr] = Field(default=None, description="the XPath of the element")
    domain: Optional[StrictStr] = Field(default=None, description="domain in SERP")
    title: Optional[StrictStr] = Field(default=None, description="title of the result in SERP")
    url: Optional[StrictStr] = Field(default=None, description="sitelink URL")
    breadcrumb: Optional[StrictStr] = Field(default=None, description="breadcrumb in SERP")
    website_name: Optional[StrictStr] = Field(default=None, description="name of the website in SERP")
    is_image: Optional[StrictBool] = Field(default=None, description="indicates whether the element contains an image")
    is_video: Optional[StrictBool] = Field(default=None, description="indicates whether the element contains a video")
    is_featured_snippet: Optional[StrictBool] = Field(default=None, description="indicates whether the element is a featured_snippet")
    is_malicious: Optional[StrictBool] = Field(default=None, description="indicates whether the element is marked as malicious")
    description: Optional[StrictStr] = Field(default=None, description="description of the results element in SERP")
    pre_snippet: Optional[StrictStr] = Field(default=None, description="includes additional information appended before the result description in SERP")
    extended_snippet: Optional[StrictStr] = Field(default=None, description="includes additional information appended after the result description in SERP")
    amp_version: Optional[StrictBool] = Field(default=None, description="Accelerated Mobile Pages. indicates whether an item has the Accelerated Mobile Page (AMP) version")
    rating: Optional[RatingElement] = Field(default=None, description="the item’s rating . the popularity rate based on reviews and displayed in SERP")
    highlighted: Optional[List[Optional[StrictStr]]] = Field(default=None, description="words highlighted in bold within the results description")
    links: Optional[List[Optional[LinkElement]]] = Field(default=None, description="sitelinks. the links shown below some of Google’s search results. if there are none, equals null")
    about_this_result: Optional[AboutThisResultElement] = Field(default=None, description="contains information from the ‘About this result’ panel. ‘About this result’ panel provides additional context about why Google returned this result for the given query;. this feature appears after clicking on the three dots next to most results")
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
        "domain", 
        "title", 
        "url", 
        "breadcrumb", 
        "website_name", 
        "is_image", 
        "is_video", 
        "is_featured_snippet", 
        "is_malicious", 
        "description", 
        "pre_snippet", 
        "extended_snippet", 
        "amp_version", 
        "rating", 
        "highlighted", 
        "links", 
        "about_this_result", 
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
        _dict['domain'] = self.domain
        _dict['title'] = self.title
        _dict['url'] = self.url
        _dict['breadcrumb'] = self.breadcrumb
        _dict['website_name'] = self.website_name
        _dict['is_image'] = self.is_image
        _dict['is_video'] = self.is_video
        _dict['is_featured_snippet'] = self.is_featured_snippet
        _dict['is_malicious'] = self.is_malicious
        _dict['description'] = self.description
        _dict['pre_snippet'] = self.pre_snippet
        _dict['extended_snippet'] = self.extended_snippet
        _dict['amp_version'] = self.amp_version
        _dict['rating'] = self.rating.to_dict() if self.rating else None
        _dict['highlighted'] = self.highlighted
        links_items = []
        if self.links:
            for _item in self.links:
                if _item:
                    links_items.append(_item.to_dict())
            _dict['links'] = links_items
        _dict['about_this_result'] = self.about_this_result.to_dict() if self.about_this_result else None
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
            "domain": obj.get("domain"),
            "title": obj.get("title"),
            "url": obj.get("url"),
            "breadcrumb": obj.get("breadcrumb"),
            "website_name": obj.get("website_name"),
            "is_image": obj.get("is_image"),
            "is_video": obj.get("is_video"),
            "is_featured_snippet": obj.get("is_featured_snippet"),
            "is_malicious": obj.get("is_malicious"),
            "description": obj.get("description"),
            "pre_snippet": obj.get("pre_snippet"),
            "extended_snippet": obj.get("extended_snippet"),
            "amp_version": obj.get("amp_version"),
            "rating": RatingElement.from_dict(obj["rating"]) if obj.get("rating") is not None else None,
            "highlighted": obj.get("highlighted"),
            "links": [LinkElement.from_dict(_item) for _item in obj["links"]] if obj.get("links") is not None else None,
            "about_this_result": AboutThisResultElement.from_dict(obj["about_this_result"]) if obj.get("about_this_result") is not None else None,
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