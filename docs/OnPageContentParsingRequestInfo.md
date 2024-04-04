# OnPageContentParsingRequestInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | URL of the content to parse required field URL of the page to parse example: https://www.fujielectric.com/ | [optional] 
**id** | **str** | ID of the task required field you can get this ID in the response of the Task POST endpoint note: the enable_content_parsing parameter in the POST request must be set to true example: \&quot;07131248-1535-0216-1000-17384017ad04\&quot; | [optional] 

## Example

```python
from dataforseo_client.models.on_page_content_parsing_request_info import OnPageContentParsingRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OnPageContentParsingRequestInfo from a JSON string
on_page_content_parsing_request_info_instance = OnPageContentParsingRequestInfo.from_json(json)
# print the JSON string representation of the object
print OnPageContentParsingRequestInfo.to_json()

# convert the object into a dict
on_page_content_parsing_request_info_dict = on_page_content_parsing_request_info_instance.to_dict()
# create an instance of OnPageContentParsingRequestInfo from a dict
on_page_content_parsing_request_info_form_dict = on_page_content_parsing_request_info.from_dict(on_page_content_parsing_request_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


