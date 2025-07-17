from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class Advertiser(BaseModel):
    """
    Advertiser
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    advertiser_id: Optional[StrictStr] = Field(default=None, description="unique identifier of the advertiser account. can be used to obtain data on advertising campaigns from the Google Ads Search endpoint")
    location: Optional[StrictStr] = Field(default=None, description="location of the advertiser account. country code associated with the advertiser account")
    verified: Optional[StrictBool] = Field(default=None, description="verified advertiser account. equals true if advertiser account is verified by Google Ads")
    approx_ads_count: Optional[StrictInt] = Field(default=None, description="ads count. the approximate number of ads that are run by the advertiser account across all available Google Ads platforms")
    __properties: ClassVar[List[str]] = [
        "type", 
        "advertiser_id", 
        "location", 
        "verified", 
        "approx_ads_count", 
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
        _dict['advertiser_id'] = self.advertiser_id
        _dict['location'] = self.location
        _dict['verified'] = self.verified
        _dict['approx_ads_count'] = self.approx_ads_count
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "advertiser_id": obj.get("advertiser_id"),
            "location": obj.get("location"),
            "verified": obj.get("verified"),
            "approx_ads_count": obj.get("approx_ads_count"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj