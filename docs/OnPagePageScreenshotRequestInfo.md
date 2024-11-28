# OnPagePageScreenshotRequestInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | page url required field absolute URL of the page to snap note: if the URL you indicate here returns a 404 status code or the indicated value is not a valid URL, you will obtain \&quot;error_message\&quot;:\&quot;Screenshot is empty\&quot; in the response array | [optional] 
**accept_language** | **str** | language header for accessing the website optional field all locale formats are supported (xx, xx-XX, xxx-XX, etc.) note: if you do not specify this parameter, some websites may deny access; in this case, you will obtain \&quot;error_message\&quot;:\&quot;Screenshot is empty\&quot; in the response array | [optional] 
**custom_user_agent** | **str** | custom user agent optional field custom user agent for crawling a website example: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36  default value: Mozilla/5.0 (compatible; RSiteAuditor) | [optional] 
**browser_preset** | **str** | preset for browser screen parameters optional field if you use this field, you don’t need to indicate browser_screen_width, browser_screen_height, browser_screen_scale_factor possible values: desktop, mobile, tablet desktop preset will apply the following values: browser_screen_width: 1920 browser_screen_height: 1080 browser_screen_scale_factor: 1 mobile preset will apply the following values: browser_screen_width: 390 browser_screen_height: 844 browser_screen_scale_factor: 3 tablet preset will apply the following values: browser_screen_width: 1024 browser_screen_height: 1366 browser_screen_scale_factor: 2 Note: in this endpoint, the enable_browser_rendering, enable_javascript, load_resources, and enable_xhr parameters are always enabled. | [optional] 
**browser_screen_width** | **int** | browser screen width optional field you can set a custom browser screen width to perform audit for a particular device; if you use this field, you don’t need to indicate browser_preset as it will be ignored; minimum value, in pixels: 240 maximum value, in pixels: 9999 | [optional] 
**browser_screen_height** | **int** | browser screen height optional field you can set a custom browser screen height to perform audit for a particular device; if you use this field, you don’t need to indicate browser_preset as it will be ignored; minimum value, in pixels: 240 maximum value, in pixels: 9999 | [optional] 
**browser_screen_scale_factor** | **float** | browser screen scale factor optional field you can set a custom browser screen resolution ratio to perform audit for a particular device; if you use this field, you don’t need to indicate browser_preset as it will be ignored; minimum value: 0.5 maximum value: 3 | [optional] 
**full_page_screenshot** | **bool** | take a screenshot of the full page optional field set to false if you want to capture only the part of the page displayed before scrolling default value: true | [optional] 
**disable_cookie_popup** | **bool** | disable the cookie popup  optional field set to true if you want to disable the popup requesting cookie consent from the user; default value: false | [optional] 
**switch_pool** | **bool** | switch proxy pool optional field if true, additional proxy pools will be used to obtain the requested data; the parameter can be used if a multitude of tasks is set simultaneously, resulting in occasional rate-limit and/or site_unreachable errors | [optional] 
**ip_pool_for_scan** | **str** | proxy pool optional field you can choose a location of the proxy pool that will be used to obtain the requested data; the parameter can be used if page content is inaccessible in one of the locations, resulting in occasional site_unreachable errors possible values: us, de | [optional] 

## Example

```python
from dataforseo_client.models.on_page_page_screenshot_request_info import OnPagePageScreenshotRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OnPagePageScreenshotRequestInfo from a JSON string
on_page_page_screenshot_request_info_instance = OnPagePageScreenshotRequestInfo.from_json(json)
# print the JSON string representation of the object
print(OnPagePageScreenshotRequestInfo.to_json())

# convert the object into a dict
on_page_page_screenshot_request_info_dict = on_page_page_screenshot_request_info_instance.to_dict()
# create an instance of OnPagePageScreenshotRequestInfo from a dict
on_page_page_screenshot_request_info_from_dict = OnPagePageScreenshotRequestInfo.from_dict(on_page_page_screenshot_request_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


