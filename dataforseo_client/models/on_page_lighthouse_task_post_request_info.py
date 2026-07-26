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
    url: Optional[StrictStr] = Field(default=None, description=r"*target URL*. **required field**. target page should be specified with its absolute URL (including http:// or https://). example:. `https://dataforseo.com/`")
    for_mobile: Optional[StrictBool] = Field(default=None, description=r"*applies mobile emulation*. optional field. if set to `true`, Lighthouse will use mobile device and screen emulation to test the page against mobile environment. if set to `false`, the results will be provided for desktop. default value: `false`")
    categories: Optional[List[Optional[StrictStr]]] = Field(default=None, description=r"*categories of Lighthouse audits*. optional field. each category is a collection of audits and audit groups that applies weighting and scoring to the section ([see official definition](https://github.com/GoogleChrome/lighthouse/blob/master/docs/architecture.md#auditreport-terminology))**if you ignore this field, we will return data for all categories unless you specify `audits`**. use this field to get data for specific categories you indicate here. possible values:. `seo`, `performance`, `best_practices`, `accessibility`")
    audits: Optional[List[Optional[StrictStr]]] = Field(default=None, description=r"*Lighthouse audits*. optional field. audits are individual tests Lighthouse runs for each specific feature/optimization/metric to produce a numeric score ([see official definition](https://github.com/GoogleChrome/lighthouse/blob/master/docs/architecture.md#components--terminology))**if you ignore this field, we will return data for all audits**. use this field to get data for specific audits you indicate here. **note** that some audits do not belong to a specific category and are stand-alone page quality measurements. in general, there can be several use cases:. 1. if you ignore `categories`, you can use this field to get data for the specified audits only. for example, if you ignore `'categories'` and specify `'audits': ['metrics/cumulative-layout-shift','metrics/largest-contentful-paint','metrics/total-blocking-time']`, you will get data only for these audits. 2. if you specify a category, you can use this field to additionally receive audits that do not belong to the category(-ies) you specified. for example, if you specify `'categories': ['seo']` and `'audits': ['metrics/cumulative-layout-shift','metrics/largest-contentful-paint','metrics/total-blocking-time']`, you will get only these audits under 'performance' and all audits under 'seo'. you can get [the full list of possible audits here](/v3/on_page/lighthouse/audits/)")
    version: Optional[StrictStr] = Field(default=None, description=r"*lighthouse version*. optional field. you can obtain the results specific to a certain Lighthouse version by specifying its number. the list of available versions is available through the [Lighthouse Versions endpoint](/v3/on_page/lighthouse/versions/)")
    language_name: Optional[StrictStr] = Field(default=None, description=r"*lighthouse language name*. optional field. you can receive the list of available languages of the search engine with their `language_name` by making a separate request to `https://api.dataforseo.com/v3/on_page/lighthouse/languages`. default value:. `English`")
    language_code: Optional[StrictStr] = Field(default=None, description=r"*lighthouse language code*. optional field. you can receive the list of available languages of the search engine with their `language_code` by making a separate request to `https://api.dataforseo.com/v3/on_page/lighthouse/languages`. default value:. `en`")
    custom_user_agent: Optional[StrictStr] = Field(default=None, description=r"*custom user agent*. optional field. specify the custom user agent used by the browser when running the Lighthouse audit;. can be specified with up to 254 characters;")
    browser_screen_width: Optional[StrictInt] = Field(default=None, description=r"*browser screen width*. optional field. set the screen width of the browser used for the Lighthouse audit to emulate a specific device;. can be specified within the following range: `240–9999`;")
    browser_screen_height: Optional[StrictInt] = Field(default=None, description=r"*browser screen height*. optional field. set the screen height of the browser used for the Lighthouse audit to emulate a specific device;. can be specified within the following range: `240–9999`;")
    browser_screen_scale_factor: Optional[StrictFloat] = Field(default=None, description=r"*browser screen scale factor*. optional field. set the device pixel ratio of the browser used for the Lighthouse audit;. can be specified within the following range: `0.5–3`;")
    browser_network_throttling_method: Optional[StrictStr] = Field(default=None, description=r"*browser network throttling method*. optional field. defines the method used to apply throttling during the Lighthouse audit;. possible vaules:. `simulate` - calculates estimated performance metrics without applying explicit throttling;. `devtools` -  applies the throttling settings specified in `browser_network_throttling` and `browser_cpu_throttling_multiplier`;. `provided` - uses the network conditions of the crawling environment;")
    browser_cpu_throttling_multiplier: Optional[StrictFloat] = Field(default=None, description=r"*browser CPU throttling multiplier*. **required if `browser_network_throttling_method` is set to `devtools`;**. set the CPU throttling multiplier to simulate device performance conditions during the Lighthouse audit;. can be specified within the following range: `1–4`;. **Note:** this parameter is applied only when `browser_network_throttling_method` is set to `devtools`;")
    browser_network_throttling: Optional[StrictStr] = Field(default=None, description=r"*browser network throttling*. **required if `browser_network_throttling_method` is set to `devtools`;**. set the network throttling profile to simulate connection speed conditions during the Lighthouse audit;. possible values: `no_throttling`, `fast_4g`, `slow_4g`, `regular_3g`, `pc`;. **Note:** this parameter is applied only when `browser_network_throttling_method` is set to `devtools`;")
    tag: Optional[StrictStr] = Field(default=None, description=r"*user-defined task identifier*. optional field. *the character limit is 255*. you can use this parameter to identify the task and match it with the result. you will find the specified `tag` value in the `data` object of the response")
    pingback_url: Optional[StrictStr] = Field(default=None, description=r"*notification URL of a completed task*. optional field. when a task is completed we will notify you by GET request sent to the URL you have specified. you can use the ‘$id’ string as a `$id` variable and ‘$tag’ as urlencoded `$tag` variable. We will set the necessary values before sending the request.. example:. `http://your-server.com/pingscript?id=$id`. `http://your-server.com/pingscript?id=$id&tag=$tag`. **Note:** special characters in `pingback_url` will be urlencoded;. i.a., the `#` character will be encoded into `%23`learn more on our [Help Center](https://dataforseo.com/help-center/pingbacks-postbacks-with-dataforseo-api)")
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
        _dict['custom_user_agent'] = self.custom_user_agent
        _dict['browser_screen_width'] = self.browser_screen_width
        _dict['browser_screen_height'] = self.browser_screen_height
        _dict['browser_screen_scale_factor'] = self.browser_screen_scale_factor
        _dict['browser_network_throttling_method'] = self.browser_network_throttling_method
        _dict['browser_cpu_throttling_multiplier'] = self.browser_cpu_throttling_multiplier
        _dict['browser_network_throttling'] = self.browser_network_throttling
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
            "custom_user_agent": obj.get("custom_user_agent"),
            "browser_screen_width": obj.get("browser_screen_width"),
            "browser_screen_height": obj.get("browser_screen_height"),
            "browser_screen_scale_factor": obj.get("browser_screen_scale_factor"),
            "browser_network_throttling_method": obj.get("browser_network_throttling_method"),
            "browser_cpu_throttling_multiplier": obj.get("browser_cpu_throttling_multiplier"),
            "browser_network_throttling": obj.get("browser_network_throttling"),
            "tag": obj.get("tag"),
            "pingback_url": obj.get("pingback_url"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj