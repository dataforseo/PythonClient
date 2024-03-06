[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# OnPageInstantPagesRequestInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | target page url required field absolute URL of the target page Note: results will be returned for the specified URL only Note: to prevent denial-of-service events, tasks that contain a duplicate crawl host will be returned with a 40501 error; to prevent this error from occuring, avoid setting tasks with the same domain if at least one of your previous tasks with this domain (including a page URL on the domain) is still in a crawling queue | [optional]
**custom_user_agent** | **str** | custom user agent optional field custom user agent for crawling a website example: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36  default value: Mozilla/5.0 (compatible; RSiteAuditor) | [optional]
**browser_preset** | **str** | preset for browser screen parameters optional field if you use this field, you don’t need to indicate browser_screen_width, browser_screen_height, browser_screen_scale_factorpossible values: desktop, mobile, tabletdesktop preset will apply the following values: browser_screen_width: 1920 browser_screen_height: 1080 browser_screen_scale_factor: 1 mobile preset will apply the following values: browser_screen_width: 390 browser_screen_height: 844 browser_screen_scale_factor: 3 tablet preset will apply the following values: browser_screen_width: 1024 browser_screen_height: 1366 browser_screen_scale_factor: 2 Note: to use this parameter, set enable_javascript or enable_browser_rendering to true | [optional]
**browser_screen_width** | **int** | browser screen width optional field you can set a custom browser screen width to perform audit for a particular device; if you use this field, you don’t need to indicate browser_preset as it will be ignored;Note: to use this parameter, set enable_javascript or enable_browser_rendering to trueminimum value, in pixels: 240 maximum value, in pixels: 9999 | [optional]
**browser_screen_height** | **int** | browser screen height optional field you can set a custom browser screen height to perform audit for a particular device; if you use this field, you don’t need to indicate browser_preset as it will be ignored;Note: to use this parameter, set enable_javascript or enable_browser_rendering to trueminimum value, in pixels: 240 maximum value, in pixels: 9999 | [optional]
**browser_screen_scale_factor** | **float** | browser screen scale factor optional field you can set a custom browser screen resolution ratio to perform audit for a particular device; if you use this field, you don’t need to indicate browser_preset as it will be ignored;Note: to use this parameter, set enable_javascript or enable_browser_rendering to trueminimum value: 0.5 maximum value: 3 | [optional]
**store_raw_html** | **bool** | store HTML of a crawled page optional field set to true if you want get the HTML of the page using the OnPage Raw HTML endpoint default value: false | [optional]
**accept_language** | **str** | language header for accessing the website optional field all locale formats are supported (xx, xx-XX, xxx-XX, etc.) Note: if you do not specify this parameter, some websites may deny access; in this case, pages will be returned with the \&quot;type\&quot;:\&quot;broken in the response array | [optional]
**enable_javascript** | **bool** | load javascript on a page optional field set to true if you want to load the scripts available on a page default value: false Note: if you use this parameter, additional charges will apply; learn more about the cost of tasks with this parameter in our help article; the cost can be calculated on the Pricing Page | [optional]
**enable_browser_rendering** | **bool** | emulate browser rendering to measure Core Web Vitals optional field by using this parameter you will be able to emulate a browser when loading a web page; enable_browser_rendering loads styles, images, fonts, animations, videos, and other resources on a page; default value: false set to true to obtain Core Web Vitals (FID, CLS, LCP) metrics in the response; if you use this field, enable_javascript, and load_resources parameters must be set to true Note: if you use this parameter, additional charges will apply; learn more about the cost of tasks with this parameter in our help article; the cost can be calculated on the Pricing Page | [optional]
**disable_cookie_popup** | **bool** | disable the cookie popup  optional field set to true if you want to disable the popup requesting cookie consent from the user; default value: false | [optional]
**return_despite_timeout** | **bool** | return data on pages despite the timeout error optional field if true, the data will be provided on pages that failed to load within 120 seconds and responded with a timeout error; default value: false | [optional]
**enable_xhr** | **bool** | enable XMLHttpRequest on a page optional field set to true if you want our crawler to request data from a web server using the XMLHttpRequest object default value: falseif you use this field, enable_javascript must be set to true; | [optional]
**custom_js** | **str** | custom javascript optional fieldNote that the execution time for the script you enter here should be 700 ms maximumfor example, you can use the following JS snippet to check if the website contains Google Tag Manager as a scr attribute: let meta &#x3D; { haveGoogleAnalytics: false, haveTagManager: false };\\r\\nfor (var i &#x3D; 0; i &lt; document.scripts.length; i++) {\\r\\n let src &#x3D; document.scripts[i].getAttribute(\\\&quot;src\\\&quot;);\\r\\n if (src !&#x3D; undefined) {\\r\\n if (src.indexOf(\\\&quot;analytics.js\\\&quot;) &gt;&#x3D; 0)\\r\\n      meta.haveGoogleAnalytics &#x3D; true;\\r\\n\\tif (src.indexOf(\\\&quot;gtm.js\\\&quot;) &gt;&#x3D; 0)\\r\\n      meta.haveTagManager &#x3D; true;\\r\\n  }\\r\\n}\\r\\nmeta;the returned value depends on what you specified in this field. For instance, if you specify the following script: meta &#x3D; {}; meta.url &#x3D; document.URL; meta.test &#x3D; &#39;test&#39;; meta; as a response you will receive the following data: \&quot;custom_js_response\&quot;: { \&quot;url\&quot;: \&quot;https://dataforseo.com/\&quot;, \&quot;test\&quot;: \&quot;test\&quot; } Note: if you use this parameter, additional charges will apply; learn more about the cost of tasks with this parameter in our help article; the cost can be calculated on the Pricing Page | [optional]
**validate_micromarkup** | **bool** | enable microdata validation optional field if set to true, you can use the OnPage API Microdata endpoint with the id of the task; default value: false | [optional]
**check_spell** | **bool** | check spelling optional field set to true to check spelling on a website using Hunspell library default value: false | [optional]
**checks_threshold** | **Dict[str, Optional[int]]** | custom threshold values for checks optional field you can specify custom threshold values for the parameters included in the checks array of OnPage API responses; Note: only integer threshold values can be modified; | [optional]

## Example

```python
from dataforseo_client.models.on_page_instant_pages_request_info import OnPageInstantPagesRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OnPageInstantPagesRequestInfo from a JSON string
on_page_instant_pages_request_info_instance = OnPageInstantPagesRequestInfo.from_json(json)
# print the JSON string representation of the object
print OnPageInstantPagesRequestInfo.to_json()

# convert the object into a dict
on_page_instant_pages_request_info_dict = on_page_instant_pages_request_info_instance.to_dict()
# create an instance of OnPageInstantPagesRequestInfo from a dict
on_page_instant_pages_request_info_form_dict = on_page_instant_pages_request_info.from_dict(on_page_instant_pages_request_info_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")