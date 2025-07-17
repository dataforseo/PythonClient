from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.base_dataforseo_labs_api_element_item import BaseDataforseoLabsApiElementItem



class RankedSerpElement(BaseModel):
    """
    RankedSerpElement
    """ # noqa: E501
    se_type: Optional[StrictStr] = Field(default=None, description="search engine type")
    serp_item: Optional[BaseDataforseoLabsApiElementItem] = Field(default=None, description="contains data on the SERP element. the list of supported SERP elements can be found below")
    check_url: Optional[StrictStr] = Field(default=None, description="direct URL to search engine results. you can use it to make sure that we provided accurate results")
    serp_item_types: Optional[List[Optional[StrictStr]]] = Field(default=None, description="types of search results in SERP. contains types of search results (items) found in SERP. all possible item types can be found here, they include:. answer_box, app, carousel, multi_carousel, featured_snippet, google_flights, google_reviews, images, jobs, knowledge_graph, local_pack, map, organic, paid, people_also_ask, related_searches, people_also_search, shopping, top_stories, twitter, video, events, mention_carousel, recipes, top_sights, scholarly_articles, popular_products, podcasts, questions_and_answers, find_results_on, stocks_box;. note that the actual results will be returned only for organic, paid, featured_snippet, local_pack, and ai_overview_reference elements")
    se_results_count: Optional[StrictInt] = Field(default=None, description="number of search results for the returned keyword")
    keyword_difficulty: Optional[StrictInt] = Field(default=None, description="difficulty of ranking in the first top-10 organic results for a keyword. indicates the chance of getting in top-10 organic results for a keyword on a logarithmic scale from 0 to 100;. calculated by analysing, among other parameters, link profiles of the first 10 pages in SERP;. learn more about the metric in this help center guide")
    is_lost: Optional[StrictBool] = Field(default=None, description="lost ranked elements. indicates how many ranked elements of this domain were previously presented in SERPs, but weren’t found during the last check")
    last_updated_time: Optional[StrictStr] = Field(default=None, description="date and time when SERP data was updated. in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”. example:. 2019-11-15 12:57:46 +00:00")
    previous_updated_time: Optional[StrictStr] = Field(default=None, description="previous to the most recent date and time when SERP data was updated. in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”. example:. 2019-10-15 12:57:46 +00:00")
    __properties: ClassVar[List[str]] = [
        "se_type", 
        "serp_item", 
        "check_url", 
        "serp_item_types", 
        "se_results_count", 
        "keyword_difficulty", 
        "is_lost", 
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
        _dict['serp_item'] = self.serp_item.to_dict() if self.serp_item else None
        _dict['check_url'] = self.check_url
        _dict['serp_item_types'] = self.serp_item_types
        _dict['se_results_count'] = self.se_results_count
        _dict['keyword_difficulty'] = self.keyword_difficulty
        _dict['is_lost'] = self.is_lost
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
            "serp_item": BaseDataforseoLabsApiElementItem.from_dict(obj["serp_item"]) if obj.get("serp_item") is not None else None,
            "check_url": obj.get("check_url"),
            "serp_item_types": obj.get("serp_item_types"),
            "se_results_count": obj.get("se_results_count"),
            "keyword_difficulty": obj.get("keyword_difficulty"),
            "is_lost": obj.get("is_lost"),
            "last_updated_time": obj.get("last_updated_time"),
            "previous_updated_time": obj.get("previous_updated_time"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj