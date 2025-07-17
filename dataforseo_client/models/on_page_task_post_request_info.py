from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class OnPageTaskPostRequestInfo(BaseModel):
    """
    OnPageTaskPostRequestInfo
    """ # noqa: E501
    target: Optional[StrictStr] = Field(default=None, description="target domain. required field. domain name should be specified without https:// and www.. if you specify the page URL, the results will be returned for the domain included in the URL")
    max_crawl_pages: Optional[StrictInt] = Field(default=None, description="crawled pages limit. required field. the number of pages to crawl on the specified domain. Note:. if you set max_crawl_pages to 1 and do not specify start_url or set a homepage in it, the following sitewide checks will be disabled:. test_canonicalization, enable_www_redirect_check, test_hidden_server_signature, test_page_not_found, test_directory_browsing, test_https_redirect. to enable them anyway, set force_sitewide_checks to trueif you set max_crawl_pages to 1 and specify start_url other than a homepage, all sitewide checks will be disabled;. to enable them anyway, set force_sitewide_checks to true")
    start_url: Optional[StrictStr] = Field(default=None, description="the first url to crawl . optional field. Note: you should specify an absolute URL. if you want to crawl a single page, specify its URL in this field and additionally set the max_crawl_pages parameter to 1. you can also use the live Instant Pages endpoint to get page-specific data")
    force_sitewide_checks: Optional[StrictBool] = Field(default=None, description="enable sitewide checks when crawling a single page. optional field. set to true to get data on sitewide checks when crawling a single page;. default value: false")
    priority_urls: Optional[List[Optional[StrictStr]]] = Field(default=None, description="urls to be crawled bypassing the queue. optional field. URLs specified in this array will be crawled in the first instance, bypassing the crawling queue;. Note: you should specify the absolute URL;. you can specify up to 20 URLs;. all URLs in the array must belong to the target domain;. subdomains will be ignored unless the allow_subdomains parameter is set to trueexample:. 'priority_urls': [. 'https://dataforseo.com/apis/serp-api',. 'https://dataforseo.com/contact'. ]")
    max_crawl_depth: Optional[StrictInt] = Field(default=None, description="crawl depth. optional field. the linking depth of the pages to crawl;. for example, starting page of the crawl is level 0, pages that have links from that page are level 1, etc.")
    crawl_delay: Optional[StrictInt] = Field(default=None, description="delay between hits, ms. optional field. the custom delay between crawler hits to the server. default value: 2000")
    store_raw_html: Optional[StrictBool] = Field(default=None, description="store HTML of crawled pages. optional field. set to true if you want to get the HTML of the page using the OnPage Raw HTML endpoint. default value: false")
    enable_content_parsing: Optional[StrictBool] = Field(default=None, description="parse content on crawled pages. optional field. set to true to use the OnPage Content Parsing endpoint. default value: false")
    support_cookies: Optional[StrictBool] = Field(default=None, description="support cookies on crawled pages. optional field. set to true to support cookies when crawling the pages. default value: false")
    accept_language: Optional[StrictStr] = Field(default=None, description="language header for accessing the website. optional field. all locale formats are supported (xx, xx-XX, xxx-XX, etc.). Note: if you do not specify this parameter, some websites may deny access; in this case, pages will be returned with the 'type':'broken in the response array")
    custom_robots_txt: Optional[StrictStr] = Field(default=None, description="custom robots.txt settings. optional field. example: Disallow: /directory1/")
    robots_txt_merge_mode: Optional[StrictStr] = Field(default=None, description="merge with or override robots.txt settings. optional field. possible values: merge, override;. set to override if you want to ignore website crawling restrictions and other robots.txt settings. default value: merge;. Note: if set to override, specify the custom_robots_txt parameter")
    custom_user_agent: Optional[StrictStr] = Field(default=None, description="custom user agent. optional field. custom user agent for crawling a website. example: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36. . default value: Mozilla/5.0 (compatible; RSiteAuditor)")
    browser_preset: Optional[StrictStr] = Field(default=None, description="preset for browser screen parameters. optional field. if you use this field, you don’t need to indicate browser_screen_width, browser_screen_height, browser_screen_scale_factorpossible values:. desktop, mobile, tabletdesktop preset will apply the following values:browser_screen_width: 1920. browser_screen_height: 1080. browser_screen_scale_factor: 1mobile preset will apply the following values:browser_screen_width: 390. browser_screen_height: 844. browser_screen_scale_factor: 3tablet preset will apply the following values:browser_screen_width: 1024. browser_screen_height: 1366. browser_screen_scale_factor: 2. Note: to use this parameter, set enable_javascript or enable_browser_rendering to true")
    browser_screen_width: Optional[StrictInt] = Field(default=None, description="browser screen width. optional field. you can set a custom browser screen width to perform audit for a particular device;. if you use this field, you don’t need to indicate browser_preset as it will be ignored;. Note: to use this parameter, set enable_javascript or enable_browser_rendering to trueminimum value, in pixels: 240. maximum value, in pixels: 9999")
    browser_screen_height: Optional[StrictInt] = Field(default=None, description="browser screen height. optional field. you can set a custom browser screen height to perform an audit for a particular device;. if you use this field, you don’t need to indicate browser_preset as it will be ignored;. Note: to use this parameter, set enable_javascript or enable_browser_rendering to trueminimum value, in pixels: 240. maximum value, in pixels: 9999")
    browser_screen_scale_factor: Optional[StrictFloat] = Field(default=None, description="browser screen scale factor. optional field. you can set a custom browser screen resolution ratio to perform audit for a particular device;. if you use this field, you don’t need to indicate browser_preset as it will be ignored;. Note: to use this parameter, set enable_javascript or enable_browser_rendering to trueminimum value: 0.5. maximum value: 3")
    respect_sitemap: Optional[StrictBool] = Field(default=None, description="respect sitemap when crawling. optional field. set to true if you want to follow the order of pages indicated in the primary sitemap when crawling;. default value: false. Note: if set to true, the click_depth value in the API response will equal 0;. the max_crawl_depth field of the request will be ignored, you can specify the number of pages to crawl using the max_crawl_pages parameter")
    custom_sitemap: Optional[StrictStr] = Field(default=None, description="custom sitemap url. optional field. the URL of the page where the alternative sitemap is located. Note: if you want to use this parameter, respect_sitemap should be true")
    crawl_sitemap_only: Optional[StrictBool] = Field(default=None, description="crawl only pages indicated in the sitemap. optional field. set to true if you want to crawl only the pages indicated in the sitemap. if you set this parameter to true and do not specify custom_sitemap, we will crawl the default sitemap. default value: false. Note: if you want to use this parameter, respect_sitemap should be true")
    load_resources: Optional[StrictBool] = Field(default=None, description="load resources. optional field. set to true if you want to load image, stylesheets, scripts, and broken resources. default value: false. Note: if you use this parameter, additional charges will apply; learn more about the cost of tasks with this parameter in our help article; the cost can be calculated on the Pricing Page")
    enable_www_redirect_check: Optional[StrictBool] = Field(default=None, description="check if the domain implemented the www redirection. optional field. set to true if you want to check if the requested domain implemented the www to non-www or non-www to www redirect;. default value: false")
    enable_javascript: Optional[StrictBool] = Field(default=None, description="load javascript on a page. optional field. set to true if you want to load the scripts available on a page. default value: false. Note: if you use this parameter, additional charges will apply; learn more about the cost of tasks with this parameter in our help article; the cost can be calculated on the Pricing Page")
    enable_xhr: Optional[StrictBool] = Field(default=None, description="enable XMLHttpRequest on a page. optional field. set to true if you want our crawler to request data from a web server using the XMLHttpRequest object. default value: false;if you use this field, enable_javascript must be set to true;")
    enable_browser_rendering: Optional[StrictBool] = Field(default=None, description="emulate browser rendering to measure Core Web Vitals. optional field. by using this parameter you will be able to emulate a browser when loading a web page;. enable_browser_rendering loads styles, images, fonts, animations, videos, and other resources on a page;. default value: false. set to true to obtain Core Web Vitals (FID, CLS, LCP) metrics in the response;. if you use this field, enable_javascript, and load_resources parameters must be set to true. Note: if you use this parameter, additional charges will apply; learn more about the cost of tasks with this parameter in our help article; the cost can be calculated on the Pricing Page")
    disable_cookie_popup: Optional[StrictBool] = Field(default=None, description="disable the cookie popup. optional field. set to true if you want to disable the popup requesting cookie consent from the user;. default value:. false")
    custom_js: Optional[StrictStr] = Field(default=None, description="custom javascript. optional field. Note that the execution time for the script you enter here should be 700 ms maximum, for example, you can use the following JS snippet to check if the website contains Google Tag Manager as a scr attribute:. let meta = { haveGoogleAnalytics: false, haveTagManager: false };\r\nfor (var i = 0; i < document.scripts.length; i++) {\r\n let src = document.scripts[i].getAttribute(\'src\');\r\n if (src != undefined) {\r\n if (src.indexOf(\'analytics.js\') >= 0)\r\n      meta.haveGoogleAnalytics = true;\r\n\tif (src.indexOf(\'gtm.js\') >= 0)\r\n      meta.haveTagManager = true;\r\n  }\r\n}\r\nmeta;the returned value depends on what you specified in this field. For instance, if you specify the following script:. meta = {}; meta.url = document.URL; meta.test = 'test'; meta;. as a response you will receive the following data:. 'custom_js_response': {. 'url': 'https://dataforseo.com/',. 'test': 'test'. }. Note: the length of the script you enter must be no more than 2000 characters. Note: if you use this parameter, additional charges will apply; learn more about the cost of tasks with this parameter in our help article; the cost can be calculated on the Pricing Page")
    validate_micromarkup: Optional[StrictBool] = Field(default=None, description="enable microdata validation. optional field. set to true if you want to use the OnPage API Microdata endpoint. default value: false")
    allow_subdomains: Optional[StrictBool] = Field(default=None, description="include pages on subdomains. optional field. set to true if you want to crawl all subdomains of a target website. default value: false")
    allowed_subdomains: Optional[List[Optional[StrictStr]]] = Field(default=None, description="subdomains to crawl. optional field. specify subdomains that you want to crawl. example: ['blog.site.com', 'my.site.com', 'shop.site.com']. Note: to use this parameter, the allow_subdomains parameter should be set to false;. otherwise, the content of allowed_subdomains field will be ignored and the results will be returned for all subdomains")
    disallowed_subdomains: Optional[List[Optional[StrictStr]]] = Field(default=None, description="subdomains not to crawl. optional field. specify subdomains that you don’t want to crawl. example: ['status.site.com', 'docs.site.com']. Note: to use this parameter, the allow_subdomains parameter should be set to true")
    check_spell: Optional[StrictBool] = Field(default=None, description="check spelling. optional field. set to true to check spelling on a website using Hunspell library. default value: false")
    check_spell_language: Optional[StrictStr] = Field(default=None, description="language of the spell check. optional field. supported languages: ‘hy’, ‘eu’, ‘bg’, ‘ca’, ‘hr’, ‘cs’, ‘da’, ‘nl’, ‘en’, ‘eo’, ‘et’, ‘fo’, ‘fa’, ‘fr’, ‘fy’, ‘gl’, ‘ka’, ‘de’, ‘el’, ‘he’, ‘hu’, ‘is’, ‘ia’, ‘ga’, ‘it’, ‘rw’, ‘la’, ‘lv’, ‘lt’, ‘mk’, ‘mn’, ‘ne’, ‘nb’, ‘nn’, ‘pl’, ‘pt’, ‘ro’, ‘gd’, ‘sr’, ‘sk’, ‘sl’, ‘es’, ‘sv’, ‘tr’, ‘tk’, ‘uk’, ‘vi’. Note: if no language is specified, it will be set automatically based on page content")
    check_spell_exceptions: Optional[List[Optional[StrictStr]]] = Field(default=None, description="words excluded from spell check. optional field. specify the words that you want to exclude from spell check. maximum word length: 100 characters. maximum amount of words: 1000. example: 'SERP', 'minifiers', 'JavaScript'")
    calculate_keyword_density: Optional[StrictBool] = Field(default=None, description="calculate keyword density for the target domain. optional field. set to true if you want to calculate keyword density for website pages. default value: false. Note: if you use this parameter, additional charges will apply; learn more about the cost of tasks with this parameter in our help article. once the crawl is completed, you can obtain keyword density values with the Keyword Density endpoint")
    checks_threshold: Optional[Dict[str, Optional[StrictInt]]] = Field(default=None, description="custom threshold values for checks. optional field. you can specify custom threshold values for the parameters included in the checks object of OnPage API responses;. Note: only integer threshold values can be modified;. for example, the high_loading_time and large_page_size parameters are set to 3 seconds and 1 megabyte respectively by default;. if you want to change these thresholds to 1 second and 1000 kbytes, use the following snippet:. 'checks_threshold': {. 'high_loading_time': 1,. 'large_page_size': 1000. }available customizable parameters with default values:. 'title_too_short', default value: 30, type: 'int'. 'title_too_long', default value: 65, type: 'int'. 'small_page_size', default value: 1024, type: 'int'. 'large_page_size', default value: 1048576 (1024 * 1024), type: 'int'. 'low_character_count', default value: 1024, type: 'int'. 'high_character_count', default value: 256000 (250 * 1024), type: 'int'. 'low_content_rate', default value: 0.1, type: 'float'. 'high_content_rate', default value: 0.9, type: 'float'. 'high_loading_time', default value: 3000, type: 'int'. 'high_waiting_time', default value: 1500, type: 'int'. 'low_readability_rate', default value: 15.0, type: 'float'. 'irrelevant_description', default value: 0.2, type: 'float'. 'irrelevant_title', default value: 0.3, type: 'float'. 'irrelevant_meta_keywords', default value: 0.6, type: 'float'")
    disable_sitewide_checks: Optional[List[Optional[StrictStr]]] = Field(default=None, description="prevent certain sitewide checks from running. optional field. specify the following checks to prevent them from running on the target website:. 'test_page_not_found'. 'test_canonicalization'. 'test_https_redirect'. 'test_directory_browsing'example:. 'disable_sitewide_checks': ['test_directory_browsing', 'test_page_not_found']learn more on our help center")
    disable_page_checks: Optional[List[Optional[StrictStr]]] = Field(default=None, description="prevent certain page checks from running. optional field. specify certain checks to prevent them from running and impacting the onpage_scoreexample:. 'disable_page_checks': ['is_5xx_code', 'is_4xx_code']")
    switch_pool: Optional[StrictBool] = Field(default=None, description="switch proxy pool. optional field. if true, additional proxy pools will be used to obtain the requested data;. the parameter can be used if a multitude of tasks is set simultaneously, resulting in occasional rate-limit and/or site_unreachable errors")
    return_despite_timeout: Optional[StrictBool] = Field(default=None, description="return data on pages despite the timeout error. optional field. if true, the data will be provided on pages that failed to load within 120 seconds and responded with a timeout error;. default value: false")
    tag: Optional[StrictStr] = Field(default=None, description="user-defined task identifier. optional field. the character limit is 255. you can use this parameter to identify the task and match it with the result. you will find the specified tag value in the data object of the response")
    pingback_url: Optional[StrictStr] = Field(default=None, description="notification URL of a completed task. optional field. when a task is completed we will notify you by GET request sent to the URL you have specified. you can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the request.. example:. http://your-server.com/pingscript?id=$id. http://your-server.com/pingscript?id=$id&tag=$tag. Note: special characters in pingback_url will be urlencoded;. i.a., the # character will be encoded into %23. learn more on our Help Center")
    __properties: ClassVar[List[str]] = [
        "target", 
        "max_crawl_pages", 
        "start_url", 
        "force_sitewide_checks", 
        "priority_urls", 
        "max_crawl_depth", 
        "crawl_delay", 
        "store_raw_html", 
        "enable_content_parsing", 
        "support_cookies", 
        "accept_language", 
        "custom_robots_txt", 
        "robots_txt_merge_mode", 
        "custom_user_agent", 
        "browser_preset", 
        "browser_screen_width", 
        "browser_screen_height", 
        "browser_screen_scale_factor", 
        "respect_sitemap", 
        "custom_sitemap", 
        "crawl_sitemap_only", 
        "load_resources", 
        "enable_www_redirect_check", 
        "enable_javascript", 
        "enable_xhr", 
        "enable_browser_rendering", 
        "disable_cookie_popup", 
        "custom_js", 
        "validate_micromarkup", 
        "allow_subdomains", 
        "allowed_subdomains", 
        "disallowed_subdomains", 
        "check_spell", 
        "check_spell_language", 
        "check_spell_exceptions", 
        "calculate_keyword_density", 
        "checks_threshold", 
        "disable_sitewide_checks", 
        "disable_page_checks", 
        "switch_pool", 
        "return_despite_timeout", 
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

        _dict['target'] = self.target
        _dict['max_crawl_pages'] = self.max_crawl_pages
        _dict['start_url'] = self.start_url
        _dict['force_sitewide_checks'] = self.force_sitewide_checks
        _dict['priority_urls'] = self.priority_urls
        _dict['max_crawl_depth'] = self.max_crawl_depth
        _dict['crawl_delay'] = self.crawl_delay
        _dict['store_raw_html'] = self.store_raw_html
        _dict['enable_content_parsing'] = self.enable_content_parsing
        _dict['support_cookies'] = self.support_cookies
        _dict['accept_language'] = self.accept_language
        _dict['custom_robots_txt'] = self.custom_robots_txt
        _dict['robots_txt_merge_mode'] = self.robots_txt_merge_mode
        _dict['custom_user_agent'] = self.custom_user_agent
        _dict['browser_preset'] = self.browser_preset
        _dict['browser_screen_width'] = self.browser_screen_width
        _dict['browser_screen_height'] = self.browser_screen_height
        _dict['browser_screen_scale_factor'] = self.browser_screen_scale_factor
        _dict['respect_sitemap'] = self.respect_sitemap
        _dict['custom_sitemap'] = self.custom_sitemap
        _dict['crawl_sitemap_only'] = self.crawl_sitemap_only
        _dict['load_resources'] = self.load_resources
        _dict['enable_www_redirect_check'] = self.enable_www_redirect_check
        _dict['enable_javascript'] = self.enable_javascript
        _dict['enable_xhr'] = self.enable_xhr
        _dict['enable_browser_rendering'] = self.enable_browser_rendering
        _dict['disable_cookie_popup'] = self.disable_cookie_popup
        _dict['custom_js'] = self.custom_js
        _dict['validate_micromarkup'] = self.validate_micromarkup
        _dict['allow_subdomains'] = self.allow_subdomains
        _dict['allowed_subdomains'] = self.allowed_subdomains
        _dict['disallowed_subdomains'] = self.disallowed_subdomains
        _dict['check_spell'] = self.check_spell
        _dict['check_spell_language'] = self.check_spell_language
        _dict['check_spell_exceptions'] = self.check_spell_exceptions
        _dict['calculate_keyword_density'] = self.calculate_keyword_density
        _dict['checks_threshold'] = self.checks_threshold
        _dict['disable_sitewide_checks'] = self.disable_sitewide_checks
        _dict['disable_page_checks'] = self.disable_page_checks
        _dict['switch_pool'] = self.switch_pool
        _dict['return_despite_timeout'] = self.return_despite_timeout
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
            "target": obj.get("target"),
            "max_crawl_pages": obj.get("max_crawl_pages"),
            "start_url": obj.get("start_url"),
            "force_sitewide_checks": obj.get("force_sitewide_checks"),
            "priority_urls": obj.get("priority_urls"),
            "max_crawl_depth": obj.get("max_crawl_depth"),
            "crawl_delay": obj.get("crawl_delay"),
            "store_raw_html": obj.get("store_raw_html"),
            "enable_content_parsing": obj.get("enable_content_parsing"),
            "support_cookies": obj.get("support_cookies"),
            "accept_language": obj.get("accept_language"),
            "custom_robots_txt": obj.get("custom_robots_txt"),
            "robots_txt_merge_mode": obj.get("robots_txt_merge_mode"),
            "custom_user_agent": obj.get("custom_user_agent"),
            "browser_preset": obj.get("browser_preset"),
            "browser_screen_width": obj.get("browser_screen_width"),
            "browser_screen_height": obj.get("browser_screen_height"),
            "browser_screen_scale_factor": obj.get("browser_screen_scale_factor"),
            "respect_sitemap": obj.get("respect_sitemap"),
            "custom_sitemap": obj.get("custom_sitemap"),
            "crawl_sitemap_only": obj.get("crawl_sitemap_only"),
            "load_resources": obj.get("load_resources"),
            "enable_www_redirect_check": obj.get("enable_www_redirect_check"),
            "enable_javascript": obj.get("enable_javascript"),
            "enable_xhr": obj.get("enable_xhr"),
            "enable_browser_rendering": obj.get("enable_browser_rendering"),
            "disable_cookie_popup": obj.get("disable_cookie_popup"),
            "custom_js": obj.get("custom_js"),
            "validate_micromarkup": obj.get("validate_micromarkup"),
            "allow_subdomains": obj.get("allow_subdomains"),
            "allowed_subdomains": obj.get("allowed_subdomains"),
            "disallowed_subdomains": obj.get("disallowed_subdomains"),
            "check_spell": obj.get("check_spell"),
            "check_spell_language": obj.get("check_spell_language"),
            "check_spell_exceptions": obj.get("check_spell_exceptions"),
            "calculate_keyword_density": obj.get("calculate_keyword_density"),
            "checks_threshold": obj.get("checks_threshold"),
            "disable_sitewide_checks": obj.get("disable_sitewide_checks"),
            "disable_page_checks": obj.get("disable_page_checks"),
            "switch_pool": obj.get("switch_pool"),
            "return_despite_timeout": obj.get("return_despite_timeout"),
            "tag": obj.get("tag"),
            "pingback_url": obj.get("pingback_url"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj