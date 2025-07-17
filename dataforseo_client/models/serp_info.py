from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class SerpInfo(BaseModel):
    """
    SerpInfo
    """ # noqa: E501
    se_type: Optional[StrictStr] = Field(default=None, description="search engine type")
    check_url: Optional[StrictStr] = Field(default=None, description="direct URL to search engine results. you can use it to make sure that we provided accurate results")
    serp_item_types: Optional[List[Optional[StrictStr]]] = Field(default=None, description="types of search results in SERP. contains types of search results (items) found in SERP. possible item types:. answer_box, app, carousel, multi_carousel, featured_snippet, google_flights, google_reviews, third_party_reviews, google_posts, images, jobs, knowledge_graph, local_pack, hotels_pack, map, organic, paid, people_also_ask, related_searches, people_also_search, shopping, top_stories, twitter, video, events, mention_carousel, recipes, top_sights, scholarly_articles, popular_products, podcasts, questions_and_answers, find_results_on, stocks_box, visual_stories, commercial_units, local_services, google_hotels, math_solver, currency_box, product_considerations, found_on_web, short_videos, refine_products, explore_brands, perspectives, discussions_and_forums, compare_sites, courses, ai_overview;. note that the actual results will be returned only for organic, paid, featured_snippet, and local_pack elements")
    se_results_count: Optional[StrictInt] = Field(default=None, description="number of search results for the returned keyword")
    last_updated_time: Optional[StrictStr] = Field(default=None, description="date and time when search intent data was last updated. in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”. example:. 2019-11-15 12:57:46 +00:00")
    previous_updated_time: Optional[StrictStr] = Field(default=None, description="previous to the most recent date and time when SERP data was updated. in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”. example:. 2019-10-15 12:57:46 +00:00")
    __properties: ClassVar[List[str]] = [
        "se_type", 
        "check_url", 
        "serp_item_types", 
        "se_results_count", 
        "last_updated_time", 
        "previous_updated_time", 
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
        _dict['check_url'] = self.check_url
        _dict['serp_item_types'] = self.serp_item_types
        _dict['se_results_count'] = self.se_results_count
        _dict['last_updated_time'] = self.last_updated_time
        _dict['previous_updated_time'] = self.previous_updated_time
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "se_type": obj.get("se_type"),
            "check_url": obj.get("check_url"),
            "serp_item_types": obj.get("serp_item_types"),
            "se_results_count": obj.get("se_results_count"),
            "last_updated_time": obj.get("last_updated_time"),
            "previous_updated_time": obj.get("previous_updated_time"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj