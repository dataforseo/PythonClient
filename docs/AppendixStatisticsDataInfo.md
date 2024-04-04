# AppendixStatisticsDataInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**day** | [**AppendixStatisticsRatesDataInfo**](AppendixStatisticsRatesDataInfo.md) |  | [optional] 
**minute** | [**AppendixStatisticsRatesDataInfo**](AppendixStatisticsRatesDataInfo.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.appendix_statistics_data_info import AppendixStatisticsDataInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AppendixStatisticsDataInfo from a JSON string
appendix_statistics_data_info_instance = AppendixStatisticsDataInfo.from_json(json)
# print the JSON string representation of the object
print AppendixStatisticsDataInfo.to_json()

# convert the object into a dict
appendix_statistics_data_info_dict = appendix_statistics_data_info_instance.to_dict()
# create an instance of AppendixStatisticsDataInfo from a dict
appendix_statistics_data_info_form_dict = appendix_statistics_data_info.from_dict(appendix_statistics_data_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


