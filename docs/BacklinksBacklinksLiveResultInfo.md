# BacklinksBacklinksLiveResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target** | **str** | target domain in a POST array | [optional] 
**mode** | **str** | mode specified in a POST array | [optional] 
**custom_mode** | **Dict[str, Optional[object]]** | custom mode specified in a POST array | [optional] 
**total_count** | **int** | total amount of results relevant the request | [optional] 
**items_count** | **int** | the number of results returned in the items array | [optional] 
**items** | [**List[BacklinksBacklinksLiveItem]**](BacklinksBacklinksLiveItem.md) | contains relevant backlinks and referring domains data | [optional] 
**search_after_token** | **str** | token for subsequent requests by specifying the unique search_after_token when setting a new task, you will get the subsequent results of the initial task; search_after_token values are unique for each subsequent task | [optional] 

## Example

```python
from dataforseo_client.models.backlinks_backlinks_live_result_info import BacklinksBacklinksLiveResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BacklinksBacklinksLiveResultInfo from a JSON string
backlinks_backlinks_live_result_info_instance = BacklinksBacklinksLiveResultInfo.from_json(json)
# print the JSON string representation of the object
print(BacklinksBacklinksLiveResultInfo.to_json())

# convert the object into a dict
backlinks_backlinks_live_result_info_dict = backlinks_backlinks_live_result_info_instance.to_dict()
# create an instance of BacklinksBacklinksLiveResultInfo from a dict
backlinks_backlinks_live_result_info_form_dict = backlinks_backlinks_live_result_info.from_dict(backlinks_backlinks_live_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


