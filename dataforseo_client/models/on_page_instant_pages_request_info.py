from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class OnPageInstantPagesRequestInfo(BaseModel):
    """
    OnPageInstantPagesRequestInfo
    """ # noqa: E501
    url: Optional[StrictStr] = Field(default=None, description="target page url. required field. absolute URL of the target page;. Note #1: results will be returned for the specified URL only;. Note #2: to prevent denial-of-service events, tasks that contain a duplicate crawl host will be returned with a 40501 error;. to prevent this error from occurring, avoid setting tasks with the same domain if at least one of your previous tasks with this domain (including a page URL on the domain) is still in a crawling queue")
    custom_user_agent: Optional[StrictStr] = Field(default=None, description="custom user agent. optional field. custom user agent for crawling a website. example: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36. . default value: Mozilla/5.0 (compatible; RSiteAuditor)")
    browser_preset: Optional[StrictStr] = Field(default=None, description="preset for browser screen parameters. optional field. if you use this field, you don’t need to indicate browser_screen_width, browser_screen_height, browser_screen_scale_factorpossible values:. desktop, mobile, tabletdesktop preset will apply the following values:. browser_screen_width: 1920. browser_screen_height: 1080. browser_screen_scale_factor: 1. mobile preset will apply the following values:. browser_screen_width: 390. browser_screen_height: 844. browser_screen_scale_factor: 3. tablet preset will apply the following values:. browser_screen_width: 1024. browser_screen_height: 1366. browser_screen_scale_factor: 2. Note: to use this parameter, set enable_javascript or enable_browser_rendering to true")
    browser_screen_width: Optional[StrictInt] = Field(default=None, description="browser screen width. optional field. you can set a custom browser screen width to perform audit for a particular device;. if you use this field, you don’t need to indicate browser_preset as it will be ignored;Note: to use this parameter, set enable_javascript or enable_browser_rendering to trueminimum value, in pixels: 240. maximum value, in pixels: 9999")
    browser_screen_height: Optional[StrictInt] = Field(default=None, description="browser screen height. optional field. you can set a custom browser screen height to perform audit for a particular device;. if you use this field, you don’t need to indicate browser_preset as it will be ignored;Note: to use this parameter, set enable_javascript or enable_browser_rendering to trueminimum value, in pixels: 240. maximum value, in pixels: 9999")
    browser_screen_scale_factor: Optional[StrictFloat] = Field(default=None, description="browser screen scale factor. optional field. you can set a custom browser screen resolution ratio to perform audit for a particular device;. if you use this field, you don’t need to indicate browser_preset as it will be ignored;Note: to use this parameter, set enable_javascript or enable_browser_rendering to trueminimum value: 0.5. maximum value: 3")
    store_raw_html: Optional[StrictBool] = Field(default=None, description="store HTML of a crawled page. optional field. set to true if you want get the HTML of the page using the OnPage Raw HTML endpoint. default value: false")
    accept_language: Optional[StrictStr] = Field(default=None, description="language header for accessing the website. optional field. all locale formats are supported (xx, xx-XX, xxx-XX, etc.). Note: if you do not specify this parameter, some websites may deny access; in this case, pages will be returned with the 'type':'broken in the response array")
    load_resources: Optional[StrictBool] = Field(default=None, description="load resources. optional field. set to true if you want to load image, stylesheets, scripts, and broken resources. default value: false. Note: if you use this parameter, additional charges will apply; learn more about the cost of tasks with this parameter in our help article; the cost can be calculated on the Pricing Page")
    enable_javascript: Optional[StrictBool] = Field(default=None, description="load javascript on a page. optional field. set to true if you want to load the scripts available on a page. default value: false. Note: if you use this parameter, additional charges will apply; learn more about the cost of tasks with this parameter in our help article; the cost can be calculated on the Pricing Page")
    enable_browser_rendering: Optional[StrictBool] = Field(default=None, description="emulate browser rendering to measure Core Web Vitals. optional field. by using this parameter you will be able to emulate a browser when loading a web page;. enable_browser_rendering loads styles, images, fonts, animations, videos, and other resources on a page;. default value: false. set to true to obtain Core Web Vitals (FID, CLS, LCP) metrics in the response;. if you use this field, parameters enable_javascript, and load_resources are enabled automatically;. Note: if you use this parameter, additional charges will apply; learn more about the cost of tasks with this parameter in our help article; the cost can be calculated on the Pricing Page")
    disable_cookie_popup: Optional[StrictBool] = Field(default=None, description="disable the cookie popup . optional field. set to true if you want to disable the popup requesting cookie consent from the user;. default value:. false")
    return_despite_timeout: Optional[StrictBool] = Field(default=None, description="return data on pages despite the timeout error. optional field. if true, the data will be provided on pages that failed to load within 120 seconds and responded with a timeout error;. default value: false")
    enable_xhr: Optional[StrictBool] = Field(default=None, description="enable XMLHttpRequest on a page. optional field. set to true if you want our crawler to request data from a web server using the XMLHttpRequest object. default value:. falseif you use this field, enable_javascript must be set to true;")
    custom_js: Optional[StrictStr] = Field(default=None, description="custom javascript. optional fieldNote that the execution time for the script you enter here should be 700 ms maximum;. for example, you can use the following JS snippet to check if the website contains Google Tag Manager as a scr attribute:. let meta = { haveGoogleAnalytics: false, haveTagManager: false };\r\nfor (var i = 0; i < document.scripts.length; i++) {\r\n let src = document.scripts[i].getAttribute(\'src\');\r\n if (src != undefined) {\r\n if (src.indexOf(\'analytics.js\') >= 0)\r\n      meta.haveGoogleAnalytics = true;\r\n\tif (src.indexOf(\'gtm.js\') >= 0)\r\n      meta.haveTagManager = true;\r\n  }\r\n}\r\nmeta;the returned value depends on what you specified in this field. For instance, if you specify the following script:. meta = {}; meta.url = document.URL; meta.test = 'test'; meta;. as a response you will receive the following data:. 'custom_js_response': {. 'url': 'https://dataforseo.com/',. 'test': 'test'. }. Note: if you use this parameter, additional charges will apply; learn more about the cost of tasks with this parameter in our help article; the cost can be calculated on the Pricing Page")
    validate_micromarkup: Optional[StrictBool] = Field(default=None, description="enable microdata validation. optional field. if set to true, you can use the OnPage API Microdata endpoint with the id of the task;. default value: false")
    check_spell: Optional[StrictBool] = Field(default=None, description="check spelling. optional field. set to true to check spelling on a website using Hunspell library. default value: false")
    checks_threshold: Optional[Dict[str, Optional[StrictInt]]] = Field(default=None, description="custom threshold values for checks. optional field. you can specify custom threshold values for the parameters included in the checks array of OnPage API responses;. Note: only integer threshold values can be modified;")
    switch_pool: Optional[StrictBool] = Field(default=None, description="switch proxy pool. optional field. if true, additional proxy pools will be used to obtain the requested data;. the parameter can be used if a multitude of tasks is set simultaneously, resulting in occasional rate-limit and/or site_unreachable errors")
    ip_pool_for_scan: Optional[StrictStr] = Field(default=None, description="proxy pool. optional field. you can choose a location of the proxy pool that will be used to obtain the requested data;. the parameter can be used if page content is inaccessible in one of the locations, resulting in occasional site_unreachable errors. possible values: us, de")
    __properties: ClassVar[List[str]] = [
        "url", 
        "custom_user_agent", 
        "browser_preset", 
        "browser_screen_width", 
        "browser_screen_height", 
        "browser_screen_scale_factor", 
        "store_raw_html", 
        "accept_language", 
        "load_resources", 
        "enable_javascript", 
        "enable_browser_rendering", 
        "disable_cookie_popup", 
        "return_despite_timeout", 
        "enable_xhr", 
        "custom_js", 
        "validate_micromarkup", 
        "check_spell", 
        "checks_threshold", 
        "switch_pool", 
        "ip_pool_for_scan", 
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
        _dict['custom_user_agent'] = self.custom_user_agent
        _dict['browser_preset'] = self.browser_preset
        _dict['browser_screen_width'] = self.browser_screen_width
        _dict['browser_screen_height'] = self.browser_screen_height
        _dict['browser_screen_scale_factor'] = self.browser_screen_scale_factor
        _dict['store_raw_html'] = self.store_raw_html
        _dict['accept_language'] = self.accept_language
        _dict['load_resources'] = self.load_resources
        _dict['enable_javascript'] = self.enable_javascript
        _dict['enable_browser_rendering'] = self.enable_browser_rendering
        _dict['disable_cookie_popup'] = self.disable_cookie_popup
        _dict['return_despite_timeout'] = self.return_despite_timeout
        _dict['enable_xhr'] = self.enable_xhr
        _dict['custom_js'] = self.custom_js
        _dict['validate_micromarkup'] = self.validate_micromarkup
        _dict['check_spell'] = self.check_spell
        _dict['checks_threshold'] = self.checks_threshold
        _dict['switch_pool'] = self.switch_pool
        _dict['ip_pool_for_scan'] = self.ip_pool_for_scan
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "url": obj.get("url"),
            "custom_user_agent": obj.get("custom_user_agent"),
            "browser_preset": obj.get("browser_preset"),
            "browser_screen_width": obj.get("browser_screen_width"),
            "browser_screen_height": obj.get("browser_screen_height"),
            "browser_screen_scale_factor": obj.get("browser_screen_scale_factor"),
            "store_raw_html": obj.get("store_raw_html"),
            "accept_language": obj.get("accept_language"),
            "load_resources": obj.get("load_resources"),
            "enable_javascript": obj.get("enable_javascript"),
            "enable_browser_rendering": obj.get("enable_browser_rendering"),
            "disable_cookie_popup": obj.get("disable_cookie_popup"),
            "return_despite_timeout": obj.get("return_despite_timeout"),
            "enable_xhr": obj.get("enable_xhr"),
            "custom_js": obj.get("custom_js"),
            "validate_micromarkup": obj.get("validate_micromarkup"),
            "check_spell": obj.get("check_spell"),
            "checks_threshold": obj.get("checks_threshold"),
            "switch_pool": obj.get("switch_pool"),
            "ip_pool_for_scan": obj.get("ip_pool_for_scan"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj