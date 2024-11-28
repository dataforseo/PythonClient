# AppendixStatisticsMoneyData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**day** | [**AppendixDayStatisticsMoneyData**](AppendixDayStatisticsMoneyData.md) |  | [optional] 
**minute** | [**AppendixMinuteStatisticsDataInfo**](AppendixMinuteStatisticsDataInfo.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.appendix_statistics_money_data import AppendixStatisticsMoneyData

# TODO update the JSON string below
json = "{}"
# create an instance of AppendixStatisticsMoneyData from a JSON string
appendix_statistics_money_data_instance = AppendixStatisticsMoneyData.from_json(json)
# print the JSON string representation of the object
print(AppendixStatisticsMoneyData.to_json())

# convert the object into a dict
appendix_statistics_money_data_dict = appendix_statistics_money_data_instance.to_dict()
# create an instance of AppendixStatisticsMoneyData from a dict
appendix_statistics_money_data_from_dict = AppendixStatisticsMoneyData.from_dict(appendix_statistics_money_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


