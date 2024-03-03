# SerpScreenshotRequestInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_id** | **str** | task identifier required field unique identifier of the associated task in the UUID format you will be able to use it within 7 days to request the results of the task at any time | [optional] 
**browser_preset** | **str** | browser resolution preset optional field browser preset associated with a certain device type can take the following values: desktop, tablet, mobile note: by default, browser preset corresponds to the device type specified in the POST request | [optional] 
**browser_screen_width** | **int** | width of the browser resolution optional field can be specified in the following range: 240-9999 | [optional] 
**browser_screen_height** | **int** | height of the browser resolution optional field can be specified in the following range: 240-9999 | [optional] 
**browser_screen_scale_factor** | **float** | browser scale factor optional field can be specified in the following range: 0.5-3 | [optional] 

## Example

```python
from dataforseo_client.models.serp_screenshot_request_info import SerpScreenshotRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SerpScreenshotRequestInfo from a JSON string
serp_screenshot_request_info_instance = SerpScreenshotRequestInfo.from_json(json)
# print the JSON string representation of the object
print SerpScreenshotRequestInfo.to_json()

# convert the object into a dict
serp_screenshot_request_info_dict = serp_screenshot_request_info_instance.to_dict()
# create an instance of SerpScreenshotRequestInfo from a dict
serp_screenshot_request_info_form_dict = serp_screenshot_request_info.from_dict(serp_screenshot_request_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


