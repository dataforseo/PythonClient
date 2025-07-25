from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class BacklinksBulkNewLostReferringDomainsLiveRequestInfo(BaseModel):
    """
    BacklinksBulkNewLostReferringDomainsLiveRequestInfo
    """ # noqa: E501
    targets: Optional[List[Optional[StrictStr]]] = Field(default=None, description="domains, subdomains or webpages to get  new & lost referring domains for. required field. you can set up to 1000 domains, subdomains or webpages. the domain or subdomain should be specified without https:// and www.. the page should be specified with absolute URL (including http:// or https://). example:. 'targets': [.   'forbes.com',.   'cnn.com',.   'bbc.com',.   'yelp.com',.   'https://www.apple.com/iphone/',.   'https://ahrefs.com/blog/',.   'ibm.com',.   'https://variety.com/',.   'https://stackoverflow.com/',.   'www.trustpilot.com'. ]")
    date_from: Optional[StrictStr] = Field(default=None, description="starting date of the time range. optional field. this field indicates the date which will be used as a threshold for new and lost referring domains;. the referring domains that appeared in our index after the specified date will be considered as new;. the referring domains that weren’t found after the specified date, but were present before, will be considered as lost;. default value: today’s date -(minus) one month;. e.g. if today is 2021-10-13, default date_from will be 2021-09-13.. minimum value equals today’s date -(minus) one year;. e.g. if today is 2021-10-13, minimum date_from will be 2020-10-13.. date format: 'yyyy-mm-dd'. example:. '2021-01-01'")
    tag: Optional[StrictStr] = Field(default=None, description="user-defined task identifier. optional field. the character limit is 255. you can use this parameter to identify the task and match it with the result. you will find the specified tag value in the data object of the response")
    __properties: ClassVar[List[str]] = [
        "targets", 
        "date_from", 
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
        _dict['date_from'] = self.date_from
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
            "date_from": obj.get("date_from"),
            "tag": obj.get("tag"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj