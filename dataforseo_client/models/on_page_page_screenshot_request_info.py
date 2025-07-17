from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class OnPagePageScreenshotRequestInfo(BaseModel):
    """
    OnPagePageScreenshotRequestInfo
    """ # noqa: E501
    url: Optional[StrictStr] = Field(default=None, description="page url. required field. absolute URL of the page to snap. note: if the URL you indicate here returns a 404 status code or the indicated value is not a valid URL, you will obtain 'error_message':'Screenshot is empty' in the response array")
    accept_language: Optional[StrictStr] = Field(default=None, description="language header for accessing the website. optional field. all locale formats are supported (xx, xx-XX, xxx-XX, etc.). note: if you do not specify this parameter, some websites may deny access; in this case, you will obtain 'error_message':'Screenshot is empty' in the response array")
    custom_user_agent: Optional[StrictStr] = Field(default=None, description="custom user agent. optional field. custom user agent for crawling a website. example: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36. . default value: Mozilla/5.0 (compatible; RSiteAuditor)")
    browser_preset: Optional[StrictStr] = Field(default=None, description="preset for browser screen parameters. optional field. if you use this field, you don’t need to indicate browser_screen_width, browser_screen_height, browser_screen_scale_factor. possible values:. desktop, mobile, tablet. desktop preset will apply the following values:. browser_screen_width: 1920. browser_screen_height: 1080. browser_screen_scale_factor: 1. mobile preset will apply the following values:. browser_screen_width: 390. browser_screen_height: 844. browser_screen_scale_factor: 3. tablet preset will apply the following values:. browser_screen_width: 1024. browser_screen_height: 1366. browser_screen_scale_factor: 2. Note: in this endpoint, the enable_browser_rendering, enable_javascript, load_resources, and enable_xhr parameters are always enabled.")
    browser_screen_width: Optional[StrictInt] = Field(default=None, description="browser screen width. optional field. you can set a custom browser screen width to perform audit for a particular device;. if you use this field, you don’t need to indicate browser_preset as it will be ignored;. minimum value, in pixels: 240. maximum value, in pixels: 9999")
    browser_screen_height: Optional[StrictInt] = Field(default=None, description="browser screen height. optional field. you can set a custom browser screen height to perform audit for a particular device;. if you use this field, you don’t need to indicate browser_preset as it will be ignored;. minimum value, in pixels: 240. maximum value, in pixels: 9999")
    browser_screen_scale_factor: Optional[StrictFloat] = Field(default=None, description="browser screen scale factor. optional field. you can set a custom browser screen resolution ratio to perform audit for a particular device;. if you use this field, you don’t need to indicate browser_preset as it will be ignored;. minimum value: 0.5. maximum value: 3")
    full_page_screenshot: Optional[StrictBool] = Field(default=None, description="take a screenshot of the full page. optional field. set to false if you want to capture only the part of the page displayed before scrolling. default value: true")
    disable_cookie_popup: Optional[StrictBool] = Field(default=None, description="disable the cookie popup . optional field. set to true if you want to disable the popup requesting cookie consent from the user;. default value:. false")
    switch_pool: Optional[StrictBool] = Field(default=None, description="switch proxy pool. optional field. if true, additional proxy pools will be used to obtain the requested data;. the parameter can be used if a multitude of tasks is set simultaneously, resulting in occasional rate-limit and/or site_unreachable errors")
    ip_pool_for_scan: Optional[StrictStr] = Field(default=None, description="proxy pool. optional field. you can choose a location of the proxy pool that will be used to obtain the requested data;. the parameter can be used if page content is inaccessible in one of the locations, resulting in occasional site_unreachable errors. possible values: us, de")
    __properties: ClassVar[List[str]] = [
        "url", 
        "accept_language", 
        "custom_user_agent", 
        "browser_preset", 
        "browser_screen_width", 
        "browser_screen_height", 
        "browser_screen_scale_factor", 
        "full_page_screenshot", 
        "disable_cookie_popup", 
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
        _dict['accept_language'] = self.accept_language
        _dict['custom_user_agent'] = self.custom_user_agent
        _dict['browser_preset'] = self.browser_preset
        _dict['browser_screen_width'] = self.browser_screen_width
        _dict['browser_screen_height'] = self.browser_screen_height
        _dict['browser_screen_scale_factor'] = self.browser_screen_scale_factor
        _dict['full_page_screenshot'] = self.full_page_screenshot
        _dict['disable_cookie_popup'] = self.disable_cookie_popup
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
            "accept_language": obj.get("accept_language"),
            "custom_user_agent": obj.get("custom_user_agent"),
            "browser_preset": obj.get("browser_preset"),
            "browser_screen_width": obj.get("browser_screen_width"),
            "browser_screen_height": obj.get("browser_screen_height"),
            "browser_screen_scale_factor": obj.get("browser_screen_scale_factor"),
            "full_page_screenshot": obj.get("full_page_screenshot"),
            "disable_cookie_popup": obj.get("disable_cookie_popup"),
            "switch_pool": obj.get("switch_pool"),
            "ip_pool_for_scan": obj.get("ip_pool_for_scan"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj