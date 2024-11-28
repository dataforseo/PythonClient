# OnPageWaterfallRequestInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the task required field you can get this ID in the response of the Task POST endpoint example: “07131248-1535-0216-1000-17384017ad04” | [optional] 
**url** | **str** | page URL required field specify the pages you want to receive timing for | [optional] 
**tag** | **str** | user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response | [optional] 

## Example

```python
from dataforseo_client.models.on_page_waterfall_request_info import OnPageWaterfallRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OnPageWaterfallRequestInfo from a JSON string
on_page_waterfall_request_info_instance = OnPageWaterfallRequestInfo.from_json(json)
# print the JSON string representation of the object
print(OnPageWaterfallRequestInfo.to_json())

# convert the object into a dict
on_page_waterfall_request_info_dict = on_page_waterfall_request_info_instance.to_dict()
# create an instance of OnPageWaterfallRequestInfo from a dict
on_page_waterfall_request_info_from_dict = OnPageWaterfallRequestInfo.from_dict(on_page_waterfall_request_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


