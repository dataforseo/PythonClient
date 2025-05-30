# coding: utf-8

"""
    DataForSEO API documentation

    DataForSEO API is the starting point on your journey towards building powerful SEO software. With DataForSEO you can get all the data you need to build an efficient application while also saving your time and budget. DataForSEO API is using the REST technology for interchanging data between your application and our service. The data exchange is made through the widely used HTTP protocol, which allows applying our API to almost all programming languages.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class AvgBacklinksInfo(BaseModel):
    """
    AvgBacklinksInfo
    """ # noqa: E501
    se_type: Optional[StrictStr] = Field(default=None, description="search engine type")
    backlinks: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="average number of backlinks")
    dofollow: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="average number of dofollow links")
    referring_pages: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="average number of referring pages")
    referring_domains: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="average number of referring domains")
    referring_main_domains: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="average number of referring main domains")
    rank: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="average rank learn more about the metric and its calculation formula in this help center article")
    main_domain_rank: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="average main domain rank learn more about the metric and its calculation formula in this help center article")
    last_updated_time: Optional[StrictStr] = Field(default=None, description="date and time when the dataset was updated in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00")
    __properties: ClassVar[List[str]] = ["se_type", "backlinks", "dofollow", "referring_pages", "referring_domains", "referring_main_domains", "rank", "main_domain_rank", "last_updated_time"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of AvgBacklinksInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if se_type (nullable) is None
        # and model_fields_set contains the field
        if self.se_type is None and "se_type" in self.model_fields_set:
            _dict['se_type'] = None

        # set to None if backlinks (nullable) is None
        # and model_fields_set contains the field
        if self.backlinks is None and "backlinks" in self.model_fields_set:
            _dict['backlinks'] = None

        # set to None if dofollow (nullable) is None
        # and model_fields_set contains the field
        if self.dofollow is None and "dofollow" in self.model_fields_set:
            _dict['dofollow'] = None

        # set to None if referring_pages (nullable) is None
        # and model_fields_set contains the field
        if self.referring_pages is None and "referring_pages" in self.model_fields_set:
            _dict['referring_pages'] = None

        # set to None if referring_domains (nullable) is None
        # and model_fields_set contains the field
        if self.referring_domains is None and "referring_domains" in self.model_fields_set:
            _dict['referring_domains'] = None

        # set to None if referring_main_domains (nullable) is None
        # and model_fields_set contains the field
        if self.referring_main_domains is None and "referring_main_domains" in self.model_fields_set:
            _dict['referring_main_domains'] = None

        # set to None if rank (nullable) is None
        # and model_fields_set contains the field
        if self.rank is None and "rank" in self.model_fields_set:
            _dict['rank'] = None

        # set to None if main_domain_rank (nullable) is None
        # and model_fields_set contains the field
        if self.main_domain_rank is None and "main_domain_rank" in self.model_fields_set:
            _dict['main_domain_rank'] = None

        # set to None if last_updated_time (nullable) is None
        # and model_fields_set contains the field
        if self.last_updated_time is None and "last_updated_time" in self.model_fields_set:
            _dict['last_updated_time'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AvgBacklinksInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "se_type": obj.get("se_type"),
            "backlinks": obj.get("backlinks"),
            "dofollow": obj.get("dofollow"),
            "referring_pages": obj.get("referring_pages"),
            "referring_domains": obj.get("referring_domains"),
            "referring_main_domains": obj.get("referring_main_domains"),
            "rank": obj.get("rank"),
            "main_domain_rank": obj.get("main_domain_rank"),
            "last_updated_time": obj.get("last_updated_time")
        })
        return _obj


