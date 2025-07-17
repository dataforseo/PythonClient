from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class BusinessDataTrustpilotReviewsTaskPostRequestInfo(BaseModel):
    """
    BusinessDataTrustpilotReviewsTaskPostRequestInfo
    """ # noqa: E501
    domain: Optional[StrictStr] = Field(default=None, description="domain of the local establishment. required field. domain of the local establishment on Trustpilot;. you can find the domain in the URL of every business listed on Trustpilot. example:. www.thepearlsource.com. https://www.trustpilot.com/review/www.thepearlsource.com")
    sort_by: Optional[StrictStr] = Field(default=None, description="results sorting parameter. optional field. you can use this field to sort the results;. possible sorting parameters:. recency — most recent reviews first;. relevance — most relevant reviews first;. default value: relevance")
    priority: Optional[StrictInt] = Field(default=None, description="task priority. optional field. can take the following values:. 1 – normal execution priority (set by default). 2 – high execution priority. You will be additionally charged for the tasks with high execution priority.. The cost can be calculated on the Pricing page.")
    depth: Optional[StrictInt] = Field(default=None, description="parsing depth. optional field. number of reviews to be returned from the API response. we strongly recommend setting the parsing depth in the multiples of twenty, because our system processes twenty reviews in a row. default value: 20. maximum value: 25000")
    tag: Optional[StrictStr] = Field(default=None, description="user-defined task identifier. optional field. the character limit is 255. you can use this parameter to identify the task and match it with the result. you will find the specified tag value in the data object of the response")
    postback_url: Optional[StrictStr] = Field(default=None, description="return URL for sending task results. optional field. once the task is completed, we will send a POST request with its results compressed in the gzip format to the postback_url you specified. you can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the request.. example:. http://your-server.com/postbackscript?id=$id. http://your-server.com/postbackscript?id=$id&tag=$tag. Note: special characters in postback_url will be urlencoded;. i.a., the # character will be encoded into %23. learn more on our Help Center")
    pingback_url: Optional[StrictStr] = Field(default=None, description="notification URL of a completed task. optional field. when a task is completed we will notify you by GET request sent to the URL you have specified. you can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the request.. example:. http://your-server.com/pingscript?id=$id. http://your-server.com/pingscript?id=$id&tag=$tag. Note: special characters in pingback_url will be urlencoded;. i.a., the # character will be encoded into %23. learn more on our Help Center")
    __properties: ClassVar[List[str]] = [
        "domain", 
        "sort_by", 
        "priority", 
        "depth", 
        "tag", 
        "postback_url", 
        "pingback_url", 
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

        _dict['domain'] = self.domain
        _dict['sort_by'] = self.sort_by
        _dict['priority'] = self.priority
        _dict['depth'] = self.depth
        _dict['tag'] = self.tag
        _dict['postback_url'] = self.postback_url
        _dict['pingback_url'] = self.pingback_url
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "domain": obj.get("domain"),
            "sort_by": obj.get("sort_by"),
            "priority": obj.get("priority"),
            "depth": obj.get("depth"),
            "tag": obj.get("tag"),
            "postback_url": obj.get("postback_url"),
            "pingback_url": obj.get("pingback_url"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj