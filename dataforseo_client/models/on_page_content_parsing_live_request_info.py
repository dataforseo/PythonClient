from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class OnPageContentParsingLiveRequestInfo(BaseModel):
    """
    OnPageContentParsingLiveRequestInfo
    """ # noqa: E501
    url: Optional[StrictStr] = Field(default=None, description="URL of the content to parse. required field. URL of the page to parse. example:. https://www.fujielectric.com/")
    custom_user_agent: Optional[StrictStr] = Field(default=None, description="custom user agent. optional field. custom user agent for crawling a website. example: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36. . default value: Mozilla/5.0 (compatible; RSiteAuditor)")
    browser_preset: Optional[StrictStr] = Field(default=None, description="preset for browser screen parameters. optional field. if you use this field, you don’t need to indicate browser_screen_width, browser_screen_height, browser_screen_scale_factor. possible values:. desktop, mobile, tablet. desktop preset will apply the following values:. browser_screen_width: 1920. browser_screen_height: 1080. browser_screen_scale_factor: 1. mobile preset will apply the following values:. browser_screen_width: 390. browser_screen_height: 844. browser_screen_scale_factor: 3. tablet preset will apply the following values:. browser_screen_width: 1024. browser_screen_height: 1366. browser_screen_scale_factor: 2. Note: to use this parameter, set enable_javascript or enable_browser_rendering to true")
    browser_screen_width: Optional[StrictInt] = Field(default=None, description="browser screen width. optional field. you can set a custom browser screen width to perform audit for a particular device;. if you use this field, you don’t need to indicate browser_preset as it will be ignored;. Note: to use this parameter, set enable_javascript or enable_browser_rendering to true. minimum value, in pixels: 240. maximum value, in pixels: 9999")
    browser_screen_height: Optional[StrictInt] = Field(default=None, description="browser screen height. optional field. you can set a custom browser screen height to perform audit for a particular device;. if you use this field, you don’t need to indicate browser_preset as it will be ignored;. Note: to use this parameter, set enable_javascript or enable_browser_rendering to true. minimum value, in pixels: 240. maximum value, in pixels: 9999")
    browser_screen_scale_factor: Optional[StrictFloat] = Field(default=None, description="browser screen scale factor. optional field. you can set a custom browser screen resolution ratio to perform audit for a particular device;. if you use this field, you don’t need to indicate browser_preset as it will be ignored;. Note: to use this parameter, set enable_javascript or enable_browser_rendering to true. minimum value: 0.5. maximum value: 3")
    store_raw_html: Optional[StrictBool] = Field(default=None, description="store HTML of a crawled page. optional field. set to true if you want to get the HTML of the page using the OnPage Raw HTML endpoint. default value: false")
    disable_cookie_popup: Optional[StrictBool] = Field(default=None, description="disable the cookie popup . optional field. set to true if you want to disable the popup requesting cookie consent from the user;. default value:. false")
    accept_language: Optional[StrictStr] = Field(default=None, description="language header for accessing the website. optional field. all locale formats are supported (xx, xx-XX, xxx-XX, etc.). Note: if you do not specify this parameter, some websites may deny access; in this case, pages will be returned with the 'type':'broken in the response array")
    enable_javascript: Optional[StrictBool] = Field(default=None, description="load javascript on a page. optional field. set to true if you want to load the scripts available on a page. default value: false. Note: if you use this parameter, additional charges will apply; learn more about the cost of tasks with this parameter in our help article; the cost can be calculated on the Pricing Page")
    enable_browser_rendering: Optional[StrictBool] = Field(default=None, description="emulate browser rendering to measure Core Web Vitals. optional field. by using this parameter you will be able to emulate a browser when loading a web page;. enable_browser_rendering loads styles, images, fonts, animations, videos, and other resources on a page;. default value: false. set to true to obtain Core Web Vitals (FID, CLS, LCP) metrics in the response;. if you use this field, enable_javascript, and load_resources parameters must be set to true. Note: if you use this parameter, additional charges will apply; learn more about the cost of tasks with this parameter in our help article; the cost can be calculated on the Pricing Page")
    enable_xhr: Optional[StrictBool] = Field(default=None, description="enable XMLHttpRequest on a page. optional field. set to true if you want our crawler to request data from a web server using the XMLHttpRequest object. default value:. false. if you use this field, enable_javascript must be set to true;")
    switch_pool: Optional[StrictBool] = Field(default=None, description="switch proxy pool. optional field. if true, additional proxy pools will be used to obtain the requested data;. the parameter can be used if a multitude of tasks is set simultaneously, resulting in occasional rate-limit and/or site_unreachable errors")
    ip_pool_for_scan: Optional[StrictStr] = Field(default=None, description="proxy pool. optional field. you can choose a location of the proxy pool that will be used to obtain the requested data;. the parameter can be used if page content is inaccessible in one of the locations, resulting in occasional site_unreachable errors. possible values: us, de")
    markdown_view: Optional[StrictBool] = Field(default=None, description="return page content as markdown. optional field. if set to true, the markdown-formatted content of the page will be returned in the page_as_markdown field of the response;. default value: false")
    __properties: ClassVar[List[str]] = [
        "url", 
        "custom_user_agent", 
        "browser_preset", 
        "browser_screen_width", 
        "browser_screen_height", 
        "browser_screen_scale_factor", 
        "store_raw_html", 
        "disable_cookie_popup", 
        "accept_language", 
        "enable_javascript", 
        "enable_browser_rendering", 
        "enable_xhr", 
        "switch_pool", 
        "ip_pool_for_scan", 
        "markdown_view", 
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
        _dict['disable_cookie_popup'] = self.disable_cookie_popup
        _dict['accept_language'] = self.accept_language
        _dict['enable_javascript'] = self.enable_javascript
        _dict['enable_browser_rendering'] = self.enable_browser_rendering
        _dict['enable_xhr'] = self.enable_xhr
        _dict['switch_pool'] = self.switch_pool
        _dict['ip_pool_for_scan'] = self.ip_pool_for_scan
        _dict['markdown_view'] = self.markdown_view
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
            "disable_cookie_popup": obj.get("disable_cookie_popup"),
            "accept_language": obj.get("accept_language"),
            "enable_javascript": obj.get("enable_javascript"),
            "enable_browser_rendering": obj.get("enable_browser_rendering"),
            "enable_xhr": obj.get("enable_xhr"),
            "switch_pool": obj.get("switch_pool"),
            "ip_pool_for_scan": obj.get("ip_pool_for_scan"),
            "markdown_view": obj.get("markdown_view"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj