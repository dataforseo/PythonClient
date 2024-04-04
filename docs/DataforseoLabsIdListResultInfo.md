# DataforseoLabsIdListResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | id of the task | [optional] 
**url** | **str** | URL of the task URL you used for making an API call | [optional] 
**datetime_posted** | **str** | date and time when the task was made in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2023-01-15 12:57:46 +00:00 | [optional] 
**datetime_done** | **str** | date and time when the task was completed in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2023-01-15 12:57:46 +00:00 | [optional] 
**status** | **str** | informational message of the task you can find the full list of general informational messages here | [optional] 
**cost** | **float** | cost of the task, USD | [optional] 
**metadata** | **object** | contains parameters you specified in the POST request | [optional] 

## Example

```python
from dataforseo_client.models.dataforseo_labs_id_list_result_info import DataforseoLabsIdListResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DataforseoLabsIdListResultInfo from a JSON string
dataforseo_labs_id_list_result_info_instance = DataforseoLabsIdListResultInfo.from_json(json)
# print the JSON string representation of the object
print DataforseoLabsIdListResultInfo.to_json()

# convert the object into a dict
dataforseo_labs_id_list_result_info_dict = dataforseo_labs_id_list_result_info_instance.to_dict()
# create an instance of DataforseoLabsIdListResultInfo from a dict
dataforseo_labs_id_list_result_info_form_dict = dataforseo_labs_id_list_result_info.from_dict(dataforseo_labs_id_list_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


