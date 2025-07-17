from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class BacklinksTimeseriesSummaryLiveRequestInfo(BaseModel):
    """
    BacklinksTimeseriesSummaryLiveRequestInfo
    """ # noqa: E501
    target: Optional[StrictStr] = Field(default=None, description="domain to get data for. required field. a domain should be specified without https:// and www.. example:. 'forbes.com'")
    date_from: Optional[StrictStr] = Field(default=None, description="starting date of the time range. optional field. this field indicates the date which will be used as a threshold for summary data;. minimum value: 2019-01-30. maximum value shouldn’t exceed the date specified in the date_to. date format: 'yyyy-mm-dd'. example:. '2021-01-01'")
    date_to: Optional[StrictStr] = Field(default=None, description="ending date of the time range. optional field. if you don’t specify this field, the today’s date will be used by default. minimum value shouldn’t preceed the date specified in the date_from. maximum value: today’s date. date format: 'yyyy-mm-dd'. example:. '2021-01-15'")
    group_range: Optional[StrictStr] = Field(default=None, description="time range which will be used to group the results. optional field. default value: month. possible values: day, week, month, year. note: for day, we will return items corresponding to all dates between and including date_from and date_to;. for week/month/year, we will return items corresponding to full weeks/months/years, where each item will indicate the last day of the week/month/year. for example, if you specify:. 'group_range': 'month',. 'date_from': '2022-03-23',. 'date_to': '2022-05-13'. we will return items falling between 2022-03-01 and 2022-05-31, namely, three items corresponding to the following dates: 2022-03-31, 2022-04-30, 2022-05-31. if there is no data for a certain  day/week/month/year, we will return 0")
    include_subdomains: Optional[StrictBool] = Field(default=None, description="indicates if the subdomains of the target will be included in the search. optional field. if set to false, the subdomains will be ignored. default value: true")
    rank_scale: Optional[StrictStr] = Field(default=None, description="defines the scale used for calculating and displaying the rank, domain_from_rank, and page_from_rank values. optional field. you can use this parameter to choose whether rank values are presented on a 0–100 or 0–1000 scale. possible values:. one_hundred — rank values are displayed on a 0–100 scale. one_thousand — rank values are displayed on a 0–1000 scale. default value: one_thousand. learn more about how this parameter works and how ranking metrics are calculated in this Help Center article")
    tag: Optional[StrictStr] = Field(default=None, description="user-defined task identifier. optional field. the character limit is 255. you can use this parameter to identify the task and match it with the result. you will find the specified tag value in the data object of the response")
    __properties: ClassVar[List[str]] = [
        "target", 
        "date_from", 
        "date_to", 
        "group_range", 
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

        _dict['target'] = self.target
        _dict['date_from'] = self.date_from
        _dict['date_to'] = self.date_to
        _dict['group_range'] = self.group_range
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
            "target": obj.get("target"),
            "date_from": obj.get("date_from"),
            "date_to": obj.get("date_to"),
            "group_range": obj.get("group_range"),
            "include_subdomains": obj.get("include_subdomains"),
            "rank_scale": obj.get("rank_scale"),
            "tag": obj.get("tag"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj