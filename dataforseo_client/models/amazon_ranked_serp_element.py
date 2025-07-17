from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.amazon_info import AmazonInfo



class AmazonRankedSerpElement(BaseModel):
    """
    AmazonRankedSerpElement
    """ # noqa: E501
    se_type: Optional[StrictStr] = Field(default=None, description="search engine type")
    serp_item: Optional[AmazonInfo] = Field(default=None, description="contains data on the SERP element. the list of supported SERP elements can be found below")
    check_url: Optional[StrictStr] = Field(default=None, description="direct URL to Amazon results. you can use it to make sure that we provided accurate results")
    serp_item_types: Optional[List[Optional[StrictStr]]] = Field(default=None, description="direct URL to Amazon results. contains types of all search results (items) found in the returned SERP;. possible item types:. amazon_serp, amazon_paid, editorial_recommendations, top_rated_from_our_brands, related_searches")
    se_results_count: Optional[StrictInt] = Field(default=None, description="total number of results in Amazon SERP")
    last_updated_time: Optional[StrictStr] = Field(default=None, description="date and time when SERP data was last updated. in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”. example:. 2019-11-15 12:57:46 +00:00")
    previous_updated_time: Optional[StrictStr] = Field(default=None, description="previous to the most recent update of SERP data. in the ISO 8601 format: “YYYY-MM-DDThh:mm:ss.sssssssZ”. example:. 2020-09-12T00:07:43.0733218Z")
    __properties: ClassVar[List[str]] = [
        "se_type", 
        "serp_item", 
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
        _dict['serp_item'] = self.serp_item.to_dict() if self.serp_item else None
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
            "serp_item": AmazonInfo.from_dict(obj["serp_item"]) if obj.get("serp_item") is not None else None,
            "check_url": obj.get("check_url"),
            "serp_item_types": obj.get("serp_item_types"),
            "se_results_count": obj.get("se_results_count"),
            "last_updated_time": obj.get("last_updated_time"),
            "previous_updated_time": obj.get("previous_updated_time"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj