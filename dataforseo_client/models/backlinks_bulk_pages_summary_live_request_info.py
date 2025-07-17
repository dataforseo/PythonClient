from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class BacklinksBulkPagesSummaryLiveRequestInfo(BaseModel):
    """
    BacklinksBulkPagesSummaryLiveRequestInfo
    """ # noqa: E501
    targets: Optional[List[Optional[StrictStr]]] = Field(default=None, description="domains, subdomains or webpages to get summary data for. required field. a domain or a subdomain should be specified without https:// and www.. a page should be specified with absolute URL (including http:// or https://). you can specify up to 1000 pages, domains, or subdomains in each request.. note that the URLs you set in a single request cannot belong to more than 100 different domains.")
    include_subdomains: Optional[StrictBool] = Field(default=None, description="indicates if the subdomains of the target will be included in the search. optional field. if set to false, the subdomains will be ignored. default value: true")
    rank_scale: Optional[StrictStr] = Field(default=None, description="defines the scale used for calculating and displaying the rank, domain_from_rank, and page_from_rank values. optional field. you can use this parameter to choose whether rank values are presented on a 0–100 or 0–1000 scale. possible values:. one_hundred — rank values are displayed on a 0–100 scale. one_thousand — rank values are displayed on a 0–1000 scale. default value: one_thousand. learn more about how this parameter works and how ranking metrics are calculated in this Help Center article")
    tag: Optional[StrictStr] = Field(default=None, description="user-defined task identifier. optional field. the character limit is 255. you can use this parameter to identify the task and match it with the result. you will find the specified tag value in the data object of the response")
    __properties: ClassVar[List[str]] = [
        "targets", 
        "include_subdomains", 
        "rank_scale", 
        "tag", 
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

        _dict['targets'] = self.targets
        _dict['include_subdomains'] = self.include_subdomains
        _dict['rank_scale'] = self.rank_scale
        _dict['tag'] = self.tag
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "targets": obj.get("targets"),
            "include_subdomains": obj.get("include_subdomains"),
            "rank_scale": obj.get("rank_scale"),
            "tag": obj.get("tag"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj