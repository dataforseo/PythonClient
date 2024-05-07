# AppendixPriorityTasksReadyKeywordsDataPriceDataInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cost_type** | **str** | charge type can take the following values: per_result – charge for every row in the result array per_request – charge for a GET or POST request | [optional] 
**cost** | **float** | cost, USD | [optional] 

## Example

```python
from dataforseo_client.models.appendix_priority_tasks_ready_keywords_data_price_data_info import AppendixPriorityTasksReadyKeywordsDataPriceDataInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AppendixPriorityTasksReadyKeywordsDataPriceDataInfo from a JSON string
appendix_priority_tasks_ready_keywords_data_price_data_info_instance = AppendixPriorityTasksReadyKeywordsDataPriceDataInfo.from_json(json)
# print the JSON string representation of the object
print AppendixPriorityTasksReadyKeywordsDataPriceDataInfo.to_json()

# convert the object into a dict
appendix_priority_tasks_ready_keywords_data_price_data_info_dict = appendix_priority_tasks_ready_keywords_data_price_data_info_instance.to_dict()
# create an instance of AppendixPriorityTasksReadyKeywordsDataPriceDataInfo from a dict
appendix_priority_tasks_ready_keywords_data_price_data_info_form_dict = appendix_priority_tasks_ready_keywords_data_price_data_info.from_dict(appendix_priority_tasks_ready_keywords_data_price_data_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


