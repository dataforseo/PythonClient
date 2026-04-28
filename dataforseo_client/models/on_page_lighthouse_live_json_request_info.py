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
    url: Optional[StrictStr] = Field(default=None, description=r"target URLrequired fieldtarget page should be specified with its absolute URL (including http:// or https://)example:https://dataforseo.com/")
    for_mobile: Optional[StrictBool] = Field(default=None, description=r"applies mobile emulationoptional fieldif set to true, Lighthouse will use mobile device and screen emulation to test the page against mobile environmentif set to false, the results will be provided for desktopdefault value: false")
    categories: Optional[List[Optional[StrictStr]]] = Field(default=None, description=r"categories of Lighthouse auditsoptional fieldeach category is a collection of audits and audit groups that applies weighting and scoring to the section (see official definition)if you ignore this field, we will return data for all categories unless you specify auditsuse this field to get data for specific categories you indicate herepossible values:seo, performance, best_practices, accessibility")
    audits: Optional[List[Optional[StrictStr]]] = Field(default=None, description=r"Lighthouse auditsoptional fieldaudits are individual tests Lighthouse runs for each specific feature/optimization/metric to produce a numeric score (see official definition);  if you ignore this field, we will return data for all audits;use this field to get data for specific audits you indicate here;Note: that some audits do not belong to a specific category and are stand-alone page quality measurements;in general, there can be several use cases:1. if you ignore categories, you can use this field to get data for the specified audits onlyfor example, if you ignore 'categories' and specify 'audits': ['metrics/cumulative-layout-shift','metrics/largest-contentful-paint','metrics/total-blocking-time'], you will get data only for these audits2. if you specify a category, you can use this field to additionally receive audits that do not belong to the category(-ies) you specifiedfor example, if you specify 'categories': ['seo'] and 'audits': ['metrics/cumulative-layout-shift','metrics/largest-contentful-paint','metrics/total-blocking-time'], you will get only these audits under 'performance' and all audits under 'seo'you can get the full list of possible audits here")
    version: Optional[StrictStr] = Field(default=None, description=r"lighthouse versionoptional fieldyou can obtain the results specific to a certain Lighthouse version by specifying its numberthe list of available versions is available through the Lighthouse Versions endpoint")
    language_name: Optional[StrictStr] = Field(default=None, description=r"lighthouse language nameoptional fieldyou can receive the list of available languages of the search engine with their language_name by making a separate request to https://api.dataforseo.com/v3/on_page/lighthouse/languagesdefault value:English")
    language_code: Optional[StrictStr] = Field(default=None, description=r"lighthouse language codeoptional fieldyou can receive the list of available languages of the search engine with their language_code by making a separate request to https://api.dataforseo.com/v3/on_page/lighthouse/languagesdefault value:en")
    custom_user_agent: Optional[StrictStr] = Field(default=None, description=r"custom user agentoptional fieldspecify the custom user agent used by the browser when running the Lighthouse audit;can be specified with up to 254 characters;")
    browser_screen_width: Optional[StrictInt] = Field(default=None, description=r"browser screen widthoptional fieldset the screen width of the browser used for the Lighthouse audit to emulate a specific device;can be specified within the following range: 240–9999;")
    browser_screen_height: Optional[StrictInt] = Field(default=None, description=r"browser screen heightoptional fieldset the screen height of the browser used for the Lighthouse audit to emulate a specific device;can be specified within the following range: 240–9999;")
    browser_screen_scale_factor: Optional[StrictFloat] = Field(default=None, description=r"browser screen scale factoroptional fieldset the device pixel ratio of the browser used for the Lighthouse audit;can be specified within the following range: 0.5–3;")
    browser_network_throttling_method: Optional[StrictStr] = Field(default=None, description=r"browser network throttling methodoptional fielddefines the method used to apply throttling during the Lighthouse audit;possible vaules:simulate - calculates estimated performance metrics without applying explicit throttling;devtools -  applies the throttling settings specified in browser_network_throttling and browser_cpu_throttling_multiplier;provided - uses the network conditions of the crawling environment;")
    browser_cpu_throttling_multiplier: Optional[StrictFloat] = Field(default=None, description=r"browser CPU throttling multiplierrequired if browser_network_throttling_method is set to devtools;set the CPU throttling multiplier to simulate device performance conditions during the Lighthouse audit;can be specified within the following range: 1–4;Note: this parameter is applied only when browser_network_throttling_method is set to devtools;")
    browser_network_throttling: Optional[StrictStr] = Field(default=None, description=r"browser network throttlingrequired if browser_network_throttling_method is set to devtools;set the network throttling profile to simulate connection speed conditions during the Lighthouse audit;possible values: no_throttling, fast_4g, slow_4g, regular_3g, pc;Note: this parameter is applied only when browser_network_throttling_method is set to devtools;")
    tag: Optional[StrictStr] = Field(default=None, description=r"user-defined task identifieroptional fieldthe character limit is 255you can use this parameter to identify the task and match it with the resultyou will find the specified tag value in the data object of the response")
    __properties: ClassVar[List[str]] = [
        "url", 
        "for_mobile", 
        "categories", 
        "audits", 
        "version", 
        "language_name", 
        "language_code", 
        "custom_user_agent", 
        "browser_screen_width", 
        "browser_screen_height", 
        "browser_screen_scale_factor", 
        "browser_network_throttling_method", 
        "browser_cpu_throttling_multiplier", 
        "browser_network_throttling", 
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
        _dict['custom_user_agent'] = self.custom_user_agent
        _dict['browser_screen_width'] = self.browser_screen_width
        _dict['browser_screen_height'] = self.browser_screen_height
        _dict['browser_screen_scale_factor'] = self.browser_screen_scale_factor
        _dict['browser_network_throttling_method'] = self.browser_network_throttling_method
        _dict['browser_cpu_throttling_multiplier'] = self.browser_cpu_throttling_multiplier
        _dict['browser_network_throttling'] = self.browser_network_throttling
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
            "custom_user_agent": obj.get("custom_user_agent"),
            "browser_screen_width": obj.get("browser_screen_width"),
            "browser_screen_height": obj.get("browser_screen_height"),
            "browser_screen_scale_factor": obj.get("browser_screen_scale_factor"),
            "browser_network_throttling_method": obj.get("browser_network_throttling_method"),
            "browser_cpu_throttling_multiplier": obj.get("browser_cpu_throttling_multiplier"),
            "browser_network_throttling": obj.get("browser_network_throttling"),
            "tag": obj.get("tag"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj