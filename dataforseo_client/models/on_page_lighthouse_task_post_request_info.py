from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class OnPageLighthouseTaskPostRequestInfo(BaseModel):
    """
    OnPageLighthouseTaskPostRequestInfo
    """ # noqa: E501
    url: Optional[StrictStr] = Field(default=None, description=r"target URLrequired fieldtarget page should be specified with its absolute URL (including http:// or https://)example:https://dataforseo.com/")
    for_mobile: Optional[StrictBool] = Field(default=None, description=r"applies mobile emulationoptional fieldif set to true, Lighthouse will use mobile device and screen emulation to test the page against mobile environmentif set to false, the results will be provided for desktopdefault value: false")
    categories: Optional[List[Optional[StrictStr]]] = Field(default=None, description=r"categories of Lighthouse auditsoptional fieldeach category is a collection of audits and audit groups that applies weighting and scoring to the section (see official definition)if you ignore this field, we will return data for all categories unless you specify auditsuse this field to get data for specific categories you indicate herepossible values:seo, performance, best_practices, accessibility")
    audits: Optional[List[Optional[StrictStr]]] = Field(default=None, description=r"Lighthouse auditsoptional fieldaudits are individual tests Lighthouse runs for each specific feature/optimization/metric to produce a numeric score (see official definition)if you ignore this field, we will return data for all auditsuse this field to get data for specific audits you indicate herenote that some audits do not belong to a specific category and are stand-alone page quality measurementsin general, there can be several use cases:1. if you ignore categories, you can use this field to get data for the specified audits onlyfor example, if you ignore 'categories' and specify 'audits': ['metrics/cumulative-layout-shift','metrics/largest-contentful-paint','metrics/total-blocking-time'], you will get data only for these audits2. if you specify a category, you can use this field to additionally receive audits that do not belong to the category(-ies) you specifiedfor example, if you specify 'categories': ['seo'] and 'audits': ['metrics/cumulative-layout-shift','metrics/largest-contentful-paint','metrics/total-blocking-time'], you will get only these audits under 'performance' and all audits under 'seo'you can get the full list of possible audits here")
    version: Optional[StrictStr] = Field(default=None, description=r"lighthouse versionoptional fieldyou can obtain the results specific to a certain Lighthouse version by specifying its numberthe list of available versions is available through the Lighthouse Versions endpoint")
    language_name: Optional[StrictStr] = Field(default=None, description=r"lighthouse language nameoptional fieldyou can receive the list of available languages of the search engine with their language_name by making a separate request to https://api.dataforseo.com/v3/on_page/lighthouse/languagesdefault value:English")
    language_code: Optional[StrictStr] = Field(default=None, description=r"lighthouse language codeoptional fieldyou can receive the list of available languages of the search engine with their language_code by making a separate request to https://api.dataforseo.com/v3/on_page/lighthouse/languagesdefault value:en")
    tag: Optional[StrictStr] = Field(default=None, description=r"user-defined task identifieroptional fieldthe character limit is 255you can use this parameter to identify the task and match it with the resultyou will find the specified tag value in the data object of the response")
    pingback_url: Optional[StrictStr] = Field(default=None, description=r"notification URL of a completed taskoptional fieldwhen a task is completed we will notify you by GET request sent to the URL you have specifiedyou can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the request.example:http://your-server.com/pingscript?id=$idhttp://your-server.com/pingscript?id=$id&tag=$tagNote: special characters in pingback_url will be urlencoded;i.a., the # character will be encoded into %23learn more on our Help Center")
    __properties: ClassVar[List[str]] = [
        "url", 
        "for_mobile", 
        "categories", 
        "audits", 
        "version", 
        "language_name", 
        "language_code", 
        "tag", 
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

        _dict['url'] = self.url
        _dict['for_mobile'] = self.for_mobile
        _dict['categories'] = self.categories
        _dict['audits'] = self.audits
        _dict['version'] = self.version
        _dict['language_name'] = self.language_name
        _dict['language_code'] = self.language_code
        _dict['tag'] = self.tag
        _dict['pingback_url'] = self.pingback_url
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "url": obj.get("url"),
            "for_mobile": obj.get("for_mobile"),
            "categories": obj.get("categories"),
            "audits": obj.get("audits"),
            "version": obj.get("version"),
            "language_name": obj.get("language_name"),
            "language_code": obj.get("language_code"),
            "tag": obj.get("tag"),
            "pingback_url": obj.get("pingback_url"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj