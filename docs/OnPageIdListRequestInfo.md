# OnPageIdListRequestInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datetime_from** | **str** | start time for filtering results required field if include_metadata is set to true, maximum value: a month from current datetime; if include_metadata is set to false, maximum value: six months from current datetime; must be specified in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2023-01-15 12:57:46 +00:00 | [optional] 
**datetime_to** | **str** | finish time for filtering results required field maximum value: current datetime; must be specified in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2023-01-31 13:57:46 +00:00 | [optional] 
**limit** | **int** | the maximum number of returned task IDs optional field default value: 1000 maximum value: 1000 | [optional] 
**offset** | **int** | offset in the results array of returned task IDs optional field default value: 0 if you specify the 10 value, the first ten tasks in the results array will be omitted | [optional] 
**sort** | **str** | sorting by task execution time optional field possible values: \&quot;asc\&quot;, \&quot;desc\&quot; default value: \&quot;asc\&quot; | [optional] 
**include_metadata** | **bool** | include task metadata in the respond optional field default value: false | [optional] 

## Example

```python
from dataforseo_client.models.on_page_id_list_request_info import OnPageIdListRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OnPageIdListRequestInfo from a JSON string
on_page_id_list_request_info_instance = OnPageIdListRequestInfo.from_json(json)
# print the JSON string representation of the object
print OnPageIdListRequestInfo.to_json()

# convert the object into a dict
on_page_id_list_request_info_dict = on_page_id_list_request_info_instance.to_dict()
# create an instance of OnPageIdListRequestInfo from a dict
on_page_id_list_request_info_form_dict = on_page_id_list_request_info.from_dict(on_page_id_list_request_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


