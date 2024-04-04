# BacklinksHistoryLiveRequestInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target** | **str** | domain required field a domain should be specified without https:// and www. | [optional] 
**date_from** | **str** | starting date of the time range optional field minimum value 2019-01-01 if you don’t specify this field, the minimum value will be used by default date format: \&quot;yyyy-mm-dd\&quot; example: \&quot;2019-01-15\&quot; | [optional] 
**date_to** | **str** | ending date of the time range optional field if you don’t specify this field, the today’s date will be used by default date format: \&quot;yyyy-mm-dd\&quot; example: \&quot;2019-01-15\&quot; | [optional] 
**tag** | **str** | user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response | [optional] 

## Example

```python
from dataforseo_client.models.backlinks_history_live_request_info import BacklinksHistoryLiveRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BacklinksHistoryLiveRequestInfo from a JSON string
backlinks_history_live_request_info_instance = BacklinksHistoryLiveRequestInfo.from_json(json)
# print the JSON string representation of the object
print BacklinksHistoryLiveRequestInfo.to_json()

# convert the object into a dict
backlinks_history_live_request_info_dict = backlinks_history_live_request_info_instance.to_dict()
# create an instance of BacklinksHistoryLiveRequestInfo from a dict
backlinks_history_live_request_info_form_dict = backlinks_history_live_request_info.from_dict(backlinks_history_live_request_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


