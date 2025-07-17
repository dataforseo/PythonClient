from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class OnPageLighthouseLiveJsonRequestInfo(BaseModel):
    """
    OnPageLighthouseLiveJsonRequestInfo
    """ # noqa: E501
    url: Optional[StrictStr] = Field(default=None, description="target URL. required field. target page should be specified with its absolute URL (including http:// or https://). example:. https://dataforseo.com/")
    for_mobile: Optional[StrictBool] = Field(default=None, description="applies mobile emulation. optional field. if set to true, Lighthouse will use mobile device and screen emulation to test the page against mobile environment. if set to false, the results will be provided for desktop. default value: false")
    categories: Optional[List[Optional[StrictStr]]] = Field(default=None, description="categories of Lighthouse audits. optional field. each category is a collection of audits and audit groups that applies weighting and scoring to the section (see official definition). if you ignore this field, we will return data for all categories unless you specify audits. use this field to get data for specific categories you indicate here. possible values:. seo, pwa, performance, best_practices, accessibility")
    audits: Optional[List[Optional[StrictStr]]] = Field(default=None, description="Lighthouse audits. optional field. audits are individual tests Lighthouse runs for each specific feature/optimization/metric to produce a numeric score (see official definition);  . if you ignore this field, we will return data for all audits;. use this field to get data for specific audits you indicate here;. Note: that some audits do not belong to a specific category and are stand-alone page quality measurements;. in general, there can be several use cases:. 1. if you ignore categories, you can use this field to get data for the specified audits only. for example, if you ignore 'categories' and specify 'audits': ['metrics/cumulative-layout-shift','metrics/largest-contentful-paint','metrics/total-blocking-time'], you will get data only for these audits. 2. if you specify a category, you can use this field to additionally receive audits that do not belong to the category(-ies) you specified. for example, if you specify 'categories': ['seo'] and 'audits': ['metrics/cumulative-layout-shift','metrics/largest-contentful-paint','metrics/total-blocking-time'], you will get only these audits under “performance” and all audits under “seo”. you can get the full list of possible audits here")
    version: Optional[StrictStr] = Field(default=None, description="lighthouse version. optional field. you can obtain the results specific to a certain Lighthouse version by specifying its number. the list of available versions is available through the Lighthouse Versions endpoint")
    language_name: Optional[StrictStr] = Field(default=None, description="lighthouse language name. optional field. you can receive the list of available languages of the search engine with their language_name by making a separate request to https://api.dataforseo.com/v3/on_page/lighthouse/languages. default value:. English")
    language_code: Optional[StrictStr] = Field(default=None, description="lighthouse language code. optional field. you can receive the list of available languages of the search engine with their language_code by making a separate request to https://api.dataforseo.com/v3/on_page/lighthouse/languages. default value:. en")
    tag: Optional[StrictStr] = Field(default=None, description="user-defined task identifier. optional field. the character limit is 255. you can use this parameter to identify the task and match it with the result. you will find the specified tag value in the data object of the response")
    __properties: ClassVar[List[str]] = [
        "url", 
        "for_mobile", 
        "categories", 
        "audits", 
        "version", 
        "language_name", 
        "language_code", 
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

        _dict['url'] = self.url
        _dict['for_mobile'] = self.for_mobile
        _dict['categories'] = self.categories
        _dict['audits'] = self.audits
        _dict['version'] = self.version
        _dict['language_name'] = self.language_name
        _dict['language_code'] = self.language_code
        _dict['tag'] = self.tag
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
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj