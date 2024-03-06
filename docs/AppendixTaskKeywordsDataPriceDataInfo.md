[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# AppendixTaskKeywordsDataPriceDataInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**priority_low** | [**List[AppendixPriorityTasksReadyKeywordsDataPriceDataInfo]**](AppendixPriorityTasksReadyKeywordsDataPriceDataInfo.md) |  | [optional]
**priority_normal** | [**List[AppendixPriorityTasksReadyKeywordsDataPriceDataInfo]**](AppendixPriorityTasksReadyKeywordsDataPriceDataInfo.md) |  | [optional]
**priority_high** | [**List[AppendixPriorityTasksReadyKeywordsDataPriceDataInfo]**](AppendixPriorityTasksReadyKeywordsDataPriceDataInfo.md) |  | [optional]

## Example

```python
from dataforseo_client.models.appendix_task_keywords_data_price_data_info import AppendixTaskKeywordsDataPriceDataInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AppendixTaskKeywordsDataPriceDataInfo from a JSON string
appendix_task_keywords_data_price_data_info_instance = AppendixTaskKeywordsDataPriceDataInfo.from_json(json)
# print the JSON string representation of the object
print AppendixTaskKeywordsDataPriceDataInfo.to_json()

# convert the object into a dict
appendix_task_keywords_data_price_data_info_dict = appendix_task_keywords_data_price_data_info_instance.to_dict()
# create an instance of AppendixTaskKeywordsDataPriceDataInfo from a dict
appendix_task_keywords_data_price_data_info_form_dict = appendix_task_keywords_data_price_data_info.from_dict(appendix_task_keywords_data_price_data_info_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")