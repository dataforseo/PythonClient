# SerpScreenshotResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items_count** | **int** | number of items in the results array | [optional] 
**items** | [**List[ScreenshotItem]**](ScreenshotItem.md) | items array | [optional] 

## Example

```python
from dataforseo_client.models.serp_screenshot_result_info import SerpScreenshotResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SerpScreenshotResultInfo from a JSON string
serp_screenshot_result_info_instance = SerpScreenshotResultInfo.from_json(json)
# print the JSON string representation of the object
print(SerpScreenshotResultInfo.to_json())

# convert the object into a dict
serp_screenshot_result_info_dict = serp_screenshot_result_info_instance.to_dict()
# create an instance of SerpScreenshotResultInfo from a dict
serp_screenshot_result_info_from_dict = SerpScreenshotResultInfo.from_dict(serp_screenshot_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


