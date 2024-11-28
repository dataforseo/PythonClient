# OnPageRawHtmlRequestInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the task required field you can get this ID in the response of the Task POST endpoint example: “07131248-1535-0216-1000-17384017ad04” | [optional] 
**url** | **str** | page url required field the absolute URL of a page to request HTML Note: this field is optional if the task was set using the Instant Pages endpoint | [optional] 

## Example

```python
from dataforseo_client.models.on_page_raw_html_request_info import OnPageRawHtmlRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OnPageRawHtmlRequestInfo from a JSON string
on_page_raw_html_request_info_instance = OnPageRawHtmlRequestInfo.from_json(json)
# print the JSON string representation of the object
print(OnPageRawHtmlRequestInfo.to_json())

# convert the object into a dict
on_page_raw_html_request_info_dict = on_page_raw_html_request_info_instance.to_dict()
# create an instance of OnPageRawHtmlRequestInfo from a dict
on_page_raw_html_request_info_from_dict = OnPageRawHtmlRequestInfo.from_dict(on_page_raw_html_request_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


