# OnPageDuplicateTagsRequestInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the task required field you can get this ID in the response of the Task POST endpoint example: “07131248-1535-0216-1000-17384017ad04” | [optional] 
**type** | **str** | type of element | [optional] 
**accumulator** | **str** | tag value optional field specify a title or description here if you want to receive a list of duplicate pages that contains this tag | [optional] 
**limit** | **int** | the maximum number of returned pages optional field default value: 100 maximum value: 1000 | [optional] 
**offset** | **int** | offset in the results array of returned pages optional field default value: 0 if you specify the 10 value, the first ten pages in the results array will be omitted and the data will be provided for the successive pages | [optional] 
**tag** | **str** | user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response | [optional] 

## Example

```python
from dataforseo_client.models.on_page_duplicate_tags_request_info import OnPageDuplicateTagsRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OnPageDuplicateTagsRequestInfo from a JSON string
on_page_duplicate_tags_request_info_instance = OnPageDuplicateTagsRequestInfo.from_json(json)
# print the JSON string representation of the object
print(OnPageDuplicateTagsRequestInfo.to_json())

# convert the object into a dict
on_page_duplicate_tags_request_info_dict = on_page_duplicate_tags_request_info_instance.to_dict()
# create an instance of OnPageDuplicateTagsRequestInfo from a dict
on_page_duplicate_tags_request_info_from_dict = OnPageDuplicateTagsRequestInfo.from_dict(on_page_duplicate_tags_request_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


