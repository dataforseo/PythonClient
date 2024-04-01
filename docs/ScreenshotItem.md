# ScreenshotItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image** | **str** | screenshot of the requested page URL of the page screenshot on the DataForSEO storage note: the page screenshot saved on the DataForSEO storage only remains accessible for one day after making the request | [optional] 

## Example

```python
from dataforseo_client.models.screenshot_item import ScreenshotItem

# TODO update the JSON string below
json = "{}"
# create an instance of ScreenshotItem from a JSON string
screenshot_item_instance = ScreenshotItem.from_json(json)
# print the JSON string representation of the object
print(ScreenshotItem.to_json())

# convert the object into a dict
screenshot_item_dict = screenshot_item_instance.to_dict()
# create an instance of ScreenshotItem from a dict
screenshot_item_form_dict = screenshot_item.from_dict(screenshot_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


