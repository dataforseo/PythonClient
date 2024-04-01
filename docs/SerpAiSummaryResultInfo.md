# SerpAiSummaryResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items_count** | **int** | number of items in the results array | [optional] 
**items** | [**List[SerpAiSummaryItem]**](SerpAiSummaryItem.md) | items array | [optional] 

## Example

```python
from dataforseo_client.models.serp_ai_summary_result_info import SerpAiSummaryResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SerpAiSummaryResultInfo from a JSON string
serp_ai_summary_result_info_instance = SerpAiSummaryResultInfo.from_json(json)
# print the JSON string representation of the object
print(SerpAiSummaryResultInfo.to_json())

# convert the object into a dict
serp_ai_summary_result_info_dict = serp_ai_summary_result_info_instance.to_dict()
# create an instance of SerpAiSummaryResultInfo from a dict
serp_ai_summary_result_info_form_dict = serp_ai_summary_result_info.from_dict(serp_ai_summary_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


